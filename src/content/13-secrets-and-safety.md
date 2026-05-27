@@
type: title
eyebrow: A working introduction · appendix D
title: Secrets &|*Safety.*
@@
The few rules that keep keys, passwords, and private data|out of the wrong place — including your code.

===

@@
type: default
eyebrow: 01 · Why this matters
title: Some strings are *keys.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">As soon as your app talks to a paid service or holds real data, it needs <em>secrets</em> — keys and passwords that prove it's allowed in. A leaked key can run up a bill or expose information in your name.</p>
    <p class="body subtext">The good news: keeping secrets safe is a handful of habits, not a deep skill. Learn them once and they become automatic.</p>
  </div>
  <div class="card">
    <div class="label">What's at stake</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>A leaked API key can cost real money</li>
      <li>A leaked password can expose private data</li>
      <li>Once it's public, you must assume it's compromised</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · Definition
title: A secret is a *credential.*
@@
:::anatomy
- API key | Proves your app may use a paid service | Like a card number for an AI or email service.
- Password | Proves who you are to a system | For a database, an account, a dashboard.
- Token | A temporary pass, often standing in for a login | Grants access for a while, then expires.
- Connection string | Address plus credentials for a database | Bundles "where" and "who" into one line.
lede: If it would let a stranger act as you or spend your money, treat it as a secret.
:::

===

@@
type: default
eyebrow: 03 · The pattern
title: Secrets live in a *.env* file.
@@
:::anatomy
- The .env file | A plain file holding your secrets | Sits in the project, never shared.
- .gitignore | Tells Git to ignore .env | So secrets are never committed or pushed.
- The code | Reads secrets from the environment | It uses the key without ever containing it.
lede: The values stay on your machine; the code only knows the name to look up — never the secret itself.
:::

===

@@
type: default
eyebrow: 04 · Principle 1
title: Never *commit* a secret.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="label">Why it's so easy to slip</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Pasting a key straight into the code "just to test"</li>
      <li>Committing before .env is in .gitignore</li>
      <li>Once pushed, it's in the history — even if you delete it later</li>
    </ul>
  </div>
  <p class="lede">Ask the agent up front: "set this up with a .env file and make sure it's gitignored." It knows the pattern — let it do it from the start.</p>
</div>
:::

===

@@
type: default
eyebrow: 05 · Principle 2
title: Don't *paste* keys into chat.
@@
:::html
<div class="grid-2 reveal">
  <div class="card">
    <div class="title" style="font-size: 19px;">Safe to share</div>
    <p>Your code, file names, the structure, error messages, and the <em>name</em> of a key (like <code>OPENAI_API_KEY</code>). The agent needs these to help.</p>
  </div>
  <div class="card">
    <div class="title" style="font-size: 19px;">Never share</div>
    <p>The actual value — the long secret string itself. The agent never needs the real key to wire it up; it only needs to know one exists.</p>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">Talk about the lock all you like. Don't read out the key.</p>
:::

===

@@
type: default
eyebrow: 06 · The difference
title: In the code vs. in *.env.*
@@
:::compare
[bad] secret hard-coded
[k]api_key[/k] = "sk-live-9f2a8c...real-key"

[c]# Commit this and the key is now
# in your history forever. Anyone
# with the repo has your key.[/c]
---
[good] secret read from the environment
[k]api_key[/k] = read_from_env("API_KEY")

[c]# The real value lives in .env,
# which Git ignores. The code is
# safe to share; the key is not in it.[/c]
:::

===

@@
type: default
eyebrow: 07 · If one leaks
title: Don't hide it — *rotate* it.
@@
:::html
<div class="grid-2 reveal">
  <p class="body">If a secret ends up somewhere public — a commit, a screenshot, a chat — deleting it isn't enough. Assume someone already has it. The only real fix is to make the old one useless.</p>
  <div class="loop-list">
    <div class="loop-step"><span class="n">1</span><div><span class="t">Revoke</span><span class="d">In the service's dashboard, cancel the leaked key.</span></div></div>
    <div class="loop-step"><span class="n">2</span><div><span class="t">Reissue</span><span class="d">Generate a fresh one to replace it.</span></div></div>
    <div class="loop-step"><span class="n">3</span><div><span class="t">Replace</span><span class="d">Put the new value in .env — never in the code.</span></div></div>
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">A revoked key is harmless. That's why rotating beats hiding, every time.</p>
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
A secret is anything that lets someone act as you or spend your money — guard it.
Secrets live in a gitignored .env file; the code reads them by name, never contains them.
Share code, names, and errors with the agent freely — never the actual key value.
If a secret leaks, revoke it and reissue — deleting it after the fact is never enough.
lede: A few habits, and your keys stay yours.
:::
