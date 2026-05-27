# Training Curriculum: The Agent-First Product Manager

This training is designed to transition Cambio teams from traditional product management to "Agent-First" execution. It focuses on the "Vibe Coding" methodology: describing behavior clearly and letting AI agents handle the technical implementation.

---

## Session 1: The Agentic Shift & The Vibe Mindset
**Objective:** Move from "Chatting with AI" to "Directing AI Agents."

### 1. Understanding the Agentic Shift
- **Concept:** Why agents are different from chat models. An agent doesn't just answer; it acts.
- **Reference:** `agent-presentation.html` (Understanding AI Agents)

### 2. The Vibe Coding Mindset
- **Concept:** Describing outcomes, not syntax. The loop of Describe -> Generate -> Run -> Refine.
- **Reference:** `src/content/01-what-is-vibe-coding.md`

### 3. Setting Up the Workspace
- **Action:** Installing and configuring VS Code and Antigravity. First prompt loops.
- **Reference:** `src/content/02-setting-up-the-tools.md`

---

## Session 2: The Craft of Specification
**Objective:** Master the art of defining products that agents can build flawlessly.

### 1. High-Resolution Prompting
- **Concept:** Specificity, context, and "showing what good looks like."
- **Reference:** `prompting-for-pms.html` (Prompting for PMs)

### 2. Functional Modelling & Edge Cases
- **Concept:** Using BDD (Given/When/Then) and mapping state transitions.
- **Reference:** `src/content/04-functional-modelling.md`

### 3. Adversarial Analysis (Brainstorm & Grill Me)
- **Action:** Using specialized agent skills to find logical holes and contradictions in your requirements before generating code.
- **Reference:** `Functional analysis .txt`

---

## Session 3: Building & Shipping with the Stack
**Objective:** Understand the architecture and safety nets of modern AI-driven development.

### 1. The Safety Net: Version Control
- **Concept:** Commits as save points. Fearless experimentation using branches.
- **Reference:** `src/content/03-version-control-basics.md`

### 2. The Vibe-Coded Stack
- **Concept:** Decoupling the UI (React), Logic (FastAPI), and Data (SQLite).
- **Reference:** `src/content/05-vibe-coded-stack.md`, `Vibe coded stack .txt`

### 3. Trust & Evaluation
- **Concept:** Evaluating the "trajectory" of an agent's work, not just the output. Handling agentic failure modes.
- **Reference:** `agentic-ai-for-pms.html` (Agentic AI for PMs)

---

## Final Project: The Vibe-Coded Knowledgebase
**Goal:** Build a functional, 3-tier internal tool using the standard Vibe Stack.

### Project Requirements
1. **Frontend (React):**
   - A list view of all articles.
   - A search bar that filters articles as you type.
   - A detailed view for reading a specific article (supporting Markdown).
2. **Backend (FastAPI):**
   - Secure endpoints to fetch all articles and search by keyword.
   - CORS enabled for local development.
3. **Database (SQLite):**
   - A table for `articles` with `id`, `title`, `content`, and `created_at`.

### The Architecture Prompt
> **Goal:** Build a simple Knowledgebase app.
>
> **Architecture:**
> - Frontend: React (using Tailwind for styling).
> - Backend: FastAPI (Python).
> - Database: SQLite.
>
> **Instructions:**
> 1. Create the SQLite schema for `articles` (id, title, content).
> 2. Write a FastAPI endpoint to fetch all articles. ENABLE CORS.
> 3. Write a React component that fetches and displays the list.
> 4. Give me the terminal commands to run both servers concurrently.
