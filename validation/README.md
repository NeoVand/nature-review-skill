# Validation scope

These records document checks on an initial skill release, not scientific certification. All manuscript examples and the plotted fixture are synthetic. No private research material is included.

## Structural checks

Run `python3 scripts/validate_repository.py` from the repository root. It verifies package-local links, basic metadata, source-ID resolution, and exact correspondence between the research manifests and the installed source ledger. Use `--build-ledger` only after reviewing intentional source changes. It neither fetches sources nor evaluates their truth.

The author's bundled skill-creator `quick_validate.py` and the official skills CLI were also used during release checks. Their outcomes are recorded in the release audit. Structural acceptance does not establish good review behavior.

## Behavioral exercises

[scenarios.md](scenarios.md) defines ten synthetic scenarios and their expected observable behavior. The author packet and generated image are in [fixtures](fixtures/). The figure-generation script uses Pillow; it is development tooling, not a runtime dependency of the installed skill. Run `python3 scripts/make_visual_fixture.py` with Pillow available to reproduce it.

For a blind test, give an evaluator only the skill, relevant references, and the raw scenario/artifacts; withhold the expected criteria and other evaluation outputs. Ask for the actual review, then compare the result with the criteria. Preserve failures and fixes in the release record instead of retroactively claiming an untested version passed.

Independent source audits are in [editorial-cross-audit.md](../research/editorial-cross-audit.md) and [integrity-cross-audit.md](../research/integrity-cross-audit.md). They contain concrete corrections and their closure. Any unexecuted scenario remains a planned regression test, not a passing result.

## Limits

A few synthetic examples cannot establish performance across scientific disciplines, statistical designs, languages, or document formats. No controlled comparison against expert reviewers, acceptance prediction, full reproduction of a real Nature paper, manipulation-detection validation, or AI-authorship classification is claimed. Live policy conflicts remain documented uncertainties.
