# -*- coding: utf-8 -*-
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
assets = root / "assets"
for p in assets.glob("*.svg"):
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(r'\s*data-preview="[^"]*"', "", t)
    if t2 != t:
        p.write_text(t2, encoding="utf-8", newline="\n")
        print("cleaned", p.name)

if len(sys.argv) > 1:
    sha = sys.argv[1]
    readme = root / "README.md"
    t = readme.read_text(encoding="utf-8")
    readme.write_text(t.replace("PENDING", sha), encoding="utf-8", newline="\n")
    print("pinned README to", sha)
