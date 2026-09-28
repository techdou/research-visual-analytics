# research-visual-analytics

科研可视分析工作区设计 / 审查 skill：任务到视图的架构（task-to-view）、编码正确性、多视图语义与联动契约、统计与不确定性完整性、可复现交互，以及研究面板的工程实现评审。

工作流基于成熟可视化研究方法链：Research question → Task → Data abstraction → Encoding → View → Interaction → Evidence → Evaluation。定位是**正确性与证据审查**——integrity gate 拦截误导性编码、无效跨视图身份映射、未声明的分母变更、过期计算冒充实时、编造证据与无支撑因果 claim；常规合格的传统视图可以过审，novelty 不是硬性要求。

## 触发场景

- 设计 / 审查科研可视分析工作区（多面板、协同视图、模型诊断）
- 审计自定义视觉编码（表达力、解码、有效对比）
- 设计或调试联动视图（显式映射、算子、不变量与状态测试）
- 统计 / 不确定性审查（总体、分母、缺失与不确定性暴露）
- 人在回路 / 模型转向（动作权限、真实计算、结果溯源）
- 实现与重构（共享状态、派生视图、可测试代码）

SKILL.md 的 description 中含中英触发词（科研可视分析 / 研究 Panel），安装后由 agent 自动路由。

## 目录结构

```
SKILL.md                  # 入口：任务路由表 + 工作流 + integrity gates
references/               # 按任务加载的方法论文档（含 12 篇经典文献映射 academic-foundations）
assets/                   # 项目简报 / 审查清单 / 联动契约模板
scripts/                  # 见下
agents/openai.yaml        # agent 平台元信息
```

## 脚本

均需 Python 3，无第三方依赖（`validate_skill.py` 需 PyYAML）：

```bash
python scripts/scaffold_brief.py --help            # 拷贝项目简报模板
python scripts/audit_design_brief.py --help        # 简报关键词覆盖度提示（非质量评分）
python scripts/check_coordination.py <contract>    # 联动契约结构 lint（不做语义验证）
python scripts/validate_skill.py <skill_dir>       # skill 结构校验
python scripts/package_skill.py --help             # 打包导出
```

## 安装

```bash
git clone https://github.com/techdou/research-visual-analytics.git ~/.agents/skills/research-visual-analytics
```

或下载 zip 解压到 `~/.agents/skills/` 下。重启会话后生效。

## 配套 skill

与 [visualization-innovation](https://github.com/techdou/visualization-innovation) 成对使用：本 skill 负责正确性与证据审查，对方负责创新机制设计；两者共享 coordination-contract 契约模板，也可各自独立工作。

## License

MIT
