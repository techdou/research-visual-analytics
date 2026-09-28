#!/usr/bin/env python3
from pathlib import Path
import argparse,re

p=argparse.ArgumentParser(description="Heuristic audit of a research visual analytics design brief. Warnings are advisory, not hard requirements.")
p.add_argument("file")
a=p.parse_args(); text=Path(a.file).read_text(encoding="utf-8",errors="ignore").lower()
checks={
"research question / goal":["research question","研究问题","analysis question","分析目标"],
"data description":["data","数据"],
"analysis tasks":["task","任务"],
"visual encoding":["encoding","视觉编码","mark","channel"],
"interaction":["interaction","交互","brush","filter","select"],
"multi-view coordination":["linked","coordination","联动","shared state","共享状态"],
"comparison":["compare","comparison","比较"],
"evidence/detail":["detail","evidence","sample","细节","证据","样本"],
"uncertainty/limitations":["uncertainty","limitation","不确定","局限"],
"evaluation":["evaluation","validate","评估","验证"]}
print("Keyword presence only — not semantic validation")
for label,terms in checks.items():
    ok=any(t in text for t in terms)
    print(("[PRESENT] " if ok else "[WARN] ")+label)

anti=["智慧大脑","驾驶舱","neon","glassmorphism"]
found=[x for x in anti if x in text]
if found: print("[NOTE] Decorative/dashboard terms found; verify they serve the analytical task:",", ".join(found))
