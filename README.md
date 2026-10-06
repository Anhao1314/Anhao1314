<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/profile-hero-v4-dark.svg">
  <img src="assets/profile-hero-v4-light.svg" alt="A13 / Eason — Build systems. Break assumptions. Keep the evidence." width="100%">
</picture>

<br>

<div align="center">

**Reliable AI systems for long-running agents, learning loops, and research work.**

<sub>I like systems that can explain themselves after something goes wrong.</sub>

</div>

---

## Focus

<table>
<tr>
<td width="33%" valign="top">

<sub>AGENT SYSTEMS</sub>

### Memory / Runtime / Recovery

Long-running agents with explicit state, bounded execution, verification, and human authority.

</td>
<td width="33%" valign="top">

<sub>RL / ROBOTICS</sub>

### Policy / Replay / Control

PPO, MuJoCo, hierarchical navigation, experiment reliability, and failure analysis.

</td>
<td width="33%" valign="top">

<sub>RESEARCH INFRA</sub>

### Grounding / Evidence / Change

Versioned knowledge, inspectable evidence, belief revision, and reproducible decisions.

</td>
</tr>
</table>

## Now

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/runtime-now-v4-dark.svg">
  <img src="assets/runtime-now-v4-light.svg" alt="Current live workstreams: RL Sentinel and chat-distiller active, Deep Native v0.2 in experiment." width="100%">
</picture>

## Selected systems

<table>
<tr>
<td width="62%" valign="top">

<sub>01 / FLAGSHIP / RELIABILITY</sub>

## [RL Sentinel ↗](https://github.com/Anhao1314/RL-Sentinel)

**Replay what the system knew, not what we know later.**

A reliability layer for reinforcement-learning experiments: chronological replay, time-gated inputs, evidence bundles, failure analysis, and explicit limits.

<sub>PYTHON / RL / REPLAY / EXPERIMENT RELIABILITY</sub>

</td>
<td width="38%" valign="top">

<sub>02 / EMBODIED RL</sub>

### [Go2W MoRA ↗](https://github.com/Anhao1314/Go2w-MoRA-navigation)

Hierarchical navigation for Unitree Go2W in MuJoCo.

<sub>PYTORCH / MUJOCO / PPO</sub>

</td>
</tr>
<tr>
<td width="38%" valign="top">

<sub>03 / MEMORY</sub>

### [chat-distiller ↗](https://github.com/Anhao1314/chat-distiller)

Versioned memory, stale detection, and recovery context for long-running agents.

<sub>PYTHON / MEMORY / RECOVERY</sub>

</td>
<td width="62%" valign="top">

<sub>04 / FLAGSHIP / VERIFICATION</sub>

## [Deep Native ↗](https://github.com/Anhao1314/deep-native)

**Make coding agents prove they're done.**

Evidence-first execution for coding agents, now exploring adaptive FAST / STANDARD / DEEP escalation without hiding verification failure.

<sub>CLAUDE CODE / DEEPSEEK / VERIFICATION / ADAPTIVE RUNTIME</sub>

</td>
</tr>
<tr>
<td width="56%" valign="top">

<sub>05 / RESEARCH MEMORY</sub>

### [FlowCredit Research ↗](https://github.com/Anhao1314/flowcredit-research)

Grounded evidence, versioned claims, explicit relations, and human-reviewed belief change.

<sub>EVIDENCE / CLAIMS / GROUNDING</sub>

</td>
<td width="44%" valign="top">

<sub>06 / DECISION INFRA</sub>

### [FlowCredit ↗](https://github.com/Anhao1314/flowcredit)

Evidence-aware risk infrastructure for AI-native systems.

<sub>NODE.JS / RISK / AGENTS</sub>

</td>
</tr>
</table>

## Recent signals

**2026.10.06 · [FlowCredit Research](https://github.com/Anhao1314/flowcredit-research)**  
<code>SAFETY / AUDIT</code> — hardened v0.2C S1 safety-audit integrity without changing runtime, benchmark labels, or thresholds.

**2026.10.06 · [Deep Native](https://github.com/Anhao1314/deep-native)**  
<code>EXPERIMENT / V0.2</code> — added an adaptive runtime candidate with FAST / STANDARD / DEEP escalation and held-out ablation planning.

**2026.10.06 · [chat-distiller](https://github.com/Anhao1314/chat-distiller)**  
<code>MEMORY / V0.4</code> — added Context Gateway 0.4 for a lower-friction connect → sync → context → status path.

**2026.10.06 · [RL Sentinel](https://github.com/Anhao1314/RL-Sentinel)**  
<code>RELIABILITY / DOCS</code> — refined the project identity and reading experience while preserving runtime APIs and historical evidence.

## The thread

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/system-loop-dark.svg">
  <img src="assets/system-loop-light.svg" alt="Observe, remember, decide, verify and recover form a continuous trust-across-time loop." width="100%">
</picture>

<div align="center">

### Trust is not a model output. It is a system property you have to keep earning.

</div>

## Principles

<table>
<tr>
<td width="33%" valign="top">

<sub>01 / EVIDENCE</sub>

**Evidence over claims.**

A successful-looking output is not proof.

</td>
<td width="33%" valign="top">

<sub>02 / REPLAY</sub>

**Replay before trust.**

Important decisions should survive reconstruction.

</td>
<td width="33%" valign="top">

<sub>03 / AUTHORITY</sub>

**Human authority above automation.**

Agents can propose and execute. Acceptance stays explicit.

</td>
</tr>
</table>

---

<div align="center">

<sub>A13 / BUILD · BREAK · VERIFY · REPEAT</sub>

</div>
