# Prior art and distribution research

Checked 2026-10-10. Community skills informed the design review; they are not evidence for journal or scientific requirements. No third-party skill text or code is bundled.

## Existing review skills

| Resource inspected | Public popularity observation | Useful design ideas / limits |
|---|---|---|
| [K-Dense peer-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md), version 2.4; [scientific-writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md), version 2.3 | GitHub API returned 48,279 stars for the whole repository, not these individual skills. The former claude-scientific-skills URL redirects to scientific-agent-skills. | Evidence-bounded findings, separate human accountability, and explicit verification states are useful. Its broad scientific remit and optional tools are not a substitute for a current flagship Nature profile. We did not adopt its external-product suggestions or import its code. |
| [GuangyaoYin scientific-manuscript-review](https://github.com/GuangyaoYin/skill-scientific-manuscript-review/blob/main/SKILL.md) | GitHub API returned 4 stars; license metadata was null. | Claim-to-evidence tables and revision assessment are useful. Its bilingual Word-report defaults and field emphasis are not requirements for this skill. Do not ask a user for their preferred scientific verdict or inherit fixed recommendation rules. |
| [wentorai paper-review-skills directory entry](https://www.skills.sh/wentorai/research-plugins/paper-review-skills) | skills.sh displayed 197 installs and 298 repository stars. | Demonstrates task routing across critique, reading, responses, and review writing. This entry is a router, not direct evidence that an individual review procedure works. |

Counts are dated observations, not quality measures, independent users, clinical/scientific validation, or a ranking of accuracy. Direct K-Dense peer-review skills.sh pages were inaccessible in this research session, so no install count is claimed for that skill. Search results exposed many copies/forks; their counts were not aggregated.

## Packaging

The [Agent Skills specification](https://agentskills.io/specification) defines a skill folder with `SKILL.md`, including `name` and `description` YAML fields. Supporting references can be loaded as needed. Our folder name matches the skill name; all runtime references stay inside the installable folder. The repository contains one skill under `skills/` so later journal profiles can be independently added.

The [official skills CLI README](https://github.com/vercel-labs/skills) documents selecting a skill, selecting an agent, and `--list` for discovery without installation. Its [discovery implementation](https://github.com/vercel-labs/skills/blob/main/src/skills.ts) searches the `skills/` container. No registry manifest or root-level duplicate `SKILL.md` is needed for this layout.

## Publishing and skills.sh

The [skills.sh FAQ](https://www.skills.sh/docs/faq) says skills are hosted on GitHub and leaderboard inclusion follows CLI installation telemetry. Therefore the publication path is a public repository with a discoverable skill plus an honest install command, not an npm package or a manual leaderboard submission. The [CLI documentation](https://www.skills.sh/docs/cli) describes telemetry and its opt-out. Do not fabricate installs or equate `--list` with an installation.

The [skills.sh API reference](https://www.skills.sh/docs/api), section “Get security audit results,” says audits follow the first installation and can be delayed. A repository push, successful discovery, leaderboard presence, and security-audit completion are distinct events. Security audits assess security; they do not validate Nature advice or scientific correctness. Report only observed status.

Commands for users, run from the project where the skill should be available:

```sh
npx skills add NeoVand/nature-review-skill --list
npx skills add NeoVand/nature-review-skill --skill nature-research-review
```

For Codex-specific installation, the CLI supports adding `--agent codex`. Use `--global` only when the user wants installation across projects. No global install is necessary to publish this repository.

## Verification approach

Before publication: check skill metadata, resolve all relative paths, validate source identifiers, inspect the staged file list, and run independent synthetic review exercises. After publication: verify the public repository and remote commit, run real CLI discovery, and distinguish distribution checks from the source audit. Any installation smoke test belongs in an isolated temporary project, not a user's research repository.
