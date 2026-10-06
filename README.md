<div align="center">

# Eason

### Building reliable AI systems that can act, remember, recover, and be verified.

**Agent Systems · Reinforcement Learning · Embodied AI**

<sub>Evidence-first engineering for long-running agents, learning systems, and research infrastructure.</sub>

</div>

---

## What I build

I am interested in AI systems that keep working after the first impressive demo: systems with explicit state, recoverable execution, inspectable evidence, and honest failure boundaries.

- **Agent systems** — memory, runtime, verification, recovery, and human authority.
- **Reinforcement learning & robotics** — PPO, MuJoCo, hierarchical control, replay, and experiment reliability.
- **Research infrastructure** — grounded evidence, versioned knowledge, reproducible decisions, and auditable change.

## Currently building

| System | Current question |
| --- | --- |
| **[RL Sentinel](https://github.com/Anhao1314/RL-Sentinel)** | Can an RL experiment explain what was knowable at a decision point, replay it later, and keep future information out? |
| **[chat-distiller](https://github.com/Anhao1314/chat-distiller)** | How should long-running agents preserve decisions, version knowledge, detect staleness, and recover useful context? |
| **[Deep Native](https://github.com/Anhao1314/deep-native)** | Can coding agents be pushed toward evidence-first completion instead of declaring success before verification? |

## Selected systems

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ [RL Sentinel](https://github.com/Anhao1314/RL-Sentinel)

**Reliability layer for reinforcement-learning experiments.**

Chronological replay, time-gated inputs, recommendation evidence, failure analysis, and reproducible validation.

<code>Python</code> · <code>RL</code> · <code>Time Series</code> · <code>Experiment Reliability</code>

</td>
<td width="50%" valign="top">

### 🤖 [Go2W MoRA Navigation](https://github.com/Anhao1314/Go2w-MoRA-navigation)

**Hierarchical navigation for Unitree Go2W in MuJoCo.**

PPO, behavior cloning, DAgger, curriculum learning, ablations, and simulation-first evaluation with explicit experiment limits.

<code>PyTorch</code> · <code>MuJoCo</code> · <code>PPO</code> · <code>Robotics</code>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧠 [chat-distiller](https://github.com/Anhao1314/chat-distiller)

**Versioned memory and knowledge infrastructure for long-running agents.**

Turns retained decisions into cited knowledge pages, tracks revisions, detects stale inputs, and builds bounded recovery context.

<code>Python</code> · <code>Agent Memory</code> · <code>Knowledge Systems</code>

</td>
<td width="50%" valign="top">

### ⚙️ [Deep Native](https://github.com/Anhao1314/deep-native)

**Evidence-first coding workflow for DeepSeek in Claude Code.**

Inspection, checkpoints, verification contracts, stale-evidence rejection, and bounded delivery workflows. It does not pretend to upgrade the underlying model.

<code>Python</code> · <code>Coding Agents</code> · <code>Verification</code> · <code>Agent Skills</code>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔬 [FlowCredit Research](https://github.com/Anhao1314/flowcredit-research)

**Auditable research memory built around evidence and belief change.**

Versioned claims, grounded evidence, explicit relations, human review, and historical state instead of silent rewrites.

<code>JavaScript</code> · <code>Research Memory</code> · <code>Grounding</code>

</td>
<td width="50%" valign="top">

### ◈ [FlowCredit](https://github.com/Anhao1314/flowcredit)

**Evidence-aware risk intelligence infrastructure for AI-native systems.**

Deterministic risk signals, provenance-aware inputs, integrity vetoes, versioned APIs, and a strict boundary between model assistance and authoritative outputs.

<code>Node.js</code> · <code>API</code> · <code>Risk Systems</code> · <code>AI Agents</code>

</td>
</tr>
</table>

## The thread connecting the projects

<pre>
observe
  ↓
preserve state
  ↓
make a decision
  ↓
attach evidence
  ↓
verify / review
  ↓
recover and replay
</pre>

Different domains, same engineering question:

> **How do we make AI systems trustworthy across time, not only impressive in a single run?**

## Working principles

- **Evidence over claims.** A successful-looking output is not proof that the system worked.
- **Replay before trust.** Important decisions should be reconstructable from the information available at the time.
- **Abstention is valid behavior.** Uncertainty should stay visible instead of being converted into fake confidence.
- **History should not be silently rewritten.** Knowledge, claims, and execution state should evolve explicitly.
- **Human authority stays above automation.** Agents may propose, execute, and review; consequential acceptance remains explicit.

---

<div align="center">

<sub>Building systems, running experiments, keeping the receipts.</sub>

</div>
