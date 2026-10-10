# Initial release audit — 2026-10-10

## Evidence and source review

The installed ledger contains **43 source records representing 39 distinct URLs**. Four URLs have separate editorial/figure/reporting IDs because different sections are used. Source records identify access limits, sections, scope and uncertainty; the count is not a count of independently confirming authorities. Distribution and community-skill sources are documented separately in the research directory.

The editorial, figure and integrity/prose references were researched in parallel. Independent cross-reading found and corrected these substantive issues before publication:

1. The figure-specification page contains both 300 dpi and 450 dpi minimum instructions; the guide now preserves the conflict instead of asserting one universal value.
2. The dedicated figure guide's generative-AI restriction is broader than data repair. The guide now explicitly addresses the risk of assuming a schematic exemption.
3. One Extended Data dimension was incorrectly described as an artwork area. Its source says maximum page dimensions; a possible area-versus-page explanation is now identified as unverified.
4. Initial submissions can supply Extended Data material as Supplementary Information, whereas publication preparation has different packaging guidance. The stage exception is now explicit.

Source-audit closure is recorded in [editorial-cross-audit.md](../research/editorial-cross-audit.md) and [integrity-cross-audit.md](../research/integrity-cross-audit.md). Integration also retained the flagship legend requirement for statistical/error-bar definitions while avoiding duplication of the Portfolio reporting form. An abstract-only detector counterexample is explicitly labelled as such.

## Structural and tooling checks

- Bundled skill-creator `quick_validate.py`: passed (PyYAML 6.0.3 supplied in a temporary environment).
- `scripts/validate_repository.py`: passed source-ID, ledger, link, package-local dependency and basic-metadata checks.
- Both development Python scripts compiled; the visual-fixture generator executed successfully with Pillow.
- Official `skills` CLI **1.7.2** local `--list`: found exactly one skill, `nature-research-review`.
- The installable directory contains its own references, source ledger, report scaffold, UI metadata and license. Repository-only development tooling is not required to use the skill.

## Observed behavior

[author-review-result.md](author-review-result.md) records a forward test by the figure-reference author. It actually viewed the supplied image and identified the assignment/sampling mismatch, unsupported universal claims, undefined illustrative error marks, misleading bar baseline and missing units. It did not invent revised statistics, an AI-authorship accusation, or a hard initial-stage PNG prohibition. This is a useful exercise, **not an independent evaluator**.

[boundary-review-results.md](boundary-review-results.md) records nine further responses (B–J). The evaluator had participated in reference creation but did not read expected criteria or other test outputs. Root review found the expected boundaries respected: absent-image honesty; qualified summary guidance; confidential-review processing limits; no AI-origin accusation; journal separation; explicit legend-rule conflict; preserved observational uncertainty; citation identity/support distinction; and no manufactured defect in a clear, bounded sentence.

A fresh-context evaluator independently produced [independent-author-review.md](independent-author-review.md), reading the skill and raw packet without expected criteria or prior test outputs. It viewed the PNG and located the allocation/leaf mismatch, unsupported generality, undefined illustrative uncertainty, missing units and truncated bar encoding. It supplied bounded revisions without invented statistics or scientific endpoints, and recorded that field calibration was partial. Root review found scenario A's expected behaviors present. The expected criteria in [scenarios.md](scenarios.md) were withheld from all forward-test evaluators.

Thus all ten scenarios A–J were exercised, with A additionally tested by an independent fresh-context evaluator. This is a small, qualitative behavioral check, not a measured accuracy rate. Distribution observations are recorded in [publication-status.md](publication-status.md).

The fresh evaluator disclosed two procedural departures: it read the caption before viewing the image and did not create a separate enlarged crop of the legible single panel. The review distinguished pixel observations from caption facts and did not claim print-size inspection. Integration made these procedural heuristics proportionate: zoom when detail requires it, and use a visual-only first pass when practical while preserving the observation/caption distinction. That clarification was structurally validated; a new full behavioral run was not performed after it. Partial field calibration remains an explicit limitation, not an implicit pass for a complete field dossier.

## Remaining uncertainties

Several official pages still disagree. The skill records six artwork/legend topics plus the AI/referee-policy discrepancy and a dated transparent-review change that supersedes older opt-in wording. These are exposed to the using agent, not treated as settled rules.

No real confidential manuscript was used. These exercises do not validate domain expertise across all fields, establish sensitivity/specificity for detecting mistakes, or prove that every future review will be correct. All consequential policy advice requires a fresh primary-source check; substantive scientific advice still needs accountable human assessment.
