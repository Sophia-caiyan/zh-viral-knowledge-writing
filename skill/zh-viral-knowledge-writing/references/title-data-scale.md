# Title Data Scale

Use this reference when the user asks for titles, title diagnosis, title scoring, or "which title should I use". It summarizes the public-safe aggregate analysis of 1026 valid titles from the private metadata workbook. Do not quote or reproduce the full title dataset.

## Data Snapshot

| Field | Value |
| --- | ---: |
| Metadata rows inspected | 1111 |
| Valid titles analyzed | 1026 valid titles |
| Like p25 | 5775 |
| Like median | 9270 |
| Like p75 | 15286 |
| Like p90 | 25461 |

Engagement note: WeChat read counts were mostly capped at 100001, so likes are more useful than reads for relative title analysis.

## Layered Findings

| Finding | Low Likes | Mid Likes | High Likes | Top 10% Likes | Skill Rule |
| --- | ---: | ---: | ---: | ---: | --- |
| Median title length | 13 | 13 | 13 | 13 | Aim for 12-18 Chinese characters; use subtitle for explanation. |
| Average title length | 13.4 | 13.5 | 13.0 | 13.1 | Do not make titles long to look thoughtful. |
| Question rate | 25.4% | 20.3% | 20.9% | 14.4% | Questions are optional, not the main hook. |
| Exclamation rate | 33.2% | 23.0% | 21.6% | 19.2% | Exclamation marks are seasoning, not structure. |
| Number rate | 38.3% | 38.4% | 37.9% | 37.5% | Number titles need real method delivery. |
| You/me/self rate | 58.2% | 64.7% | 58.8% | 70.2% | Prefer direct reader implication. |
| Colon rate | 3.9% | 6.2% | 15.0% | 11.5% | Colon can frame a judgment or case, but do not overuse. |
| Quote/book-title mark rate | 9.0% | 10.5% | 8.5% | 13.5% | Quoted speech works when it creates a scene. |
| Emotion word rate | 16.8% | 19.7% | 21.6% | 23.1% | Use emotion with scene, cost, and exit. |
| Conflict word rate | 34.8% | 31.2% | 32.0% | 34.6% | Conflict matters, but must be specific. |
| Identity word rate | 23.8% | 22.0% | 22.9% | 19.2% | Identity alone is weaker than situation plus conflict. |
| Empty buzzword rate | 0.0% | 0.0% | 0.0% | 0.0% | Ban empty terms such as 认知升级, 底层逻辑, 时代红利, 破局, 赋能. |

## Core Interpretation

High-like titles are not longer or more punctuated. They are more often compact, reader-facing, and stance-bearing.

The reusable pattern:

> A concrete person or relationship + a felt conflict + a clear judgment + a promise the body can prove.

For AI, psychology, and coaching topics, translate this as:

- Do not title the concept. Title the reader's situation.
- Do not decorate with anxiety. Name the concrete cost behind anxiety.
- Do not rely on question marks or exclamation marks.
- Do not use big abstract terms.
- Make the title a Forwardable stance: the reader can share it to express a position.

## Title Data Scale

Score each candidate out of 100 before recommending it.

| Dimension | Points | Pass Standard |
| --- | ---: | --- |
| Reader implication | 15 | Names or strongly implies "you/me/us/specific reader". |
| Compactness | 10 | Usually 12-18 Chinese characters, unless a public case requires longer framing. |
| Concrete situation | 15 | Points to a scene, relationship, work moment, or visible cost. |
| Conflict and judgment | 20 | Contains a real tension and a defensible stance, not a vague topic. |
| Proof readiness | 20 | The body can prove the claim through emotion escalation, logic chain, and solution delivery. |
| Forwardable stance | 15 | Sharing the title lets the reader express "this says what I mean". |
| Punctuation discipline | 5 | Does not depend on "?!", ellipses, or shouting to create force. |

Hard reject:

- The title is only a topic label.
- The title uses anxiety as a decoration.
- The title sounds clever but cannot be proved by the planned article.
- The title promises a list or method but the body cannot deliver it.
- The title depends on empty big words.

## Output Mode For Title Requests

When the user asks for titles, output:

1. Data-calibrated diagnosis.
2. Emotion escalation.
3. Logic chain.
4. Solution delivery.
5. 20 title candidates grouped by hook.
6. A scoring table for the top 5 candidates.
7. Recommended title and subtitle.
8. Why the title can be proved by the article.
9. Attractive but rejected titles, with rejection reason.

## Top-5 Scoring Table Format

| Rank | Title | Score | Why It Works | Body Must Prove | Risk |
| ---: | --- | ---: | --- | --- | --- |
| 1 | ... | 0-100 | Reader + conflict + stance | Emotion, logic, solution | Overpromise / safe |

Use this table in user-facing answers when the user is comparing titles.

