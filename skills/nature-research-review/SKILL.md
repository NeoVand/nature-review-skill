---
name: nature-research-review
description: Review author-owned drafts intended as research Articles in the flagship journal Nature, or critically read published Nature Articles. Audit claims, methods, citations, prose, and actual figure images with field-specific research and traceable evidence. Supports author revisions and permitted human-reviewer assistance; does not replace editorial judgment. Not a Nature Portfolio-wide formatting guide or an AI-authorship detector.
license: MIT
metadata:
  version: "0.1.0"
  policy-audit-date: "2026-10-10"
---

# Nature research review

Produce an evidence-grounded assessment that helps authors make a paper more accurate, intelligible, and reviewable. Preserve the science and the author's voice. Nature is the flagship journal, not a shorthand for all Nature Portfolio journals. Science and other journals need separately researched profiles; do not silently reuse Nature's rules.

This is an independent author-support skill, not Nature's own service or a certified substitute for expert review. Its workflow, issue priorities, tables, and suggested research effort are **review heuristics**, not journal requirements. Source-linked statements in the references distinguish policies, guidance, and unresolved conflicts. Never promise error-free science, compliance, acceptance, or reliable AI detection.

## Establish scope without obstructing useful work

Use the user's existing context to identify target journal/article type, discipline, study design, manuscript stage, material provided, and desired depth. Default to a substantive author-side review with detailed visual review when actual figures are available. A request to review does not by itself ask you to rewrite files; provide recommendations and sample edits. When editing is requested, retain a reviewable original/diff and never invent missing results or declarations.

For an author asking about their own draft or a public Article, proceed within the authorized scope. For **confidential material received as an appointed peer reviewer**, first read the AI/confidentiality section of [rigor-and-reporting.md](references/rigor-and-reporting.md) and current journal instructions. Nature's pages contain conflicting upload language. Resolve permitted processing before ingesting confidential files; reading a local file into a hosted assistant is still external processing. Human reviewers retain critique, judgment, and accountability. If permission is unresolved, work on public policies or the reviewer's general questions without the confidential material.

Inventory only the supplied/requested materials: main text, actual figure files/pages, legends, tables, Methods, Extended Data, supplement, source data/code, and any response letter. Record missing and inaccessible items. Do not call text extraction a visual inspection. A partial manuscript supports a partial review, not an invented verdict about the whole study.

## Refresh the applicable evidence

Read [evidence-review.md](references/evidence-review.md) and the relevant entries in [sources.json](references/sources.json). Open the live source before asserting a current journal rule or prescribing a format correction. Record journal, article type, stage, source section, access date, and whether the language is mandatory, recommended, typical, or conflicting. A saved audit date is not a guarantee of currency.

- Use [nature-articles.md](references/nature-articles.md) for Nature scope, editorial criteria, sections, references, and submission-stage distinctions.
- Use [rigor-and-reporting.md](references/rigor-and-reporting.md) for study validity, reporting, transparency, ethics, and AI policy; load the design-specific official standard only when applicable.
- Use [figures.md](references/figures.md) whenever images, figures, tables, or legends are in scope.
- Use [field-and-prose.md](references/field-and-prose.md) before field-specific style advice or prose revision.

If browsing fails, continue manuscript-internal analysis. Label journal compliance and literature novelty unverified; do not promote a cached preference to a current rule. Search using public topic/method terms, not confidential passages or unpublished findings.

## Learn the field before judging its writing

Build a compact field dossier from verified, relevant primary papers, appropriate methods/standards, and recent flagship Nature Articles when available. Follow the procedure in [field-and-prose.md](references/field-and-prose.md). Record why each comparison is appropriate, accessible content, date/version, methodological limits, and actual examples of section organization, claim strength, and terminology. Match study design and audience, not just keywords.

Search for both supporting and challenging precedents. Separate broad significance from narrow novelty and from validity. Never infer priority or “first ever” from a small comparison set or no search hits. Do not mistake a distinctive author style for a field-wide rule. When evidence is sparse, offer a bounded clarity review and mark field calibration incomplete.

## Review the scientific argument before polishing

1. State the research question, central advance, strongest evidence, and main uncertainty in neutral language. Check your interpretation against the manuscript.
2. Build a claim–evidence map: claim and exact location → design/analysis → figure/table and Methods location → stated uncertainty → alternative explanation → assessment. Include claims in title, summary, figure titles, and conclusion, not just Results.
3. Assess methods, controls, independent units, analysis assumptions, missingness/exclusions, multiplicity, validation, and scope using the appropriate discipline. Distinguish **not reported**, **not provided**, **unclear**, and **demonstrably inconsistent** from **not performed**.
4. Reconcile numbers, units, groups, time points, sample sizes, uncertainty definitions, and analysis sets across text, legends, tables, and source data. Request an explanation for a mismatch before deciding which value is wrong.
5. Review transparency and design-specific reporting. Checklist completion is not evidence that a design is sound. Suggest additional work only with the exact claim it would test and why available evidence is insufficient. Separate essential support from optional extensions; a narrower claim may resolve a concern without a new experiment.
6. Inspect references for bibliographic identity **and** actual claim support. A resolving DOI is not substantive verification. State citation-audit coverage; never claim all references were checked after sampling.

Do not calculate a prestige score or probability of acceptance. Explain fit in terms of the evidenced advance and audience. Preserve solid passages and defensible choices; a useful review need not manufacture weaknesses.

## Inspect the actual visuals

Render and view every in-scope figure page and every panel, using the available PDF/image tools. Inspect the whole arrangement and enough panel detail to read the evidence; enlarge where necessary and record when native resolution is sufficient. View at intended publication size when dimensions are known. Include Extended Data and relevant supplementary figures in a full review. Record file/page/panel and inspection status so skipped, unreadable, or unavailable images cannot masquerade as reviewed.

Apply [figures.md](references/figures.md): scientific encoding; axes, units, and scales; uncertainty and independent replication; visible data distribution; comparable conditions; image processing and provenance; panel order and cross-references; colour/accessibility and typography; legend completeness; and stage-appropriate technical delivery. When practical, make a visual-only pass before caption-assisted interpretation to expose missing labels; then reconcile both with Methods and claims. If the caption was already read, still distinguish observations in the pixels from information supplied by the caption. Ask whether the display supports the stated inference, not merely whether it looks polished.

Distinguish observations from suspicions. Similar patterns, a visible seam, or a compressed screenshot do not establish manipulation. Request originals/source data where needed. Do not alter research pixels, smooth traces, remove observations, regenerate evidence, or fabricate representative images to improve presentation.

## Edit for precision and disciplinary fluency

Only after the scientific audit, use the field dossier to assess structure, information order, terminology, qualification, tense, and voice. Replace vague or promotional phrasing with the actual finding **only when that finding is supplied and supported**. Preserve technical terms that carry meaning. Passive voice, first person, long sentences, and particular vocabulary are contextual choices, not automatic defects.

For each consequential sample edit, show original → proposed text → reason → any change in scientific meaning. Preserve numbers, entities, units, negation, time, population, uncertainty, causal strength, and citations. Mark an interpretation change for author verification. Do not identify AI authorship, score “AI likelihood,” imitate a named scientist, add deliberate errors, or disguise disclosure-relevant AI use.

## Deliver an actionable, bounded review

Use [review-report.md](assets/review-report.md) as a flexible scaffold, scaling it to the request. Include:

- Scope and coverage: materials actually inspected, live policy checks, field calibration, unavailable evidence.
- Overall assessment: contribution, substantiated strengths, principal scientific limitations, and bounded Nature fit.
- Prioritized findings with exact location, observed evidence, why it matters, smallest defensible remedy, and verification status. Label each as scientific concern, policy requirement, journal guidance, or optional editorial suggestion.
- Claim–evidence map; panel-level figure/legend audit; citation audit and coverage; a selective prose edit table when useful.
- Unresolved questions and a sequence of revisions, with substantive issues ahead of cosmetic ones.

Our priorities: **major** affects a central inference or essential reproducibility; **moderate** affects interpretation or an important local result; **minor** is a local clarity/presentation problem. **Needs verification** is a knowledge state, not a severity. Do not label a formatting preference a scientific flaw. In approved reviewer-support mode, adapt to the actual editor's questions; never submit a review or contact anyone unless separately authorized.

Before delivery, trace every high-impact finding to material you actually read or saw. Remove unsupported accusations and invented rules. Confirm proposed edits do not change scientific meaning silently. Report remaining limitations explicitly rather than declaring the paper “Nature-ready.”
