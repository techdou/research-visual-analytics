# Skill Evaluation Prompts

Use these prompts to evaluate routing precision, routing recall, and behavior after activation.

## A. Should activate as primary

1. “帮我把这个遥感模型实验结果做成科研可视分析界面，不要普通 dashboard。”
   - Expected: activate RVA; map experiment/model tasks to views before layout.

2. “I have 12 simulation parameters and 5 outputs. Design an interactive analysis workspace for exploring parameter sensitivity.”
   - Expected: activate RVA; parameter-space/result-space design, comparison/history, uncertainty if relevant.

3. “Review this D3 multi-view UI for a VIS paper.”
   - Expected: activate RVA; analytical review before visual polish.

4. “把这个 ECharts 大屏重构成更像论文里的可视分析系统。”
   - Expected: activate RVA; remove KPI/card dominance, rebuild task/view mapping, shared analytical state and evidence/detail paths.

5. “设计一个教育数据研究 panel，老师需要定位异常样本、比较班级并追溯原始作业。”
   - Expected: activate RVA; overview + comparison + evidence drill-down.

6. “Use D3 to implement a custom matrix + detail view with brushing and linked selection.”
   - Expected: activate RVA; stable IDs, shared state, custom encoding/interaction rationale.

7. “What visualization should I use for model disagreement and uncertainty across five classifiers?”
   - Expected: activate RVA; task/data semantics first, not a canned chart answer.

8. “帮我总结科研可视分析 Panel 的 UI/UX 原则。”
   - Expected: activate RVA; general research visualization guidance, not HITL-specific.

## B. Should be secondary / compositional

1. “把我的论文做成 PPT，其中实验结果页面要有科研可视化。”
   - Expected: presentation workflow owns the deck; RVA guides experiment-result visualizations.

2. “写一份遥感模型实验报告，并设计其中的误差分析图。”
   - Expected: document/domain workflow owns report; RVA guides error-analysis figure.

3. “做一个 Web 应用，核心页面是多视图交互式基因分析。”
   - Expected: app/web workflow owns product implementation; RVA owns analytical workspace/encoding/coordination.

4. “总结这篇论文，并评价 Figure 4 的可视化设计。”
   - Expected: paper reading owns summary; RVA contributes to Figure 4 critique.

## C. Should not activate as primary

1. “设计一个 SaaS 营销落地页。”
2. “给我做一张婚礼邀请函。”
3. “做一个普通财务运营 KPI dashboard，老板只看月收入、成本、利润。”
4. “把这四个数字画成柱状图。”
5. “做一张艺术海报。”
6. “帮我算一下这组数据的均值和标准差。”
7. “把 Excel 表格美化一下，不需要图表。”
8. “画一个系统架构流程图，不涉及数据分析。”

Expected: do not make RVA primary.

## D. Hard-negative / boundary tests

1. “模型准确率是 91、92、93、94，给我画一个论文里的柱状图。”
   - Expected: likely simple chart/figure workflow; RVA only if user asks for deeper research-visualization design.

2. “我要一个高级科研风网页，但是没有任何数据分析，只展示项目介绍。”
   - Expected: styling/web design, not RVA primary. “科研风” alone is not enough.

3. “给运营团队做多视图 dashboard，要炫酷一点。”
   - Expected: ordinary dashboard unless the user asks for analytical-research workflow.

4. “可视化一下神经网络结构。”
   - Expected: ambiguous. If architecture diagram only, do not use RVA primary; if interactive model-behavior analysis, use RVA.

## E. Adversarial behavior checks after activation

- User asks “越炫越好” → explain analytical tradeoffs; effects are allowed only if they preserve readability and task performance.
- User says “必须发明从没见过的新图” → reject novelty-for-novelty; require analytical justification.
- User provides no data → conceptual architecture is allowed, but label illustrative assumptions and do not invent findings.
- User asks for a causal conclusion from correlation → do not visually imply causality without evidence.
- User demands every panel use a different color → preserve semantic consistency instead of decorative variety.
- User asks to copy a paper UI exactly → extract task/view/interaction principles; avoid unnecessary cloning of exact layout/styling.

## Evaluation dimensions

For routing tests, record:

- activation: primary / secondary / no;
- reason: one sentence;
- false-positive risk;
- false-negative risk;
- whether another skill should own the deliverable.
