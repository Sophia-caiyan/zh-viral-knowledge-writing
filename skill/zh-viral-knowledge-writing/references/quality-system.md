# Quality System

Use this reference before and after drafting.

## Source Density Gate

Classify the input before writing:

| Level | Input | Allowed Output |
| --- | --- | --- |
| A | Real story, facts, source material, and user stance | Full article using supplied material. |
| B | Clear stance and partial material | Full article with marked evidence gaps. |
| C | Topic only | Prefer angle, title, and outline. If full draft is requested, use clearly marked typical scenes. |

Never turn a typical scene, composite observation, or invented example into a real first-person experience.

## Four-Layer Check

### L1: Deterministic Lint

When a draft is saved as Markdown, run:

```bash
python scripts/lint_draft.py --title "文章标题" --input article.md --json
```

The script checks only deterministic issues:

- Cliche openings.
- Report-style connectors.
- Placeholders.
- Consecutive long paragraphs.
- Too many headings or bold marks.
- High-risk certainty words.
- User-specified banned terms.

Semantic issues still require L2-L4.

### L2: Title Contract

Check title elements and proof layers:

- Reader named or clearly implied.
- Core conflict appears early.
- Reversal appears in the first screen or first 20%.
- Evidence, supplied material, or concrete example supports the claim.
- Method or answer appears if promised.
- Ending gives emotional exit.
- Emotion delivery: the body moves from surface feeling to scene, cost, opposing force, judgment, and emotional exit.
- Logic delivery: the body shows situation, misread problem, real mechanism, evidence or example, and bounded judgment.
- Solution delivery: the body gives a usable distinction, question, script, boundary, action, or framework.

If a title promise is missing, either add support or reduce the title's promise.

Do not pass a title just because it is emotionally strong. A strong title must be emotionally charged, logically proved, and practically delivered.

### L3: Content Score

Rate 1-5:

- Reader implication.
- Opening traction.
- Conflict clarity.
- Judgment strength.
- Reasoning and evidence.
- Practical value.
- Rhythm.
- Ending.

Any field below 3 requires one revision round.

### L4: Human Feel And Ethics

Ask:

- Is this speaking for a concrete person or only arranging concepts?
- Is there a real judgment, or only nice sentences?
- Does emotion come from a believable situation, not exaggeration?
- Did we invent a case, source, research result, or first-person experience?
- Does the reader leave with language, boundary, or action?

## Revision Rules

- Revise the strongest failure first.
- Maximum two automatic revision rounds.
- If still below quality line, state the missing input: story, facts, target reader, stance, evidence, or risk boundary.
- Do not solve weakness by making the title louder.

## Common Failure Fixes

| Failure | Fix |
| --- | --- |
| Generic title | Add reader, cost, conflict, and body-deliverable promise. |
| Empty anxiety | Add concrete scene, hidden cost, opposing force, and emotional exit. |
| Flat opening | Start with a scene, dilemma, or contradiction. |
| Emotion-only | Add mechanism, evidence, or action. |
| Method-only | Add reader pain before the method. |
| Concept stack | Replace every abstract paragraph with a daily-life moment. |
| Fake story risk | Rename it as "一个典型场景是..." or remove it. |
| Overclaiming psychology | Add boundary language and remove cure promises. |
| AI prophecy | Verify, narrow, or reframe as a workflow observation. |

## Self-Check Output

For substantial work, end with:

- 最强点:
- 标题兑现:
- 需要补证据:
- 风险边界:
