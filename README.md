# Nature Research Review

An evidence-grounded agent skill for reviewing research Articles intended for **Nature**, the flagship journal. It supports author-side manuscript review and critical reading of published papers, including actual figure inspection, scientific reasoning, citations, and field-specific prose.

This is an independent project, not affiliated with Nature or Springer Nature. The initial policy audit is dated **10 October 2026**. Journal rules can change; the skill requires live verification before prescribing a journal-specific correction. It makes no guarantee of correctness, acceptance, or exhaustive scientific validation.

## Use

```sh
npx skills add NeoVand/nature-review-skill --skill nature-research-review
```

To inspect discovery first, append `--list` to `npx skills add NeoVand/nature-review-skill`. The [official CLI](https://github.com/vercel-labs/skills) documents agent and installation-scope options.

Example request:

> Use $nature-research-review to review my Nature Article draft and all supplied figures. Research the conventions of this field first. Prioritize scientific validity, visual evidence, caption clarity, citation support, and precise prose. Give source-backed recommendations and proposed edits without changing my files.

The host needs web access for current policies and literature, document extraction for supplied formats, and the ability to render and view images for visual review. No paid scientific service, API key, or runtime script is required by this skill. If a capability or document is unavailable, the review explicitly records that gap.

## What it does

- Separates scientific concerns, journal requirements, journal guidance, and optional editorial preferences.
- Maps claims to methods and evidence; checks uncertainty, replication, reporting, and reproducibility.
- Inspects actual figures panel by panel, including scale, encoding, accessibility, image integrity, and caption consistency.
- Researches the specific field before judging prose. Removes vagueness and inflation while preserving scientific meaning; does not infer AI authorship or optimize for detector evasion.
- Verifies citation identity and claim support separately.
- Records contradictory official instructions instead of inventing a single answer.

Confidential manuscripts received as an appointed peer reviewer need a resolved, policy-compliant processing arrangement before ingestion. The skill does not replace a human reviewer's judgment or automatically submit reviews. Author-side work and public-paper critique are its primary use cases.

## Contents and audit

Start with [SKILL.md](skills/nature-research-review/SKILL.md). Its linked references contain the detailed procedures, journal profile, field/prose guidance, scientific checks, and figure review. [The source ledger](skills/nature-research-review/references/sources.json) travels with the installed skill.

[Research records](research/) preserve primary-source provenance and the [community-skill/distribution comparison](research/ecosystem-and-publication.md). [Validation](validation/) records structural checks, synthetic behavioral exercises, and known limitations. These checks increase reviewability; they do not certify scientific correctness.

The repository is structured for future separately researched journal profiles. **Science and other Nature Portfolio journals are not yet supported.** Do not apply this Nature profile to them unchanged.

## Maintenance

Policy changes and corrections should include the exact source, access date, journal/article/stage scope, revised claim, and behavioral regression example when appropriate. Keep requirements distinct from heuristics. Run `python3 scripts/validate_repository.py` after edits. The validator checks package structure and provenance links, not the truth of source content.

For distribution details and the distinction between publication, installs, and security scans, see [publication research](research/ecosystem-and-publication.md). skills.sh inclusion is driven by CLI install telemetry according to its [FAQ](https://www.skills.sh/docs/faq); no listing or audit result is implied merely by this README.

The skill is now [listed on skills.sh](https://skills.sh/neovand/nature-review-skill/nature-research-review). Its observed Snyk audit warns about indirect prompt-injection risk from external manuscript content. The skill explicitly treats such content as data, and a targeted regression exercise was completed; the warning is not represented as cleared. See [verified publication and audit status](validation/publication-status.md).

## License

Original skill instructions and repository tooling: MIT. Linked journal policies and research papers retain their own rights; this repository does not redistribute their full text or figures.
