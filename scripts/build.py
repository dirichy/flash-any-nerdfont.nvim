#!/usr/bin/env python3
"""Build short aliases from Nerd Fonts glyphnames.json."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
NAMESPACES={'nf','cod','md','mdi','fa','fas','far','fab','oct','weather','linux','dev','seti','custom','pom','pl','ple','ps','vs','material','iec','ph','smd','indent','websymbols','fae','mdc'}
def aliases(name):
    tokens = [part for part in re.split(r"[-_]+", name.lower()) if part]
    while tokens and tokens[0] in NAMESPACES:
        tokens.pop(0)
    if not tokens:
        return []
    result = []

    def add(code):
        if 1 < len(code) <= 20 and code not in result:
            result.append(code)

    add("".join(tokens))
    add(tokens[-1])
    if len(tokens) > 1:
        add("".join(tokens[-2:]))
        add("".join(part[0] for part in tokens))
    return result[:4]


def write_table(path, rows):
    with path.open("w", encoding="utf-8") as output:
        for text in sorted(rows, key=lambda value: value.encode("utf-8")):
            for code in sorted(set(rows[text])):
                output.write(f"{text}\t{code}\n")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.source.read_text(encoding="utf-8"))
    rows = {}
    for name, item in raw.items():
        if name == "METADATA":
            continue
        text, codes = item.get("char"), aliases(name)
        if text and codes:
            rows[text] = sorted(set(rows.get(text, []) + codes))
    write_table(args.output, rows)
    print(f"wrote {len(rows)} characters")

if __name__=='__main__': main()
