# 🧠 AGENTS.md — Personal Productivity & Sports AI System

## 🎯 Project Overview

This project is a **Personal AI Agent System** designed to assist with:

* Daily planning (study, work, personal tasks)
* Sports scheduling (football, gym, recovery)
* Habit tracking
* Context-aware recommendations

The goal is to build a **real-world useful system**, not a demo.

---

## 👤 User Context

* 22 years old student and automation engineer
* Limited daily time (~1 hour/day)
* Lives with parents
* Interested in productivity, data, and AI systems
* Passionate about sports, especially football

---

## 🧱 System Vision

The system will evolve into a modular architecture with:

* LLM-based agents (LangChain / LangGraph)
* MCP (Model Context Protocol):

  * Local tools (Python)
  * External tools (APIs)
* Backend (FastAPI)
* Database (SQLite → PostgreSQL)
* Simple UI (Streamlit or React)
* Monitoring (LangSmith)
* Optional: RAG (later phase)

---

## 🤖 Agent Responsibilities

The main agent should:

1. Understand user intent
2. Decide which tools to use
3. Execute actions
4. Provide structured, useful responses

---

## 🧰 Available Tools (Planned)

### Local MCP Tools

* Task manager (CRUD tasks)
* Habit tracker
* Daily planner
* Training recommendation engine

### External MCP Tools

* Weather API
* Calendar API (Google Calendar, optional)

---

## ⚽ Domain Logic (Important)

The system must consider:

* Training should adapt to:

  * Available time
  * Fatigue
  * Schedule
* Balance between:

  * Study
  * Work
  * Physical activity

---

## 🗄️ Data Persistence

Initial:

* JSON or SQLite

Later:

* PostgreSQL

Data to store:

* Tasks
* Habits
* Daily plans
* Interaction history (for future RAG)

---

## 🔄 Development Philosophy

* Build incrementally
* Keep things simple first
* Avoid over-engineering early
* Each feature must be usable in real life

---

## 📅 Roadmap (High-Level)

1. Basic LLM script
2. Simple agent (planning assistant)
3. Add tools (task management, training)
4. Introduce MCP structure
5. Build LangGraph workflow
6. FastAPI backend
7. Simple frontend
8. Add persistence
9. Monitoring (LangSmith)
10. Optional: RAG

---

## 🧪 Constraints

* Max ~1 hour of development per day
* Prioritize clarity over complexity
* Prefer Python ecosystem
* Use Google AI Studio as LLM provider

---

## 🚫 What to Avoid

* Over-complicated architecture early
* Premature optimization
* Adding too many tools at once
* Building UI too early

---

## ✅ Success Criteria

* The system is used daily
* The agent provides real value
* The architecture is modular and extensible
* The developer understands every component

---

## 🧠 Future Extensions

* Advanced analytics (weekly performance)
* Smart notifications
* Integration with wearables
* Football performance tracking

---

