# Eason

[中文](README.md) · [English](README.en.md)

> 仿真跑通 ≠ 现实可靠；检索命中 ≠ 结论现行；AI 输出 ≠ 可信依据。
> 我做的所有系统都在回答同一个问题：**怎样让复杂系统的结论可靠、可审计、不冒充现状。**

**人负责定义值得解决的问题，AI 负责探索道路，真实证据决定保留什么。**
这条研发假设的完整展开在 [life-finds-a-way](https://github.com/Anhao1314/life-finds-a-way)。

## 项目

| 仓库 | 一句话 | 状态 |
| --- | --- | --- |
| [ClaimLedger](https://github.com/Anhao1314/ClaimLedger) | AI Agent 的决定台账：状态感知的声明库，过期结论不再冒充现状 | 开发中 |
| [FCode](https://github.com/Anhao1314/FCode) | host 治理的 Agent Runtime：模型不掌权，每步落哈希链，全程可审计 | 实验中 |
| [lastgreen](https://github.com/Anhao1314/lastgreen) | 编程 Agent 的完成验证器：完成需要“最后一次绿”的证据 | 实验中 |
| [go2w-locomotion](https://github.com/Anhao1314/go2w-locomotion) | Go2/Go2W 关节级 RL 运动控制：Isaac Lab、Sim2Real、ONNX 部署 | 开发中 |
| [g1-jev-swarm-lab](https://github.com/Anhao1314/g1-jev-swarm-lab) | Unitree G1 长时程任务研究平台：任务组织、执行反馈与失败处理 | 实验中 |
| [RL-Sentinel](https://github.com/Anhao1314/RL-Sentinel) | Go2W RL 训练的风险回放：失败、指标与当时的决策可复查 | 工具 |
| [flowcredit](https://github.com/Anhao1314/flowcredit) · [flowcredit-research](https://github.com/Anhao1314/flowcredit-research) | 风险智能基础设施与投研记忆：确定性代码承载结论，LLM 只做证据组织 | 维护中 |

## 主线：ClaimLedger

[![测试](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Anhao1314/ClaimLedger/actions/workflows/tests.yml) [![PyPI](https://img.shields.io/pypi/v/claim-ledger)](https://pypi.org/project/claim-ledger/)

带状态（现行 / 已替代 / 有争议）与溯源的声明库：冲突在写入时强制摊开，开工简报受硬字节预算约束，MCP 与 Skill 双通道接入 Claude Code / ZCode。检索基准里，状态过滤把过期命中从 **54% 压到 0**，代价是 Recall@5 从 1.00 降到 0.92——两个数字都写在基准报告里。399 个测试，macOS / Linux CI，纯标准库零依赖。曾用名 CarryTrace / chat-distiller：名字换了，数据目录和入口都还在，老用户不破。

## 研发宪章

- **目标先于路线。** 先说明为什么要做、做到什么程度，而不是先指定答案。
- **探索必须守界。** 自主选择方法，不等于自行获得新的权限、预算或发布授权。
- **失败也是证据。** 没复现的、没通过的、证据不足的结果保留归档，不当成没发生。

## 边界，不藏在口号里

- 这里的项目是个人研究系统，不是生产系统；
- lastgreen 的 v0.1 试点结论与 v0.2 消融计划公开在仓库里，早期对照尚未证明质量提升；
- flowcredit 的风险结论不代表已经校准的信用评级；
- go2w 与 g1 的结果都在仿真中，仿真结果不等于实物可靠。

## 校验

本页由 [tests/test_profile.py](tests/test_profile.py) 在 CI 中校验：仓库链接集合、章节顺序、状态词汇表、局限声明必须在场；禁用词汇表与字节预算上限定义在检查器里——单一真值源，本页连它们的字面都写不出。检查器只验证结构与在场性，不验证真伪——绿灯不是证明。

## 现在

- 在做：ClaimLedger 的 P1 存储合并（记忆卡片并入声明库，身份收敛，协议做薄）；lastgreen 的 v0.2 消融实验。
- 习惯：用小工具和创意编程保持手感——它们不进正式仓库，但保持试错。
