<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/profile-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/profile-light.svg">
    <img alt="Eason — Life finds a way. AI and complex systems." src="assets/profile-light.svg" width="100%">
  </picture>
</p>

# Eason

[中文](README.md) · [English](README.en.md) · [Visual home](https://anhao1314.github.io)

Independent researcher on **AI and complex systems**: how systems study, decide, act — and answer for their conclusions.

> **Life finds a way.** 生命会自己寻求出路。

**Working hypothesis**　People define the problems worth solving, AI explores the paths, real evidence decides what survives. Charter: [life-finds-a-way](https://github.com/Anhao1314/life-finds-a-way).

**Core question**　How to make a complex system's conclusions reliable, auditable and unable to masquerade as present state.

> Simulation passing ≠ reality working　·　Retrieval hit ≠ claim current　·　AI output ≠ trusted evidence

---

## Projects · REPOS

No shared architecture — one set of questions: what deserves trust, how far an agent may go alone, how a system proves a task done, and how simulation success becomes capability.

### Evidence-native AI and agent runtimes

| Repo | One line | Status |
| --- | --- | --- |
| [ClaimLedger](https://github.com/Anhao1314/ClaimLedger) | Decision ledger for AI agents: status-aware claims; stale conclusions never pass as present | active |
| [FCode](https://github.com/Anhao1314/FCode) | Host-governed agent runtime: the model only proposes; every event lands on a hash chain | experiment |
| [lastgreen](https://github.com/Anhao1314/lastgreen) | Completion verifier for coding agents: "done" requires evidence from the last green state | experiment |

### Embodied intelligence

| Repo | One line | Status |
| --- | --- | --- |
| [go2w-locomotion](https://github.com/Anhao1314/go2w-locomotion) | Go2W wheeled navigation (MuJoCo) archived;<br>Go2 joint-level RL (Isaac Lab) passed three seeds, artifacts unpublished | active |
| [g1-jev-swarm-lab](https://github.com/Anhao1314/g1-jev-swarm-lab) | Single-G1 testbed (MuJoCo): task graphs, strict judging;<br>failures block dependents, physical halt opt-in | experiment |
| [RL-Sentinel](https://github.com/Anhao1314/RL-Sentinel) | Risk replay for RL training: failures, metrics and decisions remain re-checkable, misses included | tool |

### AI-native financial intelligence

| Repo | One line | Status |
| --- | --- | --- |
| [flowcredit](https://github.com/Anhao1314/flowcredit) | Risk intelligence API: deterministic rules carry conclusions,<br>extraction consent-gated, PD and expected loss null | maintenance |
| [flowcredit-research](https://github.com/Anhao1314/flowcredit-research) | Investment-research memory: claims traceable, revisions recorded,<br>model holds no authority; blind test failed | experiment |

---

## Main line: ClaimLedger · LEDGER

[![Tests](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml/badge.svg)](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml)　[v0.10.0](https://github.com/Anhao1314/ClaimLedger/releases/latest) · macOS / Linux · stdlib only, zero dependencies

Memory failure in long-running work is not bad retrieval: expired conclusions served as current, conflicts merged silently at read time, disputes unadjudicated. ClaimLedger structures memory as **claim + status + provenance**. Conflicting writes require an explicit supersession or dispute; `--at` rebuilds the ledger at any instant.

| Stale hits @5 | Recall @5 | Engineering check |
| :---: | :---: | :---: |
| **54% → 0** | **1.00 → 0.92** | **421 tests** |

Both numbers are in the [benchmark report](https://github.com/Anhao1314/ClaimLedger/blob/main/benchmarks/benchmark-results.md). Refusals count too: no vector DB, auto capture, daemon or cloud sync.

**Remaining limits**　Synthetic benchmark (40 sessions, 24 queries), retrieval only; Recall@5 falls to 0.50 on conflict queries, expired-target recall unmeasured. It governs status and provenance, not truth — no general solution to AI memory, agent reliability or fact-checking.

---

## Engineering charter · CHARTER

- **Goals before routes.** Say why and how far before choosing how; industry default is no reason.
- **Exploration has boundaries.** Freedom to pick methods is not new permissions, budgets or release authority.
- **Failure is evidence.** Results that don't reproduce, don't pass or lack evidence stay archived as they are.

---

## Limits, not hidden behind slogans · LIMITS

- These are personal research systems, not production systems;
- lastgreen's v0.1 pilot was negative (0 wins, 1 loss, 9 ties in 10 pairs); its 12-run v0.2 ablation has not run: early comparisons have not yet proven quality improvement;
- flowcredit's risk conclusions are not a calibrated credit rating;
- go2w and g1 results are all in simulation, no domain randomization or hardware validation: simulation results are not hardware reliability.

---

## Verification · VERIFY

CI checks this page via [test_profile.py](tests/test_profile.py): link set and status vocabulary cover both files; section order, identity phrases and limit statements are asserted on the Chinese page. Structure and presence, not truth: green is not proof.

---

## Now · NOW

- **Working**　ClaimLedger v2 dispute closure, bitemporal claims and dependency backtracking are on main, unreleased; Phase B and storage merge: design only.
- **Not yet**　Domain randomization and sim-to-real validation for go2w; long-horizon g1 missions remain a goal, not a result.
- **Habit**　Small tools and creative coding keep the trial-and-error instinct — never in formal repos.
