@@
type: title
eyebrow: A working introduction · chapter five
title: The Vibe-Coded|*Stack.*
@@
How an AI assembles the pieces of a real app —|a React front end, a FastAPI back end, and SQLite.

===

@@
type: default
eyebrow: 01 · Why this matters
title: From single scripts to *actual apps.*
@@
:::html
<div class="grid-2 reveal" style="margin-top: var(--space-md);">
  <div class="stack">
    <p class="body">"Vibe coding" started as generating single-file scripts. But real products need a screen people can use, a place to store data, and some logic connecting the two.</p>
    <p class="body subtext">This chapter is a little more technical than the others — but you still won't write the code. You just need to recognise the parts, so you can point the agent at the right one.</p>
  </div>
  <div class="card">
    <div class="label">The Monolith Myth</div>
    <div class="title">"Just put it in one file"</div>
    <p>Works for a 5-minute prototype. Fails when you need a real UI, secure API keys, and persistent data.</p>
    <div class="label" style="margin-top: 20px;">The Vibe Stack</div>
    <div class="title">Separation of Concerns</div>
    <p>A decoupled UI, an API backend, and a simple database. The sweet spot between prototype and enterprise.</p>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 02 · The scenario
title: Building a *Knowledgebase.*
@@
:::html
<div class="grid-2 reveal">
  <p class="body">To anchor this, let's look at a classic internal tool: a simple knowledgebase. Users need to read articles, search for topics, and authors need to write them.</p>
  <div class="prompt-block good">
<span class="tag">requirements</span>
<span class="h">Core Features</span>1. View a list of articles.
2. Read a specific article.
3. Search by title or keyword.

<span class="h">The Problem</span>If this is just an HTML file,
where do the articles live?
How do you update them?
How do you search across them
without loading everything at once?
  </div>
</div>
<p class="lede reveal" style="margin-top: var(--space-lg);">You need a frontend to display it, a backend to search it, and a database to store it.</p>
:::

===

@@
type: default
eyebrow: 03 · Architecture anatomy
title: Three layers of a modern Vibe App.
@@
:::anatomy
- React | The front end (what users see) | Runs in the user's browser. Fetches data, displays buttons, handles clicks.
- middle: FastAPI | The back end (the API) | Runs on a server. Holds secret keys, talks to AI models, processes data safely.
- bottom: SQLite | The database (the data) | Stores the actual articles. A simple file on the server.
lede: AI knows this stack well. Ask for a "React, FastAPI, SQLite stack" and it knows exactly how to wire the parts together.
:::

===

@@
type: default
eyebrow: Layer 1
title: The front end: *React.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Why React? Because AI models have seen millions of React examples, so they produce tidy, good-looking screens reliably. (Node is just the tooling that runs it.)</p>
    <p class="body subtext">The front end's only job is to look good and ask the back end for data. It should hold <em>no</em> business logic and never touch the database directly.</p>
  </div>
  <div class="card">
    <div class="label">For the Knowledgebase</div>
    <div class="title">Visuals &amp; State</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>Search bar component</li>
      <li>Article list view</li>
      <li>Markdown rendering</li>
      <li class="muted">Loading spinners while fetching</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Layer 2
title: The Backend: *FastAPI.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Why FastAPI (Python)? Because Python is the main language of AI. If you want to add smarter AI features later, the tools you'll need are already in Python.</p>
    <p class="body subtext">FastAPI is light, fast, and documents itself automatically — which also helps the agent understand the API it just wrote.</p>
  </div>
  <div class="card">
    <div class="label">For the Knowledgebase</div>
    <div class="title">Endpoints &amp; Logic</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li><span style="font-family: var(--font-code); font-size: 13px;">GET /articles</span></li>
      <li><span style="font-family: var(--font-code); font-size: 13px;">GET /articles/{id}</span></li>
      <li><span style="font-family: var(--font-code); font-size: 13px;">GET /search?q=query</span></li>
      <li class="muted">Connecting to SQLite safely</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: Layer 3
title: The Database: *SQLite.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack">
    <p class="body">Why SQLite? Because you don't need a massive Postgres cluster to test an idea. SQLite is a database contained entirely within a single local file (<span style="font-family: var(--font-code);">app.db</span>).</p>
    <p class="body subtext">It requires zero setup, zero passwords, and zero network configuration. It is the ultimate database for vibe-coding a V1.</p>
  </div>
  <div class="card">
    <div class="label">For the Knowledgebase</div>
    <div class="title">Persistent Storage</div>
    <ul class="dotlist" style="margin-top: 8px;">
      <li>A table for `articles`</li>
      <li>Columns for `title`, `content`, `date`</li>
      <li>Retains data when the server restarts</li>
      <li class="muted">Easy to backup (just copy the file)</li>
    </ul>
  </div>
</div>
:::

===

@@
type: default
eyebrow: 04 · Pitfalls
title: Where the vibe *breaks.*
@@
:::html
<div class="grid-2 reveal">
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">CORS errors</div>
      <p>A very common snag. The React front end tries to call FastAPI on a different port, and the browser blocks it. Just tell the agent: "Configure CORS on the FastAPI app."</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">Premature optimisation</div>
      <p>Asking the AI for heavy infrastructure on day one. Start with SQLite. Upgrade only when something actually breaks.</p>
    </div>
  </div>
  <div class="stack-sm">
    <div class="card">
      <div class="title" style="font-size: 19px;">Secret leaks</div>
      <p>Putting API keys in the React code. The frontend runs on the user's machine. Keys go in the FastAPI backend only.</p>
    </div>
    <div class="card">
      <div class="title" style="font-size: 19px;">Database Locks</div>
      <p>SQLite doesn't love 10,000 users writing at the same exact millisecond. It's fine for reading and typical MVP traffic.</p>
    </div>
  </div>
</div>
:::

===

@@
type: example
eyebrow: Worked example · 01 of 04
title: The *Memory* (SQLite).
@@
:::example
lead:
### Setting up the schema.
The foundation of the app. You tell the agent what data you need to store, and it writes the SQL to structure that single `.db` file.
Notice how simple it is. No external services required.
tags: Database, Schema, Local File
---
tag: database.py
[c]# Generated by AI for the backend[/c]
[k]import[/k] sqlite3

[k]def[/k] init_db():
    conn = sqlite3.connect([arg]'kb.db'[/arg])
    c = conn.cursor()
    
    [c]# Create the articles table[/c]
    c.execute([arg]'''[/arg]
[arg]        CREATE TABLE IF NOT EXISTS articles ([/arg]
[arg]            id INTEGER PRIMARY KEY AUTOINCREMENT,[/arg]
[arg]            title TEXT NOT NULL,[/arg]
[arg]            content TEXT NOT NULL,[/arg]
[arg]            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP[/arg]
[arg]        )[/arg]
    [arg]'''[/arg])
    conn.commit()
    conn.close()
:::

===

@@
type: example
eyebrow: Worked example · 02 of 04
title: The *Brain* (FastAPI).
@@
:::example
lead:
### Exposing the data securely.
The backend acts as a bouncer. It receives a request from the frontend, securely reads from the SQLite database, and returns clean JSON.
FastAPI makes routing incredibly semantic and easy to read.
tags: Backend, Python, JSON API
---
tag: main.py
[k]from[/k] fastapi [k]import[/k] FastAPI
[k]import[/k] sqlite3

app = FastAPI()

[c]# The Endpoint[/c]
[arr]@app.get[/arr]([arg]"/api/articles"[/arg])
[k]def[/k] get_articles():
    conn = sqlite3.connect([arg]'kb.db'[/arg])
    c = conn.cursor()
    
    [c]# Query the database[/c]
    c.execute([arg]"SELECT id, title FROM articles"[/arg])
    articles = c.fetchall()
    conn.close()
    
    [c]# Return JSON to the frontend[/c]
    [k]return[/k] [{[arg]"id"[/arg]: row[0], [arg]"title"[/arg]: row[1]} [k]for[/k] row [k]in[/k] articles]
:::

===

@@
type: example
eyebrow: Worked example · 03 of 04
title: The *Face* (React).
@@
:::example
lead:
### Fetching and displaying.
The UI doesn't know how the database works. It just calls the API URL, waits for the JSON, and paints the screen.
This decoupling means you can change the DB later without rewriting the UI.
tags: Frontend, React, Fetch
---
tag: App.jsx
[k]import[/k] { useState, useEffect } [k]from[/k] [arg]'react'[/arg];

[k]export default function[/k] KnowledgeBase() {
  [k]const[/k] [articles, setArticles] = useState([]);

  useEffect(() [arr]=>[/arr] {
    [c]// Call the FastAPI backend[/c]
    [k]fetch[/k]([arg]'http://localhost:8000/api/articles'[/arg])
      .then(res [arr]=>[/arr] res.json())
      .then(data [arr]=>[/arr] setArticles(data));
  }, []);

  [k]return[/k] (
    [arr]<div className="p-8">[/arr]
      [arr]<h1 className="text-2xl font-bold">[/arr]KB Articles[arr]</h1>[/arr]
      [arr]<ul>[/arr]
        {articles.map(article [arr]=>[/arr] (
          [arr]<li key=[/arr]{article.id}[arr]>[/arr]{article.title}[arr]</li>[/arr]
        ))}
      [arr]</ul>[/arr]
    [arr]</div>[/arr]
  );
}
:::

===

@@
type: example
eyebrow: Worked example · 04 of 04
title: The *Architecture Prompt.*
@@
:::example
lead:
### Telling the agent how to build it.
When you sit down with your agent (in VS Code or Antigravity), you don't ask it to "build an app."
You spell out the stack, so it wires the pieces together correctly from step one.
tags: System Prompt, Context, Architecture
---
tag: vibe prompt
[h]Goal[/h]Build a simple Knowledgebase app.

[h]Architecture[/h]- [k]Frontend:[/k] React (using Tailwind for styling).
- [k]Backend:[/k] FastAPI (Python).
- [k]Database:[/k] SQLite.

[h]Instructions[/h]1. Create the SQLite schema for `articles`
   (id, title, content).
2. Write a FastAPI endpoint to fetch all
   articles. ENABLE CORS so the frontend
   can access it locally.
3. Write a React component that fetches
   and displays the list.
4. Give me the terminal commands to run
   both servers concurrently.
:::

===

@@
type: takeaways
eyebrow: In closing
title: Four things to *remember.*
@@
:::takeaways
A real app separates the UI (React), logic (FastAPI), and data (SQLite).
FastAPI is the bridge. It connects the frontend to the AI ecosystem.
Start with SQLite. Don't let the agent over-engineer your MVP database.
Specify the architecture in your prompt so the AI wires it up correctly.
lede: Decoupled systems. Fast execution.
:::
