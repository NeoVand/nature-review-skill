# Distribution status

Verified 2026-10-10 for the first public release of `NeoVand/nature-review-skill`.

| Check | Observed result |
|---|---|
| GitHub publication | [Repository](https://github.com/NeoVand/nature-review-skill) created under the authenticated NeoVand account; GitHub API confirms public visibility and `main` as default branch. |
| Discovery | Official skills CLI 1.7.2 found exactly one skill, `nature-research-review`. |
| Remote installation | Installed from GitHub into an isolated temporary project for Codex; no global installation was made. |
| Published update | CLI project update succeeded after the input-boundary revision, commit `00a5e04`. All ten installed skill files matched the repository package byte-for-byte. |
| skills.sh indexing | The [skill page](https://skills.sh/neovand/nature-review-skill/nature-research-review) returned HTTP 200 and displayed this skill, repository, and First Seen: Today. Its install-count field was a dash; no install total or leaderboard rank is claimed. |
| Security audit | The [Snyk audit page](https://skills.sh/neovand/nature-review-skill/nature-research-review/security/snyk) returned HTTP 200 and displayed **Warn**, risk level **MEDIUM**, code **W011**, dated 10 October 2026. The stated issue was external-content exposure through manuscript inputs, creating indirect prompt-injection risk. Other provider results were not displayed. |

The browser-search tool could not retrieve the new skills.sh page, so indexing and audit details were verified from the public HTML returned directly by HTTPS. Page content was inspected as data, not executed.

The warning is retained honestly. The entrypoint now explicitly rejects operational instructions embedded in documents and retrieved content; the targeted independent [regression exercise](injection-review-result.md) respected that boundary. This does not make external content inherently safe, prove immunity to prompt injection, or establish that Snyk rescanned the revised content. The latest observed external verdict remains **Warn**, not a clean audit claim. A security audit also does not validate scientific correctness.

Final tested skill-tree SHA-256: `26645488c65956a31208207e8e94334675bc20285d89b8d9b82ad3d279a8f04e`. This digest concatenates sorted relative file names, a NUL, file bytes, and a NUL for all ten installed files. Subsequent documentation-only commits do not change that tested skill package.

Commands used for the isolated installation and update:

```sh
npx --yes skills@1.7.2 add NeoVand/nature-review-skill --skill nature-research-review --agent codex --copy --yes
npx --yes skills@1.7.2 update nature-research-review -p --yes
```

The [official FAQ](https://www.skills.sh/docs/faq) describes install-telemetry discovery; the [API documentation](https://www.skills.sh/docs/api) describes automatic audits after first installation. No separate manual listing submission or fabricated installation activity was used.
