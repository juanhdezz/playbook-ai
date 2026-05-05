# ⚽ Playbook AI — Personal Agent System for Productivity & Training

## 🧠 Overview

**Playbook AI** is a personal AI agent system designed to help manage daily life, combining:

* 📅 Task planning (study, work, personal)
* ⚽ Sports scheduling (football, gym, recovery)
* 📊 Habit tracking
* 🤖 Intelligent decision-making using AI agents

This is not a demo project — it is built to be **used daily in real life**.

---

## 🎯 Goals

* Build a **modular AI agent system** using modern tools
* Learn and apply:

  * Agent orchestration (LangChain / LangGraph)
  * MCP (Model Context Protocol)
  * Prompt engineering & observability (LangSmith)
* Create a system that:

  * Understands context
  * Takes decisions
  * Uses tools
  * Evolves over time

---

## 🏗️ Architecture (Planned)

```
User (UI)
   ↓
FastAPI Backend
   ↓
LangGraph Agent System
   ↓
-------------------------
|       MCP Layer        |
|------------------------|
| Local Tools (Python)   |
| External APIs          |
-------------------------
   ↓
Database (SQLite → PostgreSQL)
```

---

## 🤖 Core Features

### 1. Daily Planning Agent

* Generates a structured plan for the day
* Balances:

  * Work
  * Study
  * Training

### 2. Training Recommendation Engine ⚽

* Suggests workouts based on:

  * Available time
  * Fatigue
  * Schedule

### 3. Task Management System

* Add, update, and track tasks
* Persistent storage

### 4. Habit Tracking

* Monitor consistency over time

### 5. Context-Aware Responses

* Answers questions like:

  * “What should I do today?”
  * “When should I train this week?”
  * “Am I being consistent?”

---

## 🧰 Tech Stack

### AI & Agents

* LLM: Google AI Studio (Gemini)
* LangChain
* LangGraph (for orchestration)

### Backend

* FastAPI

### MCP (Model Context Protocol)

* Local tools (Python)
* External APIs (weather, calendar, etc.)

### Data

* SQLite (initial)
* PostgreSQL (later)

### Observability

* LangSmith

### Frontend

* Streamlit (initial)
* React (optional later)

---

## 📁 Project Structure

```
playbook-ai/
│
├── AGENTS.md              # Agent instructions & system context
├── README.md
│
├── app/
│   ├── main.py            # Entry point
│   │
│   ├── agents/            # Agent definitions
│   ├── tools/             # Tools (functions the agent can use)
│   ├── mcp/               # MCP abstraction layer
│   ├── core/              # Core logic
│
├── data/                  # Local storage (JSON / SQLite)
└── tests/
```

---

## 🚀 Roadmap

### Phase 0 — Setup

* Basic LLM call (Google AI Studio)

### Phase 1 — Simple Agent

* Daily planning assistant

### Phase 2 — Tools

* Task manager
* Training recommendation
* Weather API

### Phase 3 — MCP Layer

* Separate local and external tools

### Phase 4 — LangGraph

* Multi-step agent workflow

### Phase 5 — Backend

* FastAPI endpoints

### Phase 6 — Frontend

* Simple UI (Streamlit)

### Phase 7 — Persistence

* SQLite → PostgreSQL

### Phase 8 — Observability

* LangSmith integration

### Phase 9 — (Optional)

* RAG (history + embeddings)

---

## 🧪 Development Philosophy

* Build **step by step**
* Keep things **simple first**
* Avoid over-engineering
* Every feature must be:

  * usable
  * testable
  * meaningful

---

## 👤 Author

Juan

* Double degree in Computer Engineering + Business (UGR)
* Interested in Data, AI systems, and real-world applications
* Passionate about sports and continuous learning

---

## 📌 Status

🟡 In development — building incrementally

---

## 💡 Future Ideas

* Weekly performance analytics
* Smart notifications
* Integration with wearables
* Football performance tracking

---

## 🧠 Why this project matters

This project demonstrates:

* Ability to design AI systems (not just scripts)
* Understanding of agent architectures
* Integration of tools and real-world data
* Focus on usability and real impact

---

