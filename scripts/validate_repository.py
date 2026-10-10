#!/usr/bin/env python3
"""Offline structural validation, not verification of scientific truth.

Run --build-ledger after an intentional source-manifest update. Ordinary runs
compare the installable ledger with research records without modifying files.
Only the repository containing this script is inspected.
"""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "nature-research-review"
MANIFESTS = ("nature-sources.json", "figure-sources.json", "integrity-sources.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-ledger", action="store_true")
    args = parser.parse_args()
    errors, records, ids = [], [], set()
    for name in MANIFESTS:
        path = ROOT / "research" / name
        try:
            manifest = json.loads(path.read_text())
            for source in manifest["sources"]:
                sid = source.get("id")
                if not isinstance(sid, str) or not re.fullmatch(r"[NFR]\d{2}", sid):
                    errors.append(f"Invalid source ID in {name}: {sid!r}")
                    continue
                if sid in ids:
                    errors.append(f"Duplicate source ID: {sid}")
                ids.add(sid)
                for field in ("title", "url", "accessed", "scope"):
                    if not source.get(field):
                        errors.append(f"{sid}: missing {field}")
                if not source.get("url", "").startswith("https://"):
                    errors.append(f"{sid}: expected HTTPS source URL")
                records.append({**source, "audit_manifest": name})
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"Cannot read {name}: {exc}")
    ledger = {
        "schema_version": 1,
        "audit_date": "2026-10-10",
        "notice": "Source index, not immutable policy. Reopen current sources before journal-specific advice. Operational heuristics are identified in the linked guides.",
        "sources": sorted(records, key=lambda s: s["id"]),
    }
    dest = SKILL / "references" / "sources.json"
    if args.build_ledger and not errors:
        dest.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
    try:
        if json.loads(dest.read_text()) != ledger:
            errors.append("Installed source ledger is stale; review manifests then use --build-ledger")
    except (OSError, ValueError) as exc:
        errors.append(f"Source ledger missing or invalid: {exc}")

    md = SKILL / "SKILL.md"
    body = md.read_text()
    # Deliberately minimal checks; actual YAML is tested by skill-creator/CLI.
    parts = body.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append("SKILL.md must begin with frontmatter")
    else:
        name_match = re.search(r"^name:\s*(\S+)\s*$", parts[1], re.M)
        description = re.search(r"^description:\s*(.+)$", parts[1], re.M)
        if not name_match or name_match.group(1) != SKILL.name:
            errors.append("Skill name/folder mismatch")
        if not description or len(description.group(1)) > 1024:
            errors.append("Missing or oversized description")
    if len(body.splitlines()) >= 500:
        errors.append("Entrypoint exceeds 500-line packaging guideline")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        content = path.read_text()
        for label, target in re.findall(r"\[([^\]]*)\]\(([^)]+)\)", content):
            target = target.strip().strip("<>")
            if target.startswith("#") or urlsplit(target).scheme:
                continue
            local = unquote(target.split("#", 1)[0])
            resolved = (path.parent / local).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{path.relative_to(ROOT)}: link leaves repository: {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target: {target}")
            if path.is_relative_to(SKILL) and not resolved.is_relative_to(SKILL):
                errors.append(f"Installed skill depends on repository-only file: {target}")
        if path.is_relative_to(SKILL):
            for sid in set(re.findall(r"\b[NFR]\d{2}\b", content)):
                if sid not in ids:
                    errors.append(f"{path.relative_to(ROOT)}: unresolved source {sid}")
            if re.search(r"\bTODO\b|\[INSERT\b", content):
                errors.append(f"Unfinished scaffold: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print("FAIL:", error)
        raise SystemExit(1)
    unique_urls = {s["url"] for s in records}
    print(f"PASS: 1 skill, {len(records)} source records, {len(unique_urls)} distinct source URLs")
    print("PASS: source IDs, ledger consistency, local links, self-contained package, basic metadata")
    print("LIMIT: this does not validate scientific claims, live policy, external links, or reviewer performance")


if __name__ == "__main__":
    main()
