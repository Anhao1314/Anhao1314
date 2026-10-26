# Eason

[中文](README.md) · [English](README.en.md)

Independent researcher on AI and complex systems: how systems study, decide, act — and answer for their conclusions.

> Life finds a way. 生命会自己寻求出路。

**Working hypothesis:** People define the problems worth solving, AI explores the paths, real evidence decides what survives. Charter: [life-finds-a-way](https://github.com/Anhao1314/life-finds-a-way).

**Core question:** How to make a complex system's conclusions reliable, auditable and unable to masquerade as present state.

Simulation passing ≠ reality working; retrieval hit ≠ claim current; AI output ≠ trusted evidence.

## Projects

No shared architecture — one set of questions: what deserves trust, how far an agent may go alone, how a system proves a task done, how simulation success becomes capability, and what evidence and limits survive once AI joins a decision.

### Evidence-native AI and agent runtimes

| Repo | One line | Status |
| --- | --- | --- |
| [ClaimLedger](https://github.com/Anhao1314/ClaimLedger) | Decision ledger for AI agents: status-aware claims; stale conclusions never pass as present | active |
| [FCode](https://github.com/Anhao1314/FCode) | Host-governed agent runtime: the model only proposes; every event lands on a hash chain | experiment |
| [lastgreen](https://github.com/Anhao1314/lastgreen) | Completion verifier for coding agents: "done" requires evidence from the last green state | experiment |

### Embodied intelligence

| Repo | One line | Status |
| --- | --- | --- |
| [go2w-locomotion](https://github.com/Anhao1314/go2w-locomotion) | Go2W wheeled navigation (MuJoCo) archived; Go2 joint-level RL (Isaac Lab) passed three seeds, artifacts unpublished | active |
| [g1-jev-swarm-lab](https://github.com/Anhao1314/g1-jev-swarm-lab) | Single-G1 testbed (MuJoCo): task graphs, strict judging; failures block dependents, physical halt opt-in | experiment |
| [RL-Sentinel](https://github.com/Anhao1314/RL-Sentinel) | Risk replay for RL training: failures, metrics, the moment's decisions, re-checkable — misses included | tool |

### AI-native financial intelligence

| Repo | One line | Status |
| --- | --- | --- |
| [flowcredit](https://github.com/Anhao1314/flowcredit) | Risk intelligence API: deterministic rules carry conclusions, extraction consent-gated, PD and expected loss null | maintenance |
| [flowcredit-research](https://github.com/Anhao1314/flowcredit-research) | Investment-research memory: claims traceable, revisions recorded, model holds no authority; blind test failed | experiment |

## Main line: ClaimLedger

![Tests](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml/badge.svg) [v0.10.0](https://github.com/Anhao1314/ClaimLedger/releases/latest), 421 tests, macOS/Linux CI, stdlib only, zero dependencies.

### Question

Memory failure in long-running work is not bad retrieval. Three failures: expired conclusions served as current, conflicts merged silently at read time, disputes unadjudicated.

### Mechanism

A claim: statement + status (current / superseded / disputed) + provenance. Conflicting writes are refused: supersede or dispute. Briefs obey a hard byte budget: usage and omissions are checkable. `--at` rebuilds the ledger at any instant. Refusals count as much as the roadmap: no vector DB, no auto capture, no daemon, no cloud.

### Result

Against raw transcripts, status filtering pushes stale hits (@5) from 54% to 0; the cost: Recall@5 falls from 1.00 (structured memory) to 0.92 — both in the [benchmark report](https://github.com/Anhao1314/ClaimLedger/blob/main/benchmarks/benchmark-results.md).

### Remaining limits

Synthetic benchmark (40 sessions, 24 queries), retrieval-only: on conflict queries Recall@5 drops from 1.00 to 0.50; expired-target recall unmeasured. Conflict matching surfaces suspicions, never adjudicates semantics. It governs status and provenance, not truth — no general solution to AI memory, agent reliability or fact-checking.

## Engineering charter

- **Goals before routes.** Say why and how far before choosing how; industry default is no reason.
- **Exploration has boundaries.** Freedom to pick methods is not new permissions, budgets or release authority.
- **Failure is evidence.** Results that don't reproduce, don't pass or lack evidence stay archived as they are.

## Limits, not hidden behind slogans

- These are personal research systems, not production systems;
- lastgreen's v0.1 pilot was negative (0 wins, 1 loss, 9 ties in 10 pairs); its 12-run v0.2 ablation has not run: early comparisons have not yet proven quality improvement;
- flowcredit's risk conclusions are not a calibrated credit rating;
- go2w and g1 results are all in simulation, no domain randomization or hardware validation: simulation results are not hardware reliability.

## Verification

CI checks this page with [test_profile.py](tests/test_profile.py): link set and status vocabulary cover both files; section order, identity phrases and limit statements are asserted on the Chinese page; forbidden vocabulary and the byte ceiling live in the checker. Structure and presence, not truth: a green check is not proof.

## Now

- Working: ClaimLedger v2 (dispute closure, bitemporal claims, dependency backtracking) is on main, unreleased (v0.10.0 predates it); Phase B and the storage merge: design only.
- Not yet: domain randomization and sim-to-real validation for go2w; long-horizon g1 missions: goal, not result.
- Habit: small tools and creative coding keep the trial-and-error instinct — never in formal repos.