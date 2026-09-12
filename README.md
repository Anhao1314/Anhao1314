# Hi, I'm Anhao

**Algorithm Engineer focused on reinforcement learning, robotics, quantitative research, and AI-native decision systems.**

AI undergraduate focused on algorithm engineering. I enjoy building systems that connect:

**research → experiments → engineering → reproducible evaluation**

## Current Focus

- Reinforcement Learning & Embodied AI
- Robot Navigation & Hierarchical Decision Making
- Quantitative Research Infrastructure
- AI-native Risk Intelligence

## Featured Projects

### 1. [Unitree Go2W Hierarchical RL Navigation](https://github.com/Anhao1314/go2w-MoRA-navigation)

MoRA-inspired simulation research combining high-level PPO with scripted control and rule-based decisions, supported by BC, DAgger and curriculum experiments.

- Curve navigation: **20/20 success**, 0 falls.
- 10 m-class multi-stage navigation: **20/20 success**, A-stop 100%, mean time 15.2 s.
- Junction routing: **40/40 success**, correct branch 100%, 0 falls.
- Quality: **197 tests discovered, 196 passed, 1 skipped; Pyright 0 errors** in the documented local run.

Recorded task-specific simulation results for the full system; branch choice and parts of docking are scripted. Final PPO weights require retraining. [Reports and limitations](https://github.com/Anhao1314/go2w-MoRA-navigation#demo--key-results).

**Stack:** Python · PyTorch · MuJoCo · Gymnasium · Stable-Baselines3 · NumPy

### 2. [FlowCredit](https://github.com/Anhao1314/flowcredit)

Evidence-aware risk intelligence infrastructure for AI-native businesses and agents: **Evidence → Risk → Action**.

- **67/67 tests passed** in the documented local verification run.
- **5 TAI components and 5 CCI dimensions**, computed by versioned deterministic rules.
- **6 modeled evidence source domains and 3 confirmed-event veto codes**; live external connectors remain future work.

LLMs assist extraction or explanation; deterministic rules own authoritative risk outputs. External Alpha; no calibrated lending or Finch publication claim. [Verification and methodology](https://github.com/Anhao1314/flowcredit#key-results).

**Stack:** JavaScript · Node.js · JSON Schema / Ajv · Docker

### 3. [RL Training Risk Replay & Quantitative Analysis](https://github.com/Anhao1314/go2_lianghua)

Quantitative algorithm engineering for robot-training experiments: chronological replay, configurable risk decisions and time-series data validation.

- **265 tests passed** in the documented local verification run.
- **4 risk levels (R0–R3)** and **6 data-quality categories / 20+ checks**.
- **3 built-in replay predictors**, with deterministic fixture validation and cached/direct pipeline equivalence tests.

Partial temporal filtering; final metadata isolation remains incomplete. Full Pyright has unresolved findings. This analyzes training runs, not market trading or investment returns. [Validation and limitations](https://github.com/Anhao1314/go2_lianghua/blob/main/docs/portfolio-validation.md).

**Stack:** Python · pandas · NumPy · SciPy · scikit-learn · TensorBoard

## Core Skills

Python · PyTorch · MuJoCo · Gymnasium · Stable-Baselines3 · NumPy · Pandas · Docker · Git · Linux

Additional project stack: JavaScript · Node.js · JSON Schema
