# Figure and legend review: Nature research Articles

Verified against the sources below on **2026-10-10**. This is a review protocol, not a Nature-issued checklist. Re-open relevant official pages before declaring a submission noncompliant. A named editor's current manuscript-specific instructions take precedence over generic preparation advice. Do not transfer rules from Nature Communications, Nature Methods, Scientific Reports or Nature Reviews to the flagship journal.

Labels used here: **Requirement** = explicit journal instruction within its stated scope; **Guidance** = a journal preference or external recommendation; **Heuristic** = this skill's proposed review procedure, not a journal rule. A useful question is not evidence that the manuscript has a defect.

## 1. Establish what can actually be reviewed

**Heuristic.** Inventory every main and Extended Data figure and its panels; reconcile that inventory with the manuscript's calls and legends. Record the exact document version, page, figure/panel identifiers, available source-data files, and whether editable artwork, raw images and plotting code were supplied. Include tables containing figure-like graphics. Do not silently omit Extended Data.

Use this evidence hierarchy:

| Available material | Permitted assessment | Limit to state |
| --- | --- | --- |
| Legends/text only | Terminology, reported quantities, internal consistency and missing definitions | No visual review performed |
| Rendered manuscript pages | Layout, visible labels, correspondence to caption, apparent patterns | Limited by embedded resolution and page rendering |
| Original exported figure | Detailed visible content and file properties actually inspected | Does not establish raw-data provenance |
| Raw images/source data/code | Traceable checks of selected reported quantities and processing | State which checks ran; no blanket authenticity guarantee |

**Heuristic.** Actually inspect pixels. Read each complete figure at an overview scale, at its intended reproduction size when determinable, and in enlarged panel views. Use enlargement for inspection, not as evidence that a figure is readable in print. If page scale is unknown, say so; do not report measured font sizes from an arbitrary screenshot. Record the rendering/viewing method and failed or unavailable panels. OCR can support label extraction but does not replace visual inspection.

**Stage distinction.** Initial-submission figures need sufficient resolution for assessment; production files are deferred. [F01] Treat formatting refinements as stage-specific tasks; treat obscured evidence as a scientific communication problem at any stage.

## 2. Map each panel to the claim

**Heuristic.** Complete a panel record before proposing changes:

```text
Figure/panel and source page:
Panel type: observation / quantitative analysis / simulation / schematic / other
Question or comparison:
Manuscript claim, quoted briefly or located precisely:
What is visibly shown:
What the legend says is shown:
Experimental/observational unit and denominator, if known:
Uncertainty/test/selection information, if applicable:
Source-data or raw-image pointer:
Checks completed and unavailable:
Issue + consequence + smallest defensible repair:
Basis: requirement / guidance / heuristic; source ID:
Status: observed issue / no issue observed in this check / not applicable / unassessable
```

**Heuristic.** Test the claim against the panel, rather than judging attractiveness. Can a reader identify the comparison without searching unrelated pages? Is a model prediction presented as a prediction? Is a mechanistic cartoon clearly distinguished from measured evidence? Does a claim about a population rely only on a selected example? Can main findings be followed while keeping essential controls and qualifications visible? Suggest moving or combining panels only after explaining what understanding improves and what evidence remains accessible. Never infer that an attractive figure establishes novelty or validity.

**Heuristic.** Compare panel order with the argument. Give each panel a reason to exist. Check whether panel lettering, group order and visual keys remain stable across the paper. Prioritize wrong mappings and missing evidence before spacing and cosmetic changes. Do not impose a fixed number of panels or a universal visual narrative.

## 3. Inspect every quantitative display

These are **heuristics** unless linked to a specific requirement below. Apply only relevant questions.

- **Identity and axes:** Transcribe the measured quantity, unit, transformation, scale and denominator. Verify axis direction, tick spacing, limits and any break. Check that percentages, ratios, normalized values and arbitrary units are explained. Inspect shared axes for hidden exceptions. A nonzero baseline is not automatically wrong; assess what comparison the visual encoding invites, and justify any proposed change.
- **Data marks:** Identify what each point, line, box, band, cell or symbol represents. Count visible observations only when resolvable; overlapping marks are not a reliable sample-size audit. Check whether lines imply an order, trajectory or pairing actually present in the design.
- **Comparability:** Inspect whether panels intended for comparison share compatible units, normalization, scales, binning and colour ranges. Flag unexplained differences; do not force identical scales when that would erase necessary detail.
- **Uncertainty:** Match every error bar and band to its definition. Distinguish spread, uncertainty in an estimate, prediction intervals and model variability using the authors' methods. Do not infer statistical significance by eye from interval overlap. If the uncertainty type is missing, request its definition instead of guessing. The error-bar literature explicitly warns against casual interpretations of overlap. [F15]
- **Inference:** Match each comparison bracket, symbol and reported probability to the tested groups. Trace corrections, repeated observations and hierarchical structure to the analysis description. Flag discrepancies for statistical review; do not change tests or recalculate from a picture.
- **Plot-specific definitions:** For a box plot, locate definitions of centre, box, whiskers and additional points. For a violin/density plot, ask about sample size and smoothing when interpretation depends on them. For binned plots, identify bin definitions. For fitted curves, distinguish observations, fit, extrapolation and uncertainty. For heatmaps, identify ordering, normalization and missing-value encoding.
- **Claim strength:** Ask whether the display supports direction, magnitude, precision, heterogeneity and scope of the stated effect. Check whether excluded groups, absent controls or omitted ranges are explained. Preserve null, negative and uncertain results in proposed revisions.

**External guidance.** For small continuous datasets, consider showing observations and, for paired designs, the pairing: different underlying datasets can yield similar summaries. This recommendation comes from a physiology-focused study and examples, not a Nature-wide prohibition of bars or line graphs. [F10]

**Reporting requirement, applicable fields.** Apply the statistical items in [rigor-and-reporting.md](rigor-and-reporting.md) and the live form. Its Statistics section allows information across legends, tables, text or Methods. [F09] Do not demand every item in every caption. Nature separately requires error-bar and statistical definitions in figure legends. [F02]

**Heuristic.** Build a small statistics crosswalk: `panel → plotted unit → n → source of n → estimate → interval → comparison/test → Methods location`. If a legend says `n=12`, determine whether this means participants, animals, cultures, fields, cells, simulations or repetitions. Keep uncertainty explicit until the author supplies the answer.

## 4. Inspect image-based evidence and provenance

**Nature integrity requirements.** Document acquisition and processing. Whole-image adjustments must treat controls equally and preserve information. Disclose nonlinear processing and relevant channel changes. Demarcate composites and lane rearrangements. Loading controls belong on the same blot; identify separately run sample-processing controls. Life-science final submissions require original unprocessed gels/western blots. [F07]

**Figure-guide requirements.** Label intentional panel reuse; mark splice boundaries; preserve uncropped gel originals. Do not erase bands or selectively alter their intensities. The guide prohibits generative AI in figures, including content-aware editing. [F08] Treat this as covering diagrams and schematics too; do not assume an exemption or generate research figures without an explicit editor-permitted workflow.

**Heuristic.** Work from observation to query, never directly to accusation:

1. Locate the exact region and describe the visible feature without assigning intent.
2. Compare supplied panels and originals for the particular concern; record which versions were compared.
3. Consider disclosed reuse, shared controls, adjacent fields, rendering/compression artefacts and legitimate processing before escalating.
4. Request the relevant raw file, acquisition metadata or processing history when necessary. Preserve originals and record any inspection transformation.
5. Report unresolved concern and confidence separately. Visual similarity alone does not establish fabrication, misconduct or AI origin. An unremarkable visual scan does not authenticate the data.

**Heuristic questions for microscopy and other spatial images:** Can the specimen, condition, channel and orientation be identified? Are scale bars consistent with supplied calibration and resizing? Is an inset traceable to the marked region? Does an overlay obscure the feature on which the claim relies? Are acquisition depth/time, projection or reconstruction explained when relevant? Is a selected example linked to quantified measurements and the selection procedure? Do comparisons depend on colour or contrast changes whose provenance is unavailable?

**External microscopy guidance.** Keep aspect ratio, identify inset locations, and avoid presenting a curated example as the full observed range. [F12] Label channels; assess clipping and consistency of display settings; consider separate grayscale channels and a calibrated intensity key when these clarify the evidence. [F13] These are community recommendations, not universal instructions to recolour images or replace the author's processing. Request the source data and author confirmation before any transformation affecting interpretation.

**Specialist handoff heuristic.** For chemical structures, spectra, cryo-EM/crystallography, flow cytometry, maps, astronomical images, phylogenies, electrophysiology, clinical imaging or computational benchmarks, first identify and read the relevant current journal/discipline guidance. Keep an explicit list of unresolved checks (for example, structure validation, gating, coordinate systems, calibration, leakage or baseline fairness). Do not fabricate a field-specific threshold or declare specialist validity from this general checklist.

## 5. Evaluate readability and production readiness

**Figure specifications.** Nature asks for labelled axes with units and ticks, an accessible palette and editable lettering. Standard sans-serif text is 5–7 pt; lowercase panel letters are 8 pt, bold and upright. Scale bars should remain editable and replace magnification factors. RGB is recommended. Resolution instructions conflict; see below. [F04]

**Layout guidance.** The dedicated guide gives 89/183 mm print widths and 170 mm maximum height, subject to production decisions. It recommends logical panel order and distinct, accessible colours, avoiding red–green contrasts and rainbow scales; use keys rather than coloured prose. [F05] Numeric dimensions are not proof of readability: inspect the actual export.

**Heuristic.** Record whether each problem is visible in the provided artifact or depends on an unavailable production file. Check cropped labels, colliding annotations, ambiguous symbols, inconsistent precision, missing minus signs, illegible subscripts, tiny inset axes, obscured data and stale panel references. Inspect grayscale and colour-vision-deficiency simulations when available; record the method and limitations. Do not certify universal accessibility from a single simulation or a palette name.

**External colour guidance.** Match colour encoding to the quantity: continuous order, a meaningful central reference or a cyclic variable need different treatment. Include the scale; assess perceptual ordering and avoid colour-created boundaries unsupported by data. [F11] This does not justify recolouring a source image without understanding what its channels represent.

**Heuristic.** For file checks, inspect native properties when tools allow: dimensions, effective raster resolution at placed size, editable text, vector/raster components, embedded fonts and linked assets. A PDF extension does not prove that its content is vector or editable. Upsampling is not evidence of additional measured detail. Keep editable originals even when a delivery copy must be flattened. Re-render any revised file and recheck labels and scientific content against the original.

**Extended Data specifications.** The dedicated guide allows ten display items (figures and tables combined), calls for individual JPEG/TIFF/EPS files, a 10 MB limit, and maximum page dimensions of 180 × 170 mm. It normally keeps each item with its legend on one page, permitting exceptional legend overflow for legibility. [F06] The export guide specifies RGB and a maximum 300 dpi for these files. [F05] Do not apply main-figure resolution instructions indiscriminately to Extended Data.

## 6. Review and, if requested, repair each legend

**Caption guidance.** Begin with a brief figure title, then describe what is displayed; make the figure intelligible independently. [F01] Keep procedures in Methods while retaining the definitions needed to interpret this display. **Heuristic:** use the structure below only for applicable elements; never fill missing facts with plausible values.

```text
Figure [number] | [Concise, evidence-matched title].
[Panel labels], [specimen/system; comparison; quantity displayed].
[Meaning of points, lines, colours, symbols, scale bars and abbreviations].
[Known sample counts with their units; pairing/repetition where relevant].
[Known summary and uncertainty definitions; relevant comparison/test details].
[Necessary selection/processing/reuse disclosure; precise Methods/source-data pointer].
```

**Heuristic.** Read the legend once without the main text, then read it against the pixels and the Methods. Check every panel letter, group name, time, dose, unit, denominator, count, sign, numerical result and abbreviation. Distinguish `not reported` from `reported elsewhere` and cite that location. Check whether a title overstates the displayed evidence. Do not write “representative” without knowing what was sampled, how examples were selected and what replication is documented.

**Heuristic.** If rewriting is requested, preserve scientific commitments, numerical values and citations; leave explicit author queries for missing facts. Put essential interpretation definitions ahead of optional prose. Explain any deletion or relocation. A shorter legend is not better if it hides necessary uncertainty, provenance or design information.

## 7. Preserve live-source disagreements

The following were unresolved on the verification date. They are **not grounds for a categorical failure**. Recheck the linked sections and any editor instructions before final preparation.

| Topic | Observed disagreement | Working action, explicitly our judgement |
| --- | --- | --- |
| Legend length | Initial: <250 words [F01]; formatting: <300 [F02] | Aim below 250 if complete; flag 250–299 as conflicting guidance, not an unambiguous violation. |
| Print widths | Initial: 90/180 mm [F01]; dedicated guide: 89/183 mm [F05] | Use dedicated-guide dimensions provisionally; do not fail near-equivalent draft widths. |
| Main artwork formats | Dedicated guide rejects flattened JPEG/TIFF/PNG main figures [F05]; final page accepts some raster formats [F03] | Prefer editable vector containers with appropriate raster image components; verify an unusual delivery format with production. |
| Main-image resolution | F04 Image resolution says minimum 300 dpi; its Exporting section says minimum 450 dpi. | Retain both instructions. If genuine source resolution permits, 450 dpi at placed size meets both; do not upsample to claim compliance. Verify final production requirements. |
| Extended Data dimensions | Dedicated: 180 × 170 mm page [F06]; final: 180 × 240 mm page [F03] | An artwork-versus-page distinction might explain the discrepancy, but is unverified. Preserve legend space and request production clarification for the final layout. |
| Microscopy composites | An isolated microscopy instruction conflicts with the surrounding composite-disclosure policy [F07] | Never recommend silently combining fields; retain boundaries and provenance, and request clarification if necessary. |

**Heuristic.** For AI-related figure questions, check the dedicated figure-integrity guidance [F08] alongside the current portfolio AI policy and any editorial direction. Do not treat permission for language assistance as permission to generate or reconstruct research imagery. Do not apply remembered historical exceptions as current policy.

## 8. Deliver an auditable review

**Heuristic.** Return a complete coverage table and a prioritized issue list. Each issue needs: exact figure/panel location; observed evidence; scientific or readability consequence; smallest repair; whether it is required, recommended or discretionary; source and confidence; and what remains unassessable. Separate a possible integrity concern from a confirmed mismatch. Avoid aggregate “figure quality scores” that imply validated measurement.

Example of appropriate specificity: `Fig. 2c, y-axis: label shows %, legend describes a fraction. Resolve the unit and check the plotted values against source data; current materials do not establish which is correct.` Do not silently multiply values or relabel the axis.

Close with the checks actually completed, unavailable inputs, and any specialist questions. Never write “all figures verified” when only legends, thumbnails or selected panels were reviewed.

## Source index

Precise source sections, access status and audit notes are recorded in the installed [source ledger](sources.json), with the original audit in the repository's `research/figure-sources.json`.

- **F01** [Nature — Initial submission](https://www.nature.com/nature/for-authors/initial-submission), Figures.
- **F02** [Nature — Formatting guide](https://www.nature.com/nature/for-authors/formatting-guide), Figure legends.
- **F03** [Nature — Final submission](https://www.nature.com/nature/for-authors/final-submission), Electronic image formats; Extended data display items.
- **F04** [Preparing figures — our specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/), Graphs; Images; Font choices.
- **F05** [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/), Figure sizing; Accessibility; Accepted formats.
- **F06** [Extended data formatting guidelines](https://research-figure-guide.nature.com/figures/extended-data-formatting-guidelines/), Figure sizing & positioning; File formats.
- **F07** [Nature — Image integrity and standards](https://www.nature.com/nature/editorial-policies/image-integrity), main policy; Electrophoretic gels and blots; Microscopy.
- **F08** [Figure guide — Image Integrity](https://research-figure-guide.nature.com/figures/image-integrity/), Preparing images; Photoshop; Gels.
- **F09** [Nature Portfolio Reporting Summary, flattened reference copy](https://www.nature.com/documents/nr-reporting-summary-flat.pdf), page 1, Statistics (retrieved title: August 2023 extended version).
- **F10** Weissgerber et al. (2015), [Beyond Bar and Line Graphs](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128), introduction, Figs. 1–2 and recommendations.
- **F11** Crameri et al. (2020), [The misuse of colour in science communication](https://www.nature.com/articles/s41467-020-19160-7), colour-map classes and Figs. 5–6.
- **F12** QUAREP-LiMi WG12, [Image format](https://quarep-limi.github.io/WG12_checklists_for_image_publishing/image_publishing/1_image_format.html), minimal checks.
- **F13** QUAREP-LiMi WG12, [Image colors and channels](https://quarep-limi.github.io/WG12_checklists_for_image_publishing/image_publishing/2_image_colors_channels.html), minimal/recommended checks.
- **F14** Schmied et al. (2023 online; 2024 volume), [Community-developed checklists for publishing images and image analyses](https://www.nature.com/articles/s41592-023-01987-9), Data availability links to the companion resource used for F12–F13; the article's subscription-only body was not relied on.
- **F15** Krzywinski and Altman (2013), [Error bars](https://www.nature.com/articles/nmeth.2659), publicly visible standfirst; no claim here depends on its subscription-only body.
