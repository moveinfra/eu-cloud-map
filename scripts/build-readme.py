#!/usr/bin/env python3
"""Regenerates the tables in README.md from data/eu-cloud-map.json. Run: python3 scripts/build-readme.py"""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "eu-cloud-map.json").read_text())
readme = root / "README.md"
START, END = "<!-- map:start -->", "<!-- map:end -->"

SOURCES = {"aws": "AWS", "gcp": "Google Cloud", "azure": "Azure", "digitalocean": "DigitalOcean"}
TARGETS = {"upcloud": "UpCloud 🇫🇮", "scaleway": "Scaleway 🇫🇷", "hetzner": "Hetzner 🇩🇪", "ovhcloud": "OVHcloud 🇫🇷"}
STATUS = {"automatic": "✅", "assisted": "🛠️", "not-yet": "❌"}
cell = lambda s: (s or "—").replace("|", "\\|")

out = ["### What you use today", "", "| Capability | " + " | ".join(SOURCES.values()) + " |", "|---" * (len(SOURCES) + 1) + "|"]
for c in data["capabilities"]:
    out.append(f"| **{cell(c['label'])}** | " + " | ".join(cell(c["sources"].get(s, {}).get("product")) for s in SOURCES) + " |")

out += ["", "### EU-owned equivalent", "", "| Capability | " + " | ".join(TARGETS.values()) + " |", "|---" * (len(TARGETS) + 1) + "|"]
for c in data["capabilities"]:
    row = []
    for t in TARGETS:
        m = c["targets"][t]
        note = f"<br><sub>{cell(m['notes'])}</sub>" if m.get("notes") else ""
        row.append(f"{STATUS[m['migration']]} {cell(m['product'])}{note}")
    out.append(f"| **{cell(c['label'])}** | " + " | ".join(row) + " |")

text = readme.read_text()
head, rest = text.split(START, 1)
readme.write_text(head + START + "\n" + "\n".join(out) + "\n" + END + rest.split(END, 1)[1])
print(f"README.md: {len(data['capabilities'])} capabilities")
