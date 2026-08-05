# 输出与审计记录模板 V2.2

## 一、输出模式

### Compact（默认）

#### 1. 审计摘要

- 项目模式：
- 当前阶段：
- 输出模式：`compact`
- 原型探索状态：
- 方案收敛状态：
- 研究主张状态：
- 三档总评：
- 一句话结论：

#### 2. 根因 Issue 注册表

| Issue ID | Root Cause ID | 严重度 | 冲突层级 | 受影响维度 | 当前原型影响 | 处理状态 | 复审条件 |
|---|---|---|---|---|---|---|---|

派生统计：`BLOCKER / MAJOR / MINOR / Total`。

#### 3. 关键证据边界

| 当前证据支持 | 当前证据不支持 | 限制/反例 | 置信度 |
|---|---|---|---|

#### 4. 设计师决策

- 主题：
- 可选路径 A：
- 可选路径 B：
- 每条路径需要验证：
- 标记：`DESIGNER_DECISION_REQUIRED`

#### 5. 优先行动计划

| 顺序 | Issue ID | 行动 | AI 初稿 | 设计师审核 | 分析执行 | 日历依赖 | 完成标准 |
|---|---|---|---|---|---|---|---|

#### 6. 一致性检查

- Issue ID 唯一：PASS/FAIL
- 严重度统计一致：PASS/FAIL
- 行动计划引用有效：PASS/FAIL
- BLOCKER 通过反事实门槛：PASS/FAIL
- 允许低成本探索时未误用 `PAUSE_CORE_PROTOTYPING`：PASS/FAIL

---

## 二、Full（正式归档/高风险项目）

### 1. 项目输入

- 项目名称：
- 项目模式：
- 当前阶段：
- 目标用户：
- 核心任务：
- 业务目标：
- 约束：
- 输入版本：
- 审计日期：
- Skill 版本：2.2.0

### 2. 材料盘点

| ID | 分类 | 材料 | 来源 | 位置 | 支持内容 | 限制/冲突 | 人工确认 |
|---|---|---|---|---|---|---|---|

### 3. 九项最低分析包

| 分析项 | 状态 | 核心问题是否回答 | 主要证据 | 根因 ID | 风险 | 推荐处理 |
|---|---|---|---|---|---|---|

> 九项状态不自动生成 Issue。同一根因可影响多个维度。

### 4. 原型验证状态

- 计划完整度：`NOT_PLANNED / PARTIAL_PLAN / SUFFICIENT_PLAN`
- 执行状态：`NOT_EXECUTED / IN_PROGRESS / EXECUTED_WITH_RECORDS`
- 结果证据：`NO_EVIDENCE_YET / PARTIAL_EVIDENCE / EVIDENCE_AVAILABLE`

### 5. 根因注册表

| Root Cause ID | 根因 | 冲突层级 | 证据/缺失 | 受影响维度 | 可否通过低成本原型学习 | 不可逆风险 | 拆分说明 |
|---|---|---|---|---|---|---|---|

### 6. BLOCKER 反事实测试

| 候选 Issue | 核心问题存在性未知 | 低成本原型能否学习 | 不可逆风险 | 是否将直接高成本承诺 | 学习目标/停止条件 | 判定 |
|---|---|---|---|---|---|---|---|

### 7. Issue 注册表

| Issue ID | Root Cause ID | 领域 | 严重度 | 冲突层级 | 受影响维度 | 状态 | 行动计划 | 复审条件 |
|---|---|---|---|---|---|---|---|---|

统计必须从注册表派生。

### 8. 证据链

| 证据 | 模式/洞察 | 用户问题 | 用户需求 | 设计目标 | 方案假设 | 验证状态 |
|---|---|---|---|---|---|---|

### 9. 三种状态

#### 原型探索状态

- `EXPLORE`
- `EXPLORE_WITH_GUARDRAILS`
- `PAUSE_CORE_PROTOTYPING`

#### 方案收敛状态

- `NO_PROPOSED_SOLUTION`
- `PROCEED_AS_HYPOTHESIS`
- `SUPPORTED_WITHIN_SCOPE`
- `PAUSE_PROPOSED_SOLUTION`

#### 研究主张状态

- `CLAIM_READY`
- `CLAIM_READY_AFTER_FIXES`
- `CLAIM_NOT_READY`

### 10. 三档总评

- `READY`
- `READY_AFTER_FIXES`
- `NOT_READY`

### 11. 设计决策选项卡

- 当前证据支持：
- 当前证据不支持：
- 选项 A / 风险 / 验证目标：
- 选项 B / 风险 / 验证目标：
- 标记：`DESIGNER_DECISION_REQUIRED`

### 12. 行动计划

| 顺序 | Issue ID | 行动 | 方法 | AI 初稿 | 设计师审核 | 分析执行 | 日历依赖 | 完成标准 | 复审范围 |
|---|---|---|---|---|---|---|---|---|---|

### 13. 输出一致性检查

| 检查项 | 结果 | 说明 |
|---|---|---|
| Issue ID 唯一 | PASS/FAIL | |
| Root Cause ID 有效 | PASS/FAIL | |
| 严重度统计一致 | PASS/FAIL | |
| 行动计划引用有效 | PASS/FAIL | |
| 未关闭 BLOCKER/MAJOR 有行动或确认点 | PASS/FAIL | |
| BLOCKER 通过反事实门槛 | PASS/FAIL | |
| 九项未被机械拆成重复 Issue | PASS/FAIL | |
| 方案暂停未被扩大为方向暂停 | PASS/FAIL | |

### 14. 复审记录

| 版本 | 日期 | Issue ID | 原状态 | 新证据/修改 | 新状态 | 设计师确认 |
|---|---|---|---|---|---|---|

### 15. Skill 测试记录

| Run | Skill 版本 | 案例 | Issue 数 | 原型状态 | 方案状态 | 主张状态 | 总评 | 人工修改次数 | 控制感 |
|---|---|---|---|---|---|---|---|---|---|
