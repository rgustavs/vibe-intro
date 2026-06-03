#!/usr/bin/env python3
"""
Generate slide images from the prompts declared in the deck content.

This is intentionally NOT part of build.py: generating images costs money and
needs both network and an API key. So you run it by hand, commit the resulting
PNGs into src/assets/images/, and build.py then base64-embeds them into the
self-contained decks — exactly the same split as the fonts pipeline.

Workflow
--------
1. Declare an image in a slide (src/content/NN-name.md):

       :::image
       slug: agent-loop
       alt: A four-step feedback loop diagram
       caption: describe -> run -> review -> refine
       prompt:
       A four-step loop drawn as four soft rounded nodes connected by
       gentle arrows, each node a different muted earthy tone.
       :::

   Only `slug` and `prompt` are needed to generate; `alt`/`caption` are used
   by build.py when the image is placed on the slide.

2. Set a key and run the generator (once, on a machine with internet):

       export OPENAI_API_KEY=sk-...
       python tools/generate_images.py             # generate missing images
       python tools/generate_images.py --force     # regenerate everything
       python tools/generate_images.py --only agent-loop   # one slug (repeatable)
       python tools/generate_images.py --list      # list declared images, do nothing

3. Commit src/assets/images/*.png, then run `python build.py`.

Every prompt is wrapped in a shared style template so the whole deck stays
visually consistent. Edit src/assets/images/prompt_template.txt to change the
house style (it must contain the literal placeholder "{prompt}"); otherwise the
built-in DEFAULT_TEMPLATE below is used.

Only the Python standard library is used. OpenAI is the starting point; to add a
provider, write another generate_<name>() and register it in PROVIDERS.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "src", "content")
IMAGES = os.path.join(ROOT, "src", "assets", "images")
TEMPLATE_FILE = os.path.join(IMAGES, "prompt_template.txt")

DEFAULT_SIZE = "1536x1024"   # landscape; fits slide figures well
DEFAULT_MODEL = "gpt-image-1"

DEFAULT_TEMPLATE = (
    "Editorial, minimal flat-vector illustration for a calm teaching slide "
    "deck. Soft, muted earthy palette: sage green (#6F7F6A), slate blue "
    "(#8FA9B8), warm tan (#C9BAA6), pale sage (#A8BDB6), on a warm off-white "
    "background (#F7F4EE). Generous negative space, gentle geometric shapes, "
    "soft natural lighting, friendly and modern. No text, no lettering, no "
    "logos, no watermarks.\n\nSubject: {prompt}"
)

# Matches a :::image ... ::: block and captures its inner body.
IMAGE_BLOCK_RE = re.compile(r"(?ms)^:::image[ \t]*$\n(.*?)^:::[ \t]*$")


# --------------------------------------------------------------------------
# discovery (mirrors parse_image_block in build.py)
# --------------------------------------------------------------------------

def parse_image_block(raw):
    meta = {"slug": "", "alt": "", "caption": "", "size": "", "prompt": ""}
    lines = raw.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^\s*(\w+)\s*:\s?(.*)$", lines[i])
        if m and m.group(1) in meta:
            key, val = m.group(1), m.group(2)
            if key == "prompt":
                rest = [val] if val.strip() else []
                rest.extend(lines[i + 1:])
                meta["prompt"] = "\n".join(rest).strip()
                break
            meta[key] = val.strip()
        i += 1
    return meta


def discover_images():
    """Scan all content for :::image blocks. Return ordered list of specs."""
    found = {}
    order = []
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(CONTENT, fn), "r", encoding="utf-8") as f:
            text = f.read()
        for body in IMAGE_BLOCK_RE.findall(text):
            meta = parse_image_block(body)
            slug = meta["slug"]
            if not slug:
                print("  skip: :::image without slug in %s" % fn, file=sys.stderr)
                continue
            if not meta["prompt"]:
                print("  skip: image '%s' in %s has no prompt" % (slug, fn),
                      file=sys.stderr)
                continue
            if slug in found:
                if found[slug]["prompt"] != meta["prompt"]:
                    print("  warning: duplicate slug '%s' with a different "
                          "prompt (%s) — keeping the first" % (slug, fn),
                          file=sys.stderr)
                continue
            meta["source"] = fn
            found[slug] = meta
            order.append(slug)
    return [found[s] for s in order]


def load_template():
    if os.path.isfile(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            tpl = f.read().strip()
        if "{prompt}" in tpl:
            return tpl
        print("  warning: %s has no {prompt} placeholder — using built-in "
              "template" % os.path.relpath(TEMPLATE_FILE, ROOT), file=sys.stderr)
    return DEFAULT_TEMPLATE


# --------------------------------------------------------------------------
# providers
# --------------------------------------------------------------------------

def generate_openai(prompt, size, model):
    """Call the OpenAI Images API and return raw PNG bytes."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("error: OPENAI_API_KEY is not set. export it and re-run.")
    body = json.dumps({
        "model": model, "prompt": prompt, "size": size, "n": 1,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body, method="POST",
        headers={"Authorization": "Bearer " + api_key,
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            payload = json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        sys.exit("error: OpenAI API %s\n%s" % (e.code, detail))
    return base64.b64decode(payload["data"][0]["b64_json"])


PROVIDERS = {"openai": generate_openai}


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--provider", default="openai", choices=sorted(PROVIDERS),
                    help="image provider (default: openai)")
    ap.add_argument("--model", default=DEFAULT_MODEL,
                    help="model name (default: %s)" % DEFAULT_MODEL)
    ap.add_argument("--size", default=None,
                    help="override size for all images (default per-image or %s)"
                         % DEFAULT_SIZE)
    ap.add_argument("--only", action="append", metavar="SLUG", default=[],
                    help="generate only this slug (repeatable)")
    ap.add_argument("--force", action="store_true",
                    help="regenerate images that already exist")
    ap.add_argument("--list", action="store_true",
                    help="list declared images and exit")
    args = ap.parse_args()

    specs = discover_images()
    if not specs:
        print("No :::image blocks found in src/content/. Nothing to do.")
        return

    if args.list:
        print("Declared images (%d):" % len(specs))
        for s in specs:
            exists = any(os.path.isfile(os.path.join(IMAGES, s["slug"] + e))
                         for e in (".png", ".webp", ".jpg", ".jpeg"))
            mark = "have" if exists else "MISSING"
            print("  [%-7s] %-22s %s" % (mark, s["slug"], s["source"]))
        return

    os.makedirs(IMAGES, exist_ok=True)
    template = load_template()
    generate = PROVIDERS[args.provider]
    only = set(args.only)

    made = skipped = 0
    for s in specs:
        slug = s["slug"]
        if only and slug not in only:
            continue
        dest = os.path.join(IMAGES, slug + ".png")
        if os.path.isfile(dest) and not args.force:
            print("  skip %s (exists; --force to regenerate)" % slug)
            skipped += 1
            continue
        size = args.size or s["size"] or DEFAULT_SIZE
        prompt = template.replace("{prompt}", s["prompt"])
        print("  generating %s (%s, %s)..." % (slug, args.model, size))
        data = generate(prompt, size, args.model)
        with open(dest, "wb") as f:
            f.write(data)
        print("    wrote %s (%d bytes)" % (os.path.relpath(dest, ROOT), len(data)))
        made += 1

    if only:
        missing = only - {s["slug"] for s in specs}
        for m in sorted(missing):
            print("  warning: --only %s not found in content" % m, file=sys.stderr)
    print("\nDone. %d generated, %d skipped. Now run: python build.py" % (made, skipped))


if __name__ == "__main__":
    main()
