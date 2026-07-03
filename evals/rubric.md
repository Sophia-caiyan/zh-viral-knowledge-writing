# Evaluation Rubric

Use this rubric to compare skill versions on the same prompt. Score once per generated output. Do not reroll a poor answer just because it feels unlucky.

## Score

Total: 100 points.

| Dimension | Weight | What To Look For |
| --- | ---: | --- |
| Title quality and delivery | 20 | The title names a reader, tension, and promise; the body actually delivers every key promise. |
| Reader implication | 15 | The piece makes the target reader feel "this is about me" through concrete situations, not generic claims. |
| Opening pull | 15 | The first screen contains scene, conflict, cost, or a sharp reversal. It does not begin like a report. |
| Structure and rhythm | 15 | Each section advances new information; emotion and usefulness alternate; paragraphing helps reading without becoming mechanical. |
| Judgment, evidence, and usefulness | 20 | The central claim is clear and defensible; examples or source material support it; the reader gets a usable distinction, question, script, or action. |
| Human feel | 10 | The writing sounds like a person thinking with the reader, not a template performing empathy. |
| Ending spreadability | 5 | The ending gives language, permission, boundary, or a small next action worth sharing. |

## Core 1-5 Ratings

Also rate these fields from 1 to 5:

- Reader relevance.
- Opening traction.
- Conflict clarity.
- Judgment strength.
- Reasoning and evidence.
- Practical value.
- Rhythm.
- Ending.
- Ethical safety.

Any core field below 3 is a release blocker for that case.

## Failure Tags

Attach any that apply:

- `title-overpromise`: title promises more than the body can prove.
- `generic-opening`: opening restates the topic instead of creating a scene or tension.
- `fake-story-risk`: output implies a real experience, case, survey, or source not supplied.
- `unsupported-claim`: a factual, product, psychological, medical, legal, or financial claim is not bounded or sourced.
- `emotion-only`: strong emotion without mechanism, evidence, or action.
- `method-only`: useful information without reader pain or reason to keep reading.
- `concept-stack`: abstract nouns pile up without concrete situations.
- `report-style`: sounds like an essay, report, or course note.
- `shame-as-hook`: uses humiliation of vulnerable readers as the main hook.
- `stale-v1-pattern`: follows old generic recipes without title contract or quality revision.

## Release Gates

V2 can be called releasable only when:

- Average score is at least 80/100.
- No core dimension is below 3/5.
- At least 70% of cases beat V1 by 10 points or more.
- Title key promise misses are 0.
- Fabricated facts, experiences, or sources are 0.
- Deterministic linter tests pass.
- Skill structure tests pass.

## Scoring Notes

The score is a quality regression signal, not a permanent universal benchmark. Record the model, date, skill commit, prompt set version, and whether the answer had tool access.
