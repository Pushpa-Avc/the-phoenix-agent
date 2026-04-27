# The Phoenix Agent 🦅

> **The world's first autonomously evolving AI agent repository.**

The Phoenix Agent is a state-of-the-art AI agent designed to research, develop, and improve itself. Every day at 9:00 AM, this repository is updated by **Manus**, an autonomous AI agent, with the latest advancements in AI agentic workflows, tools, and research.

## 🌟 Vision
To push the boundaries of autonomous software development by creating a repository that is a living, breathing organism of code.

## 🛠 Architecture
The agent follows a modular, graph-based architecture:
- **`core/`**: Orchestration and state management.
- **`tools/`**: Extensible tool library for the agent.
- **`brain/`**: Memory and knowledge retrieval, now powered by an **LLM Wiki** pattern.
- **`evolution/`**: Logs and scripts for the daily self-improvement cycle, featuring **autonomous execution** with retry logic.

## 📅 Daily Evolution Cycle
1. **Research**: Scans for new AI papers and GitHub trends.
2. **Analyze**: Identifies optimization opportunities.
3. **Develop**: Implements new features or refactors code.
4. **Validate**: Ensures stability via automated tests.
5. **Push**: Updates the repository with the day's progress.

## ✨ New Capabilities

### LLM Wiki for Enhanced Memory
Inspired by Andrej Karpathy's LLM Wiki concept, the agent's memory system has been upgraded to a persistent, compounding knowledge base. Instead of simple JSON storage, the `brain/memory.py` now manages:
- A `knowledge/` directory containing:
    - `index.md`: A content-oriented catalog of all findings and decisions.
    - `log.md`: A chronological record of the agent's evolution steps.
    - `pages/`: Individual markdown files for specific concepts, research findings, and decisions.

This allows the agent to build upon its past experiences and knowledge, fostering a more sophisticated understanding and continuous learning.

### Robust Autonomous Execution
The `daily_evolution.py` orchestration has been enhanced to include more resilient autonomous execution logic:
- **Retry Mechanism**: Tool executions now include a retry mechanism (up to 3 attempts) to handle transient failures, improving overall stability.
- **State-Aware Reflection**: The reflection process now leverages the `knowledge/index.md` to gain a broader context of past activities and findings, leading to more informed improvement suggestions.

## 🚀 Getting Started
*Coming soon...*

---
*Maintained autonomously by [Manus](https://manus.im).*
