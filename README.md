# Hi, I'm Anhao

### Algorithm Engineer · Reinforcement Learning · Robotics · AI Decision Systems

Building reproducible AI systems from experiments to engineering deployment.

<sub>AI Undergraduate · 2027 Graduate — research → experiments → engineering → reproducible evaluation.</sub>

---

## Featured Projects

### 1. [Unitree Go2W Hierarchical RL Navigation](https://github.com/Anhao1314/go2w-MoRA-navigation)

Hierarchical reinforcement learning for quadruped robot navigation in MuJoCo — high-level PPO over a scripted controller, with BC, DAgger and curriculum experiments.

`PPO` `Behavior Cloning` `DAgger` `Curriculum Learning` `MuJoCo`

- Curve **20/20**, multi-stage A→B **20/20**, junction routing **40/40**, **0 falls** across these archived runs.
- Includes ablation studies, failure→diagnosis analysis and a reproducible evaluation protocol.
- **196 passed / 1 skipped**, Pyright 0 errors (documented local run).
- Simulation-only (MuJoCo); branch selection and part of docking are scripted, final PPO weights require retraining.

### 2. [RL Training Risk Replay](https://github.com/Anhao1314/rl-training-risk-replay)

Experiment-infrastructure project: chronologically replay RL training runs, flag training risk and validate experiment-data quality before trusting a result.

`Chronological Replay` `Risk Analysis` `Data Quality` `Experiment Infra`

- Configurable **R0–R3** risk decisions (continue / watch / stop / tune / resize).
- **6 data-quality categories / 20+ checks**; cached-vs-direct pipeline equivalence tests.
- **265 tests passed** (documented local run); test gate runs on Linux CI.
- Analyzes robot-training logs — **not** market trading. Look-ahead isolation is unfinished and type-check debt is tracked openly in Limitations.

### 3. [FlowCredit](https://github.com/Anhao1314/flowcredit)

Risk-intelligence infrastructure for AI-native businesses and agents: **Evidence → Risk → Action**, with a deterministic risk engine behind a versioned API.

`Deterministic Risk Engine` `TAI / CCI` `Versioned API` `Docker` `AI Agents`

- Versioned deterministic **TAI (5 components)** and **CCI (5 dimensions)** plus confirmed-event integrity veto.
- Bearer-auth, bounded, idempotent versioned API; containerized with Docker.
- **67/67 tests passed** (documented local run); External Alpha.
- LLMs assist evidence extraction and explanation only — **deterministic rules own every authoritative score**.

---

## Agent & Product Tooling

### [Apple Product Design Skill](https://github.com/Anhao1314/Apple-skill)

An open-source Agent Skill for structured product definition, feature tradeoffs and technical decision review, inspired by public Apple product practices.

`Agent Skills` `Product Decision Systems` `Technical Review` `AI Tooling`

- Turns product ideas, PRDs and technical proposals into explicit **keep / merge / demote / remove / verify** decisions, with concrete alternatives instead of general "make it simpler" advice.
- Encodes a reusable workflow: **one-line product definition → simplification → end-to-end experience gaps → prototype validation**.
- Four documented modes — product review, product definition, methodology Q&A, technical proposal review — running on one model-agnostic layout: `SKILL.md`, five `references/`, a review checklist and output templates.
- Separates public product history from methodology inference, and labels assumptions and unverified claims instead of asserting them.

**Install** — `npx skills add Anhao1314/Apple-skill`

<sub>Independent project — not affiliated with or endorsed by Apple Inc. Validated through structure, reference and packaging checks; no client installation or Agent behavior test has been run yet.</sub>

---

## What I Can Deliver

- **Run the full experiment loop** — define baselines, ablations and controls, then read failure modes instead of only reporting the winning run (Go2W: BC-vs-init, DAgger and goal-conditioning ablations with explicit interpretation boundaries).
- **Build reproducible evaluation pipelines** — fixed protocols, archived reports and per-project validation records that state environment, scope and what was *not* proven.
- **Debug data and training-quality problems** — reward-drawdown / stagnation / restart risk items and six-category data-quality screening (RL Training Risk Replay).
- **Lock behavior with tests** — 196 passed / 1 skipped (Go2W), 265 passed (Risk Replay), 67/67 (FlowCredit), with honest accounting of skipped and advisory checks.
- **Take a prototype to a testable system** — versioned, schema-validated API, deterministic core, Docker packaging and documentation (FlowCredit), while keeping the LLM/rule boundary explicit.
- **Package a decision method as a reusable Agent Skill** — encode product and technical review into a repeatable workflow with explicit keep / merge / demote / remove decisions, evidence labels and reusable output templates (Apple Product Design Skill).

## Core Stack

`Python` `PyTorch` `MuJoCo` `Gymnasium` `Stable-Baselines3` `NumPy` `Pandas` `SciPy` `scikit-learn` `Linux` `Git` `Docker`

<sub>Also used in FlowCredit: JavaScript · Node.js · JSON Schema / Ajv.</sub>

---

## About

- Main thread across projects: **Algorithm Engineering · Reinforcement Learning · Robotics · Decision Systems · Experiment Infrastructure · Reproducible Engineering · Agent Tooling**.
- Seeking 2027 internship / new-grad roles in algorithm engineering, reinforcement learning, robotics or embodied-AI decision systems.
- I keep claim boundaries visible: simulation vs. real robot, post-hoc vs. predictive, deterministic vs. LLM — no result is presented as stronger than its evidence.

---

## Creator page

我的爱发电主页：[半页网页实验室](https://afdian.com/a/banyeweblab)。分享 AI 辅助制作并检查过的网页界面、前端源码和使用说明，具体功能与限制以作品说明为准。
