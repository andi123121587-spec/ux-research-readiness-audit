# 用户研究就绪度审计 Skill V2.2

## 版本目标

V2.2 根据 27 份有效 Benchmark 输出迭代，主要修复：

- 冲突证据被错误升级为方向级 BLOCKER；
- 暂停当前方案被误写成暂停整个原型方向；
- 九项最低分析包机械生成大量重复 MAJOR/BLOCKER；
- 成熟项目被过度审计；
- 固定完整报告导致运行和人工复核成本过高。

## 核心新增

- 冲突层级：问题存在性、用户范围、需求权衡、方案默认值、交互细节；
- 根因注册表 `RC-xxx` 与 `affected_dimensions`；
- BLOCKER 反事实门槛；
- 方案收敛状态 `PAUSE_PROPOSED_SOLUTION`；
- 阶段校准与根因去重；
- `compact` 默认输出与 `full` 完整输出；
- V2.2 回归测试和一致性校验。

## 显式调用

```text
$ux-research-readiness-audit-v2-2
```

默认关闭隐式调用，便于与 V1、V2.1.1 进行对照测试。
