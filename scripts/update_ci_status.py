#!/usr/bin/env python3
"""Rewrite the live CI block in profile/README.md.

Reads the latest completed run of each listed workflow on its repo's default
branch (public GitHub API, standard library only) and replaces the text between
<!-- CI-STATUS:START --> and <!-- CI-STATUS:END --> with a plain table.
Writes the file only when the table changed. Exit 0 on success, 1 on an API error
(the README is left as it was).

Usage: GITHUB_TOKEN=... python3 scripts/update_ci_status.py [README path]
"""
import json
import os
import re
import sys
import urllib.request

CHECKS = [
    ("christopherqueenconsulting/linkedin_engagement_manager", "LEM", "unit-tests.yml",
     "unit tests", "every change"),
    ("christopherqueenconsulting/linkedin_engagement_manager", "LEM", "deploy-drift-check.yml",
     "deploy drift check", "hourly: live version against published releases"),
    ("christopherqueenconsulting/linkedin_engagement_manager", "LEM", "prompt-evals.yml",
     "prompt evals", "weekly: grades changed prompts, datasets and models"),
    ("christopherqueenconsulting/cpcc_task_automation", "CPCC", "unit-tests.yml",
     "test suite", "every change"),
    ("christopherqueenconsulting/cpcc_task_automation", "CPCC", "prompt-eval.yml",
     "prompt evaluation", "every change to prompts"),
    ("christopherqueenconsulting/cpcc_task_automation", "CPCC", "pii-guard.yml",
     "PII guard", "every change: blocks personal data in the repo"),
]

START = "<!-- CI-STATUS:START -->"
END = "<!-- CI-STATUS:END -->"
WORDS = {"success": "passed", "failure": "failed", "cancelled": "cancelled",
         "timed_out": "timed out", "skipped": "skipped", "neutral": "neutral",
         "action_required": "waiting on a person", "startup_failure": "failed to start"}


def get(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "org-profile-ci-status",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
           if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def table():
    branches = {}
    rows = ["| Check | Latest result |", "| --- | --- |"]
    for repo, short, wf, name, when in CHECKS:
        if repo not in branches:
            branches[repo] = get(f"https://api.github.com/repos/{repo}")["default_branch"]
        runs = get(f"https://api.github.com/repos/{repo}/actions/workflows/{wf}/runs"
                   f"?branch={branches[repo]}&status=completed&per_page=1")["workflow_runs"]
        if runs:
            r = runs[0]
            word = WORDS.get(r["conclusion"] or "", r["conclusion"] or "unknown")
            result = f"[{word}, {r['updated_at'][:10]}]({r['html_url']})"
        else:
            result = "no completed run yet"
        link = f"https://github.com/{repo}/actions/workflows/{wf}"
        rows.append(f"| [{short} {name}]({link}) | {result} |")
    return "\n".join(rows)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "profile/README.md"
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        print("markers missing", file=sys.stderr)
        return 1
    try:
        body = table()
    except Exception as e:  # leave the README untouched on any API failure
        print(f"API error: {e}", file=sys.stderr)
        return 1
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 lambda _m: f"{START}\n{body}\n{END}", text, flags=re.S)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("updated")
    else:
        print("unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
