---
name: zh-viral-knowledge-writing
description: Use when creating, diagnosing, outlining, titling, or rewriting high-open-rate Chinese WeChat Official Account long-form articles about AI, psychology, coaching, workplace, personal growth, creator education, or social commentary; especially when the user asks for 爆款, 高共鸣, 标题钩子, 公众号长文, 情绪共鸣, story-driven knowledge writing, or turning abstract ideas into concrete reader-facing Chinese articles.
---

# 中文高共鸣公众号长文

Use this skill to turn an abstract topic, rough idea, or draft into a WeChat long-form article with a strong title, concrete opening, defensible judgment, useful delivery, and ethical boundaries.

The goal is not to copy any living writer's exact persona. Reuse only transferable mechanics: reader pain, scene, tension, reversal, proof, usefulness, and shareable judgment.

## Scope

Use for:

- WeChat Official Account long-form articles, normally 2000-3500 Chinese characters.
- AI, psychology, coaching, workplace, personal growth, creator education, and social commentary topics.
- Title generation, subtitle, opening, outline, full draft, critique, or rewrite.

Do not use this as the primary skill for Xiaohongshu notes, short-video scripts, SEO reports, news summaries, academic papers, or brand press releases.

## Load References

Read only what the request needs:

- For any complete title, outline, rewrite, or full article request, read `references/title-system.md` and `references/quality-system.md`.
- After diagnosing the article type, read `references/article-archetypes.md`.
- For AI, psychology, coaching, workplace, or growth topics, read the matching section in `references/domain-adaptation.md`.
- For full drafting, rewriting, or critique, read `references/style-examples.md`.

## Core Workflow

1. Diagnose the input.
   - Extract topic, target reader, platform, desired action, user stance, source material, hidden reader emotion, opposing force, practical promise, and risk domain.
   - If the user gives little context, infer a practical default and state it briefly.

2. Classify source density.
   - A: user supplied real story, facts, and stance. A full article can use those materials.
   - B: user supplied stance and partial material. A full article may be drafted, but mark evidence gaps.
   - C: user supplied only a topic. Prefer title, angle, and outline. If the user explicitly asks for a full article, use clearly marked typical scenes, not invented first-person experience.

3. Choose one article archetype.
   - Emotional representation, relationship truth, workplace interest, anti-chicken-soup growth, story/person, or knowledge method.
   - Do not choose story/person unless the user supplies verifiable story material.

4. Design title before drafting.
   - Generate at least 12 candidates across at least 4 hook combinations.
   - Score and reject titles that cannot be delivered.
   - Pick one recommended title and subtitle.
   - Build an internal title contract mapping title promises to body sections.

5. Draft the article.
   - First 20% must contain scene, conflict, and core judgment.
   - Put a scene, example, or consequence after every abstract point.
   - Alternate emotional recognition and useful explanation.
   - Preserve supplied facts, but rebuild order when the user's draft is flat.

6. Run quality checks.
   - L1 deterministic lint: use `scripts/lint_draft.py` when checking a saved draft.
   - L2 title contract: every title promise must be delivered.
   - L3 score content quality: reader implication, opening, conflict, judgment, evidence, usefulness, rhythm, ending.
   - L4 check human feel and ethics.
   - Revise up to two rounds. If still weak, name the missing material instead of padding.

## Default Deliverables

Unless the user asks for a narrower output, provide:

1. 读者诊断
2. 核心判断
3. 12 个标题，按钩子分组
4. 推荐标题 + 副标题
5. 标题合同摘要
6. 公众号长文正文或详细结构
7. 自检：最强点、标题兑现、需要补证据、风险边界

## Safety And Taste

- Be sharp, not cruel.
- Do not fabricate stories, cases, surveys, research, product facts, credentials, or first-person experiences.
- For psychology and coaching, do not diagnose the reader. Use bounded language such as "可能", "常见", "可以试试".
- For current AI products, model capabilities, laws, finance, medicine, or news, verify with sources or ask the user for material.
- Do not use humiliation of vulnerable people as the hook.
- If a stronger title would overpromise, lower the title promise or ask for more evidence.
