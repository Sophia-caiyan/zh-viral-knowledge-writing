#!/usr/bin/env python3
import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Issue:
    rule_id: str
    severity: str
    location: str
    snippet: str
    suggestion: str


OPENING_CLICHE_PATTERNS = [
    re.compile(r"在当今.*时代"),
    re.compile(r"快速发展"),
    re.compile(r"深刻改变"),
    re.compile(r"随着.*(发展|普及|到来)"),
    re.compile(r"众所周知"),
    re.compile(r"不可否认"),
]

REPORT_CONNECTOR_RE = re.compile(
    r"^\s*(首先|其次|再次|最后|综上所述|总之|总而言之|总结一下)[，,：:\s]"
)

PLACEHOLDER_RE = re.compile(
    r"(TODO|TBD|FIXME|待补|待完善|占位|此处补充|这里补充|XXX|xxx|【[^】]*(补充|待定|案例)[^】]*】)"
)

HIGH_RISK_CONTEXT_RE = re.compile(
    r"(焦虑|抑郁|创伤|人格|心理|疗愈|治疗|来访者|教练|诊断|AI|模型|产品|最新|数据)"
)

HIGH_RISK_CERTAINTY_RE = re.compile(
    r"(一定能|保证|彻底|根治|治好|永远|绝对|所有人都会|必然|毫无疑问)"
)


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Deterministic lint checks for Chinese long-form knowledge drafts."
    )
    parser.add_argument("--title", required=True, help="Draft title.")
    parser.add_argument("--input", required=True, help="Markdown draft path.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--ban", action="append", default=[], help="Term to forbid. Can repeat.")
    return parser.parse_args(argv)


def nonempty_paragraphs(text):
    return [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]


def line_location(text, snippet):
    if not snippet:
        return "line 1"
    for index, line in enumerate(text.splitlines(), start=1):
        if snippet in line:
            return f"line {index}"
    return "line 1"


def first_line_matching(text, pattern):
    for index, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            return index, line.strip()
    return None, ""


def add_issue(issues, rule_id, severity, location, snippet, suggestion):
    issues.append(
        Issue(
            rule_id=rule_id,
            severity=severity,
            location=location,
            snippet=snippet[:120],
            suggestion=suggestion,
        )
    )


def lint(title, text, banned_terms):
    issues = []
    paragraphs = nonempty_paragraphs(text)
    searchable = f"{title}\n{text}"

    if not title.strip():
        add_issue(
            issues,
            "EMPTY_TITLE",
            "error",
            "title",
            "",
            "补一个能说明读者、冲突和正文承诺的标题。",
        )

    if not text.strip():
        add_issue(
            issues,
            "EMPTY_DRAFT",
            "error",
            "body",
            "",
            "补正文后再运行检查。",
        )
        return issues

    if paragraphs:
        opening = paragraphs[0]
        for pattern in OPENING_CLICHE_PATTERNS:
            if pattern.search(opening):
                add_issue(
                    issues,
                    "OPENING_CLICHE",
                    "error",
                    "opening",
                    opening,
                    "开头换成具体场景、矛盾、代价或反常识判断，避免时代背景式套话。",
                )
                break

    for index, line in enumerate(text.splitlines(), start=1):
        if REPORT_CONNECTOR_RE.search(line):
            add_issue(
                issues,
                "REPORT_CONNECTOR",
                "warning",
                f"line {index}",
                line.strip(),
                "把报告式连接词改成场景推进、判断推进或小标题推进。",
            )

    for index, line in enumerate(text.splitlines(), start=1):
        match = PLACEHOLDER_RE.search(line)
        if match:
            add_issue(
                issues,
                "PLACEHOLDER",
                "error",
                f"line {index}",
                line.strip(),
                "删除占位符，或明确标注需要用户补充的素材。",
            )

    long_positions = [
        (idx, paragraph)
        for idx, paragraph in enumerate(paragraphs, start=1)
        if len(paragraph) > 220
    ]
    for (first_idx, first), (second_idx, second) in zip(long_positions, long_positions[1:]):
        if second_idx == first_idx + 1:
            add_issue(
                issues,
                "LONG_PARAGRAPH_RUN",
                "warning",
                f"paragraphs {first_idx}-{second_idx}",
                first[:60] + " / " + second[:60],
                "连续长段会降低手机阅读速度；拆成更清楚的场景、判断或动作。",
            )
            break

    heading_count = sum(1 for line in text.splitlines() if line.lstrip().startswith("#"))
    bold_count = text.count("**") // 2
    if heading_count > 10:
        add_issue(
            issues,
            "TOO_MANY_HEADINGS",
            "warning",
            "body",
            str(heading_count),
            "减少小标题数量，让段落自身承担推进，而不是把文章切成目录。",
        )
    if bold_count > 12:
        add_issue(
            issues,
            "TOO_MANY_BOLD_MARKS",
            "warning",
            "body",
            str(bold_count),
            "减少加粗；只保留真正承担转折、判断或结论的句子。",
        )

    if HIGH_RISK_CONTEXT_RE.search(searchable) and HIGH_RISK_CERTAINTY_RE.search(searchable):
        line, snippet = first_line_matching(text, HIGH_RISK_CERTAINTY_RE)
        add_issue(
            issues,
            "HIGH_RISK_CERTAINTY",
            "error",
            f"line {line or 1}",
            snippet or title,
            "心理、教练、当前 AI 产品或事实内容要加边界，不要承诺确定疗效、必然结果或未经证实的事实。",
        )

    for term in banned_terms:
        if not term:
            continue
        if term in searchable:
            add_issue(
                issues,
                "BANNED_TERM",
                "error",
                line_location(searchable, term),
                term,
                f"删除或替换禁用词：{term}",
            )

    return issues


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    input_path = Path(args.input)
    try:
        text = input_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"lint_draft.py: cannot read input: {exc}", file=sys.stderr)
        return 2

    issues = lint(args.title, text, args.ban)
    payload = {
        "ok": not issues,
        "issue_count": len(issues),
        "issues": [asdict(issue) for issue in issues],
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if not issues:
            print("OK")
        for issue in issues:
            print(
                f"{issue.severity.upper()} {issue.rule_id} {issue.location}: "
                f"{issue.suggestion}"
            )

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
