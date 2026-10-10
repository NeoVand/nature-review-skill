# Field calibration and precise scientific prose

Evidence checked 2026-10-10. Evidence identifiers resolve in `sources.json`. The field-dossier procedure, editing tests and examples below are **skill heuristics**, not Nature requirements or a validated authorship detector.

## Purpose: improve the writing without changing the science

Nature asks for clear, simple prose accessible across disciplines, explained specialist terminology and restrained abbreviation. This is especially relevant to titles and summary paragraphs. [N01](https://www.nature.com/nature/for-authors/formatting-guide)

Translate “a seasoned field expert's voice” into operational goals: correct terminology, explicit evidence, calibrated inference and economical explanation. Do not impersonate a named scientist, add prestige vocabulary, make unsupported certainty sound authoritative, or impose a single prose rhythm on every discipline. Preserve intelligible author choices. Correctness outranks elegance.

## 1. Build a field dossier before making stylistic judgments

**Skill procedure.** Use public material and generic topic/method queries where confidentiality is relevant. For a full review, normally inspect 3–5 recent, closely matched research Articles from Nature, spanning more than one research group when available, plus 1–3 primary methods or foundational papers relevant to the actual inference. These counts and a starting recency window of roughly three years are practical defaults, not evidence-based thresholds. Expand the window or use specialist-journal primary papers when necessary; label the change and its reason.

Select by research question, design, evidence type and audience. Do not select solely by citations, publicity or stylistic polish. Search results, abstracts and press releases cannot establish a full-text convention. Confirm the journal is Nature, the document type is Article, publication status and version, and any correction/retraction before treating it as an exemplar. Supplementary methods and transparent-review files, where public, can clarify expectations; they do not reveal every editorial consideration.

Record this dossier before editing:

| Dossier item | What to record |
| --- | --- |
| Scientific scope | Subfield, research question, evidence type, intended audience and limits of reviewer expertise |
| Search trail | Queries, date, inclusion/exclusion reasons, access limits and stopped searches |
| Source identity | Title, DOI/URL, journal, article type, online date, version/correction state and sections inspected |
| Epistemic conventions | What is measured, inferred, predicted or assumed; what supports the field's causal/mechanistic language |
| Terminology | Names, symbols, units, acronyms and distinctions that carry scientific meaning |
| Argument structure | How context becomes a question, how each result answers it, and where limits are stated |
| Prose observations | A small number of patterns, each located in more than one source when possible; exceptions and uncertainty |
| Methods evidence | Primary source for any methodological objection; why it applies to this design |

Synthesize a short voice specification: audience; preferred concrete nouns and verbs; conventions for uncertainty; distinctions to preserve; optional opportunities for clarity. State “observed in this sample” rather than “Nature requires” for exemplar-derived patterns. If the field cannot be researched adequately, restrict edits to transparent ambiguities and report the limitation. Do not invent the missing expertise.

### Two audited illustrations, not universal templates

- **Computational regulatory genomics:** AlphaGenome's Nature Article separates genome-track prediction from variant-effect evaluations, and its Discussion identifies domain limitations, including species coverage and untested personal-genome prediction. A useful editing inference is to preserve the exact prediction task, benchmark and domain of validity; broad claims about understanding biology need separate scrutiny. This is an observation about one Article, not a statement about all genomics prose. [R14](https://www.nature.com/articles/s41586-025-10014-0)
- **Experimental quantum information:** the Willow Article defines a measured error-suppression quantity and distinguishes achieved quantum-memory performance from conditional scaling to computation. A useful editing inference is to preserve operational definitions, uncertainty and the difference between measurement and extrapolation. Its online publication was 9 December 2024 and its issue year 2025. [R15](https://www.nature.com/articles/s41586-024-08449-y)

The Willow paper's April 2026 correction fixed Fig. 3a labels. Even a published exemplar needs version checking. [R16](https://www.nature.com/articles/s41586-026-10559-8) These examples demonstrate a calibration method; they are not a ready-made dossier for an unrelated manuscript or evidence of AI authorship.

## 2. Diagnose observable writing problems, never a person's provenance

Liang and colleagues found false positives affecting non-native-English essays in a 2023 evaluation of seven detectors; Weber-Wulff and colleagues documented reliability limitations in the tools and texts they tested. These results concern particular systems, samples and dates. [R09](https://doi.org/10.1016/j.patter.2023.100779), [R10](https://doi.org/10.1007/s40979-023-00146-z)

Evidence is context-dependent: the abstract of a 2026 Czech-language study reports no systematic native/non-native bias in its tested detector families. Only its abstract and metadata were checked here; that does not validate a detector for an individual Nature manuscript. [R11](https://arxiv.org/abs/2602.05769)

**Skill rule:** do not diagnose AI authorship from vocabulary, punctuation, fluency, repetition, sentence length, a detector score or an intuition. Do not assign an “AI probability,” accuse the author, infer native language, or label standard field terminology as a tell. Do not claim that detection is mathematically impossible or that every detector has the same bias. The task is scientific and editorial review, not provenance adjudication.

“Unslopification” in this skill means an optional pass for the concrete issues below, regardless of who or what produced the text:

| Observable issue | Evidence needed before changing it | Minimal editing action |
| --- | --- | --- |
| A broad claim has no identifiable referent | Locate the claimed object, comparison or evidence | Name it if supplied; otherwise ask what the claim means |
| Promotion replaces a result | Match the adjective to measurements and scope | State the supported finding or remove unnecessary emphasis |
| Several sentences repeat one point | Verify that they do not encode different limits or populations | Consolidate without losing distinctions |
| A transition asserts an unsupported logical relation | Check whether the next sentence is evidence, contrast, cause or speculation | Use a justified relation or remove the transition |
| Abstract nouns obscure the operation | Identify the actual entity, action and measurement | Express the operation directly without inventing an actor |
| References decorate an overbroad statement | Read the cited primary evidence | Narrow the claim, split it, or request the needed source |
| A generic future-work paragraph adds no scientific constraint | Identify the unresolved question and its consequence | Make the limitation concrete or suggest deletion |
| Repetitive scaffolding delays the result | Confirm it is not needed for method/argument navigation | Shorten locally; keep necessary signposting |

No forbidden-word list, forced sentence-length variation, filler anecdotes, deliberate errors, thesaurus substitutions or detector-evasion targets. A commonplace phrase can be precise in context; an unusual phrase can be wrong. Treat any pattern as an invitation to inspect meaning.

## 3. Protect meaning during every edit

Create a protected-facts checklist for the passage before rewriting:

- Claim type and strength; negation; alternatives; uncertainty and qualifiers.
- Population, organism, sample, condition, time point and experimental setting.
- Entity names, symbols, equations, gene/protein nomenclature and abbreviations.
- All numbers, signs, scales, units, denominators, reference categories and rounding.
- The definition of n, replicate independence, repeated observations and exclusions.
- Effect/uncertainty types, tests, P values, thresholds and multiplicity adjustments.
- Observation versus prediction/simulation; association versus mechanism/causation.
- Citations, figure/panel references, and claim-to-evidence attachment.

Use `original → suggested edit → reason → meaning check → author question (if needed)`. An edit that needs a new fact stays a question or visibly marked placeholder; do not fill it with a plausible answer. A change in scientific interpretation is a substantive recommendation requiring explicit human review, not a silent language edit.

Use active voice when it clarifies the actor and passive voice when the measured object or procedure should remain the topic. Do not mechanically ban either. Preserve precise repeated terms when synonyms would imply different entities. Keep field-specific technical language when necessary and explain it at the appropriate reader-facing point. Do not convert a cautious claim into a strong one merely to sound experienced.

### Synthetic examples of safe boundaries

These invented examples illustrate the procedure; they are not quotes from published papers.

| Original | Appropriate review action | Why |
| --- | --- | --- |
| “These remarkable results show that treatment improves survival.” | Ask for design, effect estimate, uncertainty and supported causal interpretation; optionally remove “remarkable.” | Removing emphasis is stylistic; certifying a treatment effect requires scientific evidence. |
| “Expression was associated with outcome after adjustment for age.” | Retain the association and adjustment; do not replace with “expression determined outcome.” | The replacement changes the inference. |
| “We measured 120 cells from three donors.” | Preserve both counts and ask which unit supports each analysis. | “n = 120 independent samples” would invent independence. |
| “The method was highly accurate.” | Request the metric, evaluation set and comparison; use only values already documented. | Specificity must come from evidence. |
| “The result was not significant.” | Ask which test and uncertainty are meant; do not rewrite as “there was no effect.” | Those statements are not interchangeable. |
| “At fixed temperature, the simulations predict a transition.” | Retain the condition and predictive status. | “We observed a transition” could misrepresent computation as observation. |

## 4. Relate prose to sections without manufacturing a formula

Use the Nature profile for actual section and format rules. The following are **editing questions**, not additional required sections:

- **Title and summary:** can an adjacent-field scientist identify the question, evidence and supported advance? Is every strong claim also supported in the main paper? Avoid broadening scope to make the work sound important.
- **Opening/context:** does the reader understand the established knowledge, unresolved issue and why this design addresses it? Distinguish a narrow technical gap from a broad scientific gap. Verify claims about what prior work could not do.
- **Results:** can each paragraph be linked to a question, method/comparison, result and proportionate interpretation? Preserve the distinction between directly shown evidence and inference. An explanatory clause can be useful; do not rigidly demand identical paragraph templates.
- **Discussion/closing:** are synthesis, alternative explanations, limitations and implications proportionate to the evidence? Distinguish immediate use from a future possibility. Do not remove scientifically important uncertainty to gain narrative momentum.
- **Methods:** can a relevant expert understand what was done and how choices affect inference? Concision must not erase reproducibility details. Do not invent standard-method steps that the authors have not reported.
- **Captions:** preserve the panel's actual experiment, units, n and uncertainty. Cross-check edits against the visible figure and source data; do not improve readability by stripping the information needed to interpret it.
- **References:** keep citations attached to the specific claims they support. Verify primary sources, versions and actual content; do not add a fashionable or famous citation merely to signal expertise.

Finish the pass with a semantic diff. Separate corrections needed for accuracy, suggestions for clarity, and optional voice preferences. Show a small representative set before proposing a wholesale rewrite unless the user explicitly requested full editing. If the original already communicates the science well, say so and preserve it.
