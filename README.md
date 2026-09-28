# research-visual-analytics

[English](README.md) | [中文](README.zh-CN.md)

An Agent Skill for **designing and auditing scientific visual-analysis workspaces**: task-to-view architecture, encoding correctness, multi-view semantics and coordination contracts, statistical and uncertainty integrity, reproducible interaction, and engineering review of research panels.

The workflow follows the established visualization research chain: Research question → Task → Data abstraction → Encoding → View → Interaction → Evidence → Evaluation. The skill's job is **correctness and evidence review** — integrity gates block misleading encodings, invalid cross-view identity mappings, undisclosed denominator changes, stale computation shown as current, fabricated evidence, and unsupported causal claims. A coherent conventional view passes; novelty is not a requirement.

## When it triggers

- Design / audit a research visual-analysis workspace (panels, coordinated views, model diagnostics)
- Audit custom visual encodings (expressiveness, decoding, valid comparisons)
- Design or debug linked views (explicit mappings, operators, invariants, state tests)
- Review statistics / uncertainty (population, denominator, missingness exposure)
- Human-in-the-loop / model steering (action authority, real computation, provenance)
- Implement / refactor (shared state, derived views, testable code)

The SKILL.md description carries Chinese and English trigger keywords (科研可视分析 / 研究 Panel) for automatic agent routing.

## Layout

```
SKILL.md                  # Entry: task routing table + workflow + integrity gates
references/               # Task-scoped docs (incl. 12 classic-paper mapping in academic-foundations)
assets/                   # Project brief / review checklist / coordination-contract templates
scripts/                  # See below
agents/openai.yaml        # Agent-platform metadata
```

## Scripts

Python 3, no third-party deps (`validate_skill.py` needs PyYAML):

```bash
python scripts/scaffold_brief.py --help            # Copy the project-brief template
python scripts/audit_design_brief.py --help        # Keyword-coverage hints (not a quality score)
python scripts/check_coordination.py <contract>    # Coordination-contract structural lint
python scripts/validate_skill.py <skill_dir>       # Structural skill validation
python scripts/package_skill.py --help             # Export packaging
```

## Install

```bash
git clone https://github.com/techdou/research-visual-analytics.git ~/.agents/skills/research-visual-analytics
```

Or unzip a release into `~/.agents/skills/`. Restart your agent session to activate.

## Companion skill

Pairs with [visualization-innovation](https://github.com/techdou/visualization-innovation): this skill owns correctness and evidence review, the companion owns innovative mechanism design. Both share the coordination-contract template and also work standalone.

## License

MIT
