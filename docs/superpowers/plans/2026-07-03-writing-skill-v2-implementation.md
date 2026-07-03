# Writing Skill V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade `zh-viral-knowledge-writing` into a public, title-integrated, quality-checked WeChat long-form writing skill for AI, psychology, coaching, workplace, and growth topics.

**Architecture:** Keep the GitHub repository as a public project wrapper and place the installable skill under `skill/zh-viral-knowledge-writing/`. Put deterministic checks in a script with tests, and put judgment-heavy writing guidance in progressively loaded references. Keep raw corpus files outside the repository.

**Tech Stack:** Markdown skill files, YAML UI metadata, Python standard library for linting and tests, GitHub-friendly docs.

---

## File Map

- Create `README.md`: public install, usage, evaluation, and copyright boundary.
- Create `skill/zh-viral-knowledge-writing/SKILL.md`: lean V2 workflow and routing.
- Create `skill/zh-viral-knowledge-writing/agents/openai.yaml`: UI metadata matching the V2 skill.
- Create `skill/zh-viral-knowledge-writing/references/title-system.md`: title hooks, title scoring, title contract, subtitle rules.
- Create `skill/zh-viral-knowledge-writing/references/article-archetypes.md`: six WeChat long-form article archetypes.
- Create `skill/zh-viral-knowledge-writing/references/domain-adaptation.md`: AI, psychology, coaching, workplace/growth adaptation rules.
- Create `skill/zh-viral-knowledge-writing/references/quality-system.md`: source-density gate, four-layer quality loop, ethical boundaries.
- Create `skill/zh-viral-knowledge-writing/references/style-examples.md`: synthetic before/after examples only.
- Create `skill/zh-viral-knowledge-writing/scripts/lint_draft.py`: deterministic draft checks.
- Create `tests/test_lint_draft.py`: Python tests for `lint_draft.py`.
- Create `tests/test_skill_structure.py`: repository and skill structure checks.
- Create `evals/cases.json`: 24 public prompt cases.
- Create `evals/rubric.md`: scoring rules and release gates.
- Create `evals/README.md`: how to run and record evaluations.
- Create `research/corpus-method.md`: what was studied and what stays private.
- Create `research/aggregate-findings.md`: distilled corpus findings without raw article text.
- Keep root `SKILL.md`, `agents/openai.yaml`, and `references/*.md` until V2 files are complete, then remove them to avoid duplicate install targets.

## Task 1: Add Public Evaluation Skeleton

**Files:**
- Create: `evals/cases.json`
- Create: `evals/rubric.md`
- Create: `evals/README.md`

- [ ] **Step 1: Create the evaluation files**

Add 24 cases across AI, psychology, and coaching. Each domain gets topic-only, rough-idea, plain-draft, and source-material variants.

- [ ] **Step 2: Validate JSON**

Run: `rtk python3 -m json.tool evals/cases.json`

Expected: formatted JSON prints with exit code 0.

- [ ] **Step 3: Review rubric against spec**

Check that the rubric includes title delivery, reader implication, opening pull, structure, evidence/usefulness, human feel, ending, and release gates.

## Task 2: Add Corpus Research Docs

**Files:**
- Create: `research/corpus-method.md`
- Create: `research/aggregate-findings.md`

- [ ] **Step 1: Write corpus method**

Document the 1111 metadata rows, 911 PDF matches, 719 readable bodies, 116 stratified feature-card sample, and the private/public boundary.

- [ ] **Step 2: Write aggregate findings**

Move reusable findings from `references/mimeng-patterns.md` into public research language without quoting raw articles.

- [ ] **Step 3: Check no raw article excerpts leaked**

Run: `rtk rg -n "原文|摘录|全文|咪蒙说|粉丝说" research`

Expected: no accidental raw-excerpt claims that imply the repo contains article text.

## Task 3: Write Lint Tests First

**Files:**
- Create: `tests/test_lint_draft.py`

- [ ] **Step 1: Write failing tests for the missing script**

Test these behaviors:

```python
def test_clean_draft_passes():
    ...

def test_ai_cliche_intro_fails():
    ...

def test_report_connectors_fail():
    ...

def test_placeholder_fails():
    ...

def test_json_output_contains_rule_id_and_suggestion():
    ...
```

- [ ] **Step 2: Run tests and verify RED**

Run: `rtk python3 -m unittest tests/test_lint_draft.py`

Expected: FAIL because `skill/zh-viral-knowledge-writing/scripts/lint_draft.py` does not exist yet.

## Task 4: Implement Deterministic Draft Linter

**Files:**
- Create: `skill/zh-viral-knowledge-writing/scripts/lint_draft.py`

- [ ] **Step 1: Implement CLI and rule model**

Use only Python standard library. Support:

```text
python scripts/lint_draft.py --title "文章标题" --input article.md --json
```

Exit 0 when no issues; exit 1 when any issue exists.

- [ ] **Step 2: Implement V2 hard-rule checks**

Include deterministic checks for:

- Empty/AI-cliche openings.
- Report-style connectors.
- Consecutive very long paragraphs.
- Too many list headings or bold marks.
- Placeholders.
- High-risk certainty expressions in psychology/coaching/AI factual contexts.
- Optional banned terms through repeated `--ban` flags.

- [ ] **Step 3: Run GREEN tests**

Run: `rtk python3 -m unittest tests/test_lint_draft.py`

Expected: PASS.

## Task 5: Build the Installable V2 Skill

**Files:**
- Create: `skill/zh-viral-knowledge-writing/SKILL.md`
- Create: `skill/zh-viral-knowledge-writing/agents/openai.yaml`
- Create: `skill/zh-viral-knowledge-writing/references/title-system.md`
- Create: `skill/zh-viral-knowledge-writing/references/article-archetypes.md`
- Create: `skill/zh-viral-knowledge-writing/references/domain-adaptation.md`
- Create: `skill/zh-viral-knowledge-writing/references/quality-system.md`
- Create: `skill/zh-viral-knowledge-writing/references/style-examples.md`

- [ ] **Step 1: Write lean SKILL.md**

Keep the body focused on workflow, source-density gate, progressive loading, and default deliverables.

- [ ] **Step 2: Write title and article references**

Split detailed title hooks, title contract, archetypes, domain rules, examples, and quality loop into reference files.

- [ ] **Step 3: Validate skill frontmatter and metadata**

Add `tests/test_skill_structure.py` in Task 7 to validate frontmatter, reference links, metadata, and duplicate V1 files.

## Task 6: Update Public README and Remove V1 Duplicate Files

**Files:**
- Create: `README.md`
- Delete after migration: `SKILL.md`
- Delete after migration: `agents/openai.yaml`
- Delete after migration: `references/mimeng-patterns.md`
- Delete after migration: `references/topic-adaptation.md`
- Delete after migration: `references/output-recipes.md`

- [ ] **Step 1: Write README**

Explain:

- What the skill does.
- How to install from the repo.
- Why the repo does not include raw articles.
- How title generation and quality checks work.
- How to run evaluation and lint checks.

- [ ] **Step 2: Remove duplicate V1 files**

Only delete root V1 skill files after the V2 skill folder is complete and reviewed.

## Task 7: Verify Structure and Content

**Files:**
- Existing and newly created files.
- Create: `tests/test_skill_structure.py`

- [ ] **Step 1: Write structure tests**

Test these behaviors:

```python
def test_skill_frontmatter_has_only_name_and_description():
    ...

def test_skill_references_exist():
    ...

def test_openai_yaml_mentions_skill_name():
    ...

def test_root_v1_skill_files_removed():
    ...
```

- [ ] **Step 2: Run tests**

Run: `rtk python3 -m unittest tests/test_lint_draft.py`

Expected: PASS.

- [ ] **Step 3: Run structure tests**

Run: `rtk python3 -m unittest tests/test_skill_structure.py`

Expected: PASS.

- [ ] **Step 4: Validate evaluation JSON**

Run: `rtk python3 -m json.tool evals/cases.json`

Expected: exit code 0.

- [ ] **Step 5: Check linter CLI help**

Run: `rtk python3 skill/zh-viral-knowledge-writing/scripts/lint_draft.py --help`

Expected: CLI usage prints successfully.

- [ ] **Step 6: Check no stale V1 references remain**

Run: `rtk rg -n "mimeng-patterns|topic-adaptation|output-recipes|小红书|短视频" skill README.md evals research`

Expected: no stale file names; no Xiaohongshu/short-video promise in V2.

- [ ] **Step 7: Check diff hygiene**

Run: `rtk git diff --check`

Expected: no whitespace errors.

## Task 8: Commit and Installation Sync

**Files:**
- All V2 project files.
- Optional local installed copy: `/Users/xingcaiyan/.codex/skills/zh-viral-knowledge-writing/`

- [ ] **Step 1: Review git status**

Run: `rtk git status --short`

Expected: only intended files changed.

- [ ] **Step 2: Commit repository changes**

Run:

```bash
rtk git add -A
rtk git commit -m "Implement V2 writing skill quality system"
```

- [ ] **Step 3: Sync installed skill only after repo version passes**

Copy `skill/zh-viral-knowledge-writing/` into `/Users/xingcaiyan/.codex/skills/zh-viral-knowledge-writing/` with explicit approval if sandbox requires it.
