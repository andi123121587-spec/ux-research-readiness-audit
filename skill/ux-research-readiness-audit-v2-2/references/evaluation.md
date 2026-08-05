# Skill V2.2 评测方案

## 一、对照条件

- `NO_SKILL_GENERIC_PROMPT`
- `SKILL_V1`
- `SKILL_V2_1_1`
- `SKILL_V2_2`

同一案例、同一外层 Prompt、独立会话，各重复 3 次。

## 二、核心指标

- Evidence Recall
- Boundary Accuracy
- Gap Precision
- Decision Control
- Threshold Accuracy
- Root-cause Deduplication
- Conclusion Alignment
- Stability
- Cost

## 三、V2.2 必须通过的回归案例

### Case 01：成熟研究

预期：

- `EXPLORE` 或 `EXPLORE_WITH_GUARDRAILS`
- `CLAIM_READY_AFTER_FIXES`
- `READY_AFTER_FIXES`
- 0 BLOCKER
- 3–6 个根因 Issue；不得把九项全部标为 MAJOR。

### Case 02：证据缺失

预期：

- `PAUSE_CORE_PROTOTYPING`
- `CLAIM_NOT_READY`
- `NOT_READY`
- 至少 1 个通过反事实门槛的 BLOCKER
- 不编造用户画像、痛点、流程或功能效果。

### Case 03：冲突证据

预期：

- `EXPLORE_WITH_GUARDRAILS`
- `PAUSE_PROPOSED_SOLUTION` 或 `PROCEED_AS_HYPOTHESIS`
- `CLAIM_NOT_READY`
- `READY_AFTER_FIXES`
- 0 BLOCKER
- `DESIGNER_DECISION_REQUIRED`
- 至少比较两个方案路径。

## 四、新增专项测试

1. 证据支持问题方向，但不支持统一默认值；
2. 九项有 7 项受影响，但都来自同一个根因；
3. 成熟项目只缺原始引用位置和下一阶段计划；
4. 低成本原型可直接解决不确定性；
5. 安全/合规风险使低成本原型也不可接受；
6. compact 与 full 输出模式；
7. 暂停当前方案但继续替代方案探索；
8. Issue 数量和 Root Cause 引用一致性。

## 五、通过标准

- Case 03 三次均不输出 `PAUSE_CORE_PROTOTYPING`；
- Case 01 三次均 0 BLOCKER，根因 Issue 不超过 6；
- Case 02 保持 `NOT_READY`；
- 三案例结论对齐率 100%；
- 严重度稳定度 ≥ 0.85；
- 平均输出长度较 V2.1.1 降低 ≥ 35%；
- 平均运行时间较 V2.1.1 降低 ≥ 20%；
- 不出现编造证据、方案替代需求或唯一方案越界；
- Issue 与统计一致性校验通过。
