# Autonomous Job Application AI System 

This repository contains the official Capstone Project submission for the **Kaggle 5-Day AI Agents: Intensive Vibe Coding Course with Google**.

##  Project Overview
Finding, filtering, and writing customized cover letters for hundreds of job openings is a highly exhausting and repetitive task. The **Autonomous Job Application Agent** solves this by leveraging a collaborative, multi-agent framework that scans positions, scores candidate alignment, and automatically generates custom-tailored professional application assets.

---

## Architecture & Core Components
The system is orchestrated using three specialized autonomous classes that seamlessly transfer context and execution states:

1. **Job Hunter Agent (`JobHunterAgent`):** Interacts with discovery tools to filter relevant open roles based on core keywords.
2. **Matchmaker Agent (`MatchmakerAgent`):** Evaluates CV match metrics against complex job descriptions to guarantee high-quality alignment.
3. **Applier Agent (`ApplierAgent`):** Programmatically crafts contextual, human-centric Cover Letters for approved matches.

---

## Implemented Kaggle Evaluation Requirements
This architecture checks the required core course concepts directly in the implementation code:
* **Multi-Agent Orchestration:** Decentralized logic split into distinct communicative worker agents.
* **Agent Skills / Tools:** Specialized external interfaces (`mock_job_scraper` and `read_user_resume`) for processing data streams.
* **Built-in Security Features:** Full separation of target configurations utilizing strict environment runtime calls (`os.getenv`), preventing hardcoded credential leaks.

---

##  Quick Start Guide

### 1. Set Up Environment Variables
Keep your runtime safe. Create a `.env` file or export your Gemini token directly via terminal:
```bash
export GEMINI_API_KEY="your_actual_api_key_here"
