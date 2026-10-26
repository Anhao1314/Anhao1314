# Eason

[中文](README.md) · [English](README.en.md)

> Simulation passing ≠ reality working; retrieval hit ≠ claim current; AI output ≠ trusted evidence.
> Everything I build answers the same question: **how to make a complex system's conclusions reliable, auditable, and unable to masquerade as present state.**

**People define which problems are worth solving, AI explores the paths, real evidence decides what survives.**
The full development of this working hypothesis lives in [life-finds-a-way](https://github.com/Anhao1314/life-finds-a-way).

## Projects

| Repo | One line | Status |
| --- | --- | --- |
| [ClaimLedger](https://github.com/Anhao1314/ClaimLedger) | The decision ledger for AI agents: status-aware claims, so stale conclusions stop masquerading as present | active |
| [FCode](https://github.com/Anhao1314/FCode) | Host-governed Agent Runtime: the model proposes, the host disposes, every step lands on a hash chain | experiment |
| [lastgreen](https://github.com/Anhao1314/lastgreen) | Completion verifier for coding agents: "done" requires evidence from the last green state | experiment |
| [go2w-locomotion](https://github.com/Anhao1314/go2w-locomotion) | Joint-level RL locomotion for Unitree Go2/Go2W: Isaac Lab, Sim2Real, ONNX deployment | active |
| [g1-jev-swarm-lab](https://github.com/Anhao1314/g1-jev-swarm-lab) | Research testbed for long-horizon Unitree G1 tasks | experiment |
| [RL-Sentinel](https://github.com/Anhao1314/RL-Sentinel) | Risk replay for Go2W RL training: failures, metrics and the decisions behind them, re-checkable | tool |
| [flowcredit](https://github.com/Anhao1314/flowcredit) · [flowcredit-research](https://github.com/Anhao1314/flowcredit-research) | Risk intelligence and investment-research memory: deterministic code carries conclusions, LLM organizes evidence | maintenance |

## Main line: ClaimLedger

[![Tests](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml) [![PyPI](https://img.shields.io/pypi/v/claim-ledger)](https://pypi.org/project/claim-ledger/)

A claim store with status (current / superseded / disputed) and provenance: conflicts are forced into the open at write time, working briefs are bound by a hard byte budget, and both MCP and Skill channels integrate with Claude Code / ZCode. In the retrieval benchmark, status filtering pushes stale hits from **54% to 0**, at the cost of Recall@5 dropping from 1.00 to 0.92 — both numbers are published in the benchmark report. 399 tests, macOS / Linux CI, pure standard library, zero dependencies. Formerly CarryTrace / chat-distiller: the name changed, the data directory and entry points did not — existing users don't break.

## Engineering charter

- **Goals before routes.** Say why and to what extent before prescribing how.
- **Exploration has boundaries.** Freedom to choose methods is not a grant of new permissions, budgets, or release authority.
- **Failure is evidence.** Results that don't reproduce, don't pass, or lack evidence stay archived — they are not treated as if they never happened.

## Limits, not hidden behind slogans

- These are personal research systems, not production systems;
- lastgreen's v0.1 pilot findings and v0.2 ablation plan are public in the repo; early A/B runs have not yet proven quality improvement;
- flowcredit's risk conclusions are not a calibrated credit rating;
- go2w and g1 results are in simulation; simulation results are not hardware reliability.

## Verification

This page is checked in CI by [tests/test_profile.py](tests/test_profile.py): the repo link set, section order, status vocabulary, and the limitation statements must be present; the forbidden-vocabulary list and the byte-budget ceiling live in the checker — single source of truth, and this page cannot even spell them out. The checker verifies structure and presence, not truth — a green check is not proof.

## Now

- Working on: ClaimLedger P1 storage merge (memory cards folded into the claim store, identity convergence, thinner protocol); lastgreen's v0.2 ablation.
- Habit: small tools and creative coding to stay sharp — they don't enter the formal repos, but they keep the trial-and-error alive.
