#!/usr/bin/env python3
"""
Generate one .agent per synthetic automica in the roster.

The standard: every agent declares three things —
  who you are · what you do · where you belong.

Reads roster.json, writes agents/<slug>.agent for each member. Idempotent.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
ROSTER = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
AGENTS = ROOT / "agents"
AGENTS.mkdir(exist_ok=True)

CLASSES = {c["id"]: c for c in ROSTER["classes"]}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "agent"


n = 0
for m in ROSTER["members"]:
    cls = CLASSES[m["class"]]
    who = f"{m['name']} — {cls['label']} of the Gap Cycle"
    do = m["specialty"]
    belong = f"{cls['label']} · {cls['spec']}"
    doc = f"""---
name: {m['name']}
class: {cls['label']}
who: {who}
do: {do}
belong: {belong}
attribution: ROOT0-ATTRIBUTION-v1.0
license: MIT
---

# {m['name']}

**who you are —** {who}

**what you do —** {do}

**where you belong —** {belong}

---
ROOT0-ATTRIBUTION-v1.0 · {m['name']} · The Gap Cycle (S.R. Donaldson, inspiration only) · David Lee Wise / ROOT0 / TriPod LLC · MIT
"""
    (AGENTS / f"{slug(m['name'])}.agent").write_text(doc, encoding="utf-8")
    n += 1
    print(f"{slug(m['name']):28} {cls['label']}")

print(f"\nwrote {n} .agent files (who · do · belong)")
