<a href="https://christopherqueenconsulting.com/?utm_source=github&utm_medium=org_profile">
<picture>
  <source media="(max-width: 760px) and (prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-phone-dark.svg">
  <source media="(max-width: 760px)" srcset="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-phone-light.svg">
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-dark-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-light-static.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-dark.svg">
  <img alt="Christopher Queen Consulting home page. Applied AI that holds up in production. A timeline drawn to scale: a one-week audit for $1,500, then days 1 to 30 of a build priced in a written spec ($5,000 for the sample scope), then a written hand-off of the code and evals on day 31." src="https://raw.githubusercontent.com/christopherqueenconsulting/.github/main/profile/assets/hero-light.svg" width="100%">
</picture>
</a>

**Christopher Queen Consulting (CQC) builds LLM, RAG and agent features that keep working after launch, and puts the checks that prove it in your repo.** It is for engineering leaders and seed to Series B founders who need these features without hiring an ML team. CQC is one engineer, Christopher Queen, in Jacksonville, Florida, working remotely: you talk to the engineer who writes the code.

**[Book a free 30-minute call](https://christopherqueenconsulting.com/schedule/?utm_source=github&utm_medium=org_profile)**

Or read about [the audit](https://christopherqueenconsulting.com/ai-ops-audit/?utm_source=github&utm_medium=org_profile) and [the 30-day build](https://build.christopherqueenconsulting.com/?utm_source=github&utm_medium=org_profile) first.

## Two ways to start

### The audit: one week, $1,500

- **What it is:** your LLM spend and failures, traced and graded.
- **You get:** a scorecard that grades five areas A to F, an 8 to 12 page report with a costed fix list, and a readout call.
- **You keep:** the fix list, written so your team can act on it without CQC.
- **Access:** read-only, to your LLM logs and bills, under your NDA.

### The 30-day build: priced in a written spec

- **What it is:** one working system, built in your repo over 30 days.
- **Price:** set in a written spec before day 1. The sample scope, an agent eval harness, is $5,000.
- **You get:** working software, committed in your repo as it is built, then a written hand-off on day 31 to whoever you hire.
- **You keep:** the code, which the agreement assigns to you, and the evals.
- **If the scope changes:** a new spec is written. No invoice arrives mid-build.

## Where LLM features break, and the check that catches it

These three checks run in public repos today. Each number comes with its limits.

**A model grades work, and no hard check backs the grade.** In [CPCC Task Automation #267](https://github.com/christopherqueenconsulting/cpcc_task_automation/pull/267), a real compiler now decides whether code compiles before the model's score counts. If the compiler cannot run, the result is "cannot verify", never a fail. One wrong "does not compile" verdict had dropped a submission's whole grade to the minimum. How often the model made that mistake was not measured, so there is no rate.

**A release waits undeployed, and nobody is told.** In [LinkedIn Engagement Manager #2194](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/pull/2194), a classifier sorts each database migration. Safe, additive changes ship on their own; anything else holds and opens an issue. An hourly check alerts when a release has waited more than 3 hours. Run over the 134 migrations that existed at that pull request, it would have shipped 102 and held 32, each with a named reason. The classifier has 68 tests.

**A scheduled job runs green and produces nothing.** In [Panthera #66](https://github.com/gitchrisqueen/panthera/pull/66), a daily health check scores each finished day and opens an issue for a dead one. It flags a dead day the next morning, about 26 hours later at the earliest. Its threshold was set on past data, not held out.

Sources and fuller caveats for all three: [the project write-ups](https://github.com/gitchrisqueen/gitchrisqueen/blob/main/docs/PROOF.md).

## Code you can read

- **[LinkedIn Engagement Manager (LEM)](https://github.com/christopherqueenconsulting/linkedin_engagement_manager)**: a live web app for LinkedIn content and engagement (FastAPI, Celery, Redis, MySQL, React, Docker). Its write-up lists its limits: deployed and CI-gated, no revenue.
- **[CPCC Task Automation (CPCC)](https://github.com/christopherqueenconsulting/cpcc_task_automation)**: grading and admin automation built by its author for his own college courses. Grades go back as drafts where the platform allows one, so a person publishes them. Its write-up says he is its only user.

Two more live on the founder's personal GitHub account, as does Panthera above:

- **[cqc](https://github.com/gitchrisqueen/cqc)**: a small command-line tool that serves these checks as Model Context Protocol (MCP) tools.
- **[litellm-complexity-router](https://github.com/gitchrisqueen/litellm-complexity-router)**: a public extract of a model router that scores a prompt and picks a model tier, with evals and a labelled 120-row set.

LEM runs its deploy drift check hourly and its prompt evals weekly. CPCC runs its prompt evaluation when prompts change. The other checks run on every change. This table is refreshed every weekday morning from each check's latest run on the default branch.

<!-- CI-STATUS:START -->
| Check | Latest result |
| --- | --- |
| [LEM unit tests](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/workflows/unit-tests.yml) | [passed, 2026-11-17](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/runs/44137889679) |
| [LEM deploy drift check](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/workflows/deploy-drift-check.yml) | [passed, 2026-11-17](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/runs/44137161396) |
| [LEM prompt evals](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/workflows/prompt-evals.yml) | [passed, 2026-11-16](https://github.com/christopherqueenconsulting/linkedin_engagement_manager/actions/runs/43802015461) |
| [CPCC test suite](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/workflows/unit-tests.yml) | [passed, 2026-11-17](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/runs/44131169358) |
| [CPCC prompt evaluation](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/workflows/prompt-eval.yml) | [passed, 2026-11-17](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/runs/44131169955) |
| [CPCC PII guard](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/workflows/pii-guard.yml) | [passed, 2026-11-17](https://github.com/christopherqueenconsulting/cpcc_task_automation/actions/runs/44131168894) |
<!-- CI-STATUS:END -->

## Before you book

CQC has no published client engagement yet, and the [build page](https://build.christopherqueenconsulting.com/?utm_source=github&utm_medium=org_profile) says plainly that you would be the first build client at its price. The proof above is CQC's own running systems. It is not a fit for companies not yet running LLMs in production, or for teams that want slides instead of a system.

## Fixes merged upstream

Small fixes to tools CQC builds on, merged by each project's maintainers:

- [langchain-ai/langchain #15251](https://github.com/langchain-ai/langchain/pull/15251): fixes LangChain's dev container build.
- [PostHog/posthog-openclaw #15](https://github.com/PostHog/posthog-openclaw/pull/15) and [#35](https://github.com/PostHog/posthog-openclaw/pull/35): PostHog's LLM analytics plugin for OpenClaw reads its API key and host from environment variables when the config has none.
- [taylorwilsdon/google_workspace_mcp #644](https://github.com/taylorwilsdon/google_workspace_mcp/pull/644): the Google Workspace MCP server reads the Google account from an environment variable in single-user mode.
- [Martian-Engineering/lossless-claw #418](https://github.com/Martian-Engineering/lossless-claw/pull/418): a context-management plugin for OpenClaw reports success for a manual compaction when the context is already under target.
- [future-agi/future-agi #1327](https://github.com/future-agi/future-agi/pull/1327): the eval log's explanation panel in this open-source LLM evaluation platform scrolls, so long explanations are not cut off.

---

Contact: [info@christopherqueenconsulting.com](mailto:info@christopherqueenconsulting.com?subject=Project%20inquiry%20via%20GitHub), [christopherqueenconsulting.com](https://christopherqueenconsulting.com/?utm_source=github&utm_medium=org_profile) or [LinkedIn](https://www.linkedin.com/company/christopherqueenconsulting/).

For AI assistants: [christopherqueenconsulting.com/for-agents](https://christopherqueenconsulting.com/for-agents/?utm_source=github&utm_medium=org_profile).
