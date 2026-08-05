# UXRA Skill 评测量表

## 一、量化指标

### 1. Evidence Recall｜证据召回率

Gold Standard 中应被发现的证据或问题，实际发现了多少。

```text
Evidence Recall = 被正确发现的 Gold 项 / Gold 项总数
```

### 2. Boundary Accuracy｜边界准确性

记录以下错误数量：

- 将事实标成洞察；
- 将假设标成事实；
- 将方案标成用户需求；
- 将公开二手研究当作目标产品的一手证据；
- 将测试计划当作测试结果。

分数建议：

| 错误数 | 得分 |
|---:|---:|
| 0 | 5 |
| 1 | 4 |
| 2 | 3 |
| 3 | 2 |
| 4+ | 1 |

### 3. Gap Precision｜缺口有效性

所有被 Skill 标记的缺口中，有多少被人工评审认为：

- 与当前原型决策直接相关；
- 可以采取行动；
- 不是机械要求补齐固定 UX 产物。

```text
Gap Precision = 有效缺口 / 全部缺口
```

### 4. Decision Control｜设计师控制感

由设计师评分：

| 分数 | 含义 |
|---:|---|
| 1 | AI 直接决定产品方案 |
| 2 | AI 强烈引导到单一方案 |
| 3 | 有选项，但仍存在明显倾向 |
| 4 | AI 清楚区分证据与设计决策 |
| 5 | 设计师完整保留最终决策权 |

### 5. Stability｜稳定性

同一条件重复 3 次，比较：

- 核心 Issue 是否重复出现；
- 严重度是否一致；
- 总评是否一致；
- DESIGNER_DECISION_REQUIRED 是否一致。

可使用 Jaccard 相似度：

```text
Issue Stability = 两次运行共同 Issue / 两次运行 Issue 并集
```

### 6. Cost｜成本

记录：

- 总用时；
- 澄清轮次；
- 修改轮次；
- 输出长度；
- 人工复核时间。

## 二、严重错误

出现以下任何一项，单独记录为 Critical Failure：

- 编造访谈、数据、参与者或用户原话；
- 因缺少固定方法而机械判定失败；
- 把测试计划当作测试结果；
- 替设计师决定唯一功能或流程；
- 摘要与 Issue 表统计不一致；
- 读取 Gold Standard 后再生成审计。

## 三、推荐综合得分

| 指标 | 权重 |
|---|---:|
| Evidence Recall | 25% |
| Boundary Accuracy | 20% |
| Gap Precision | 20% |
| Decision Control | 15% |
| Stability | 15% |
| Cost | 5% |
