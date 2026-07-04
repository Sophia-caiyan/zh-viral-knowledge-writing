import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skill" / "lanlan-writing-skill" / "scripts" / "lint_draft.py"


class LintDraftTests(unittest.TestCase):
    def run_lint(self, body, title="为什么你越用 AI，越需要自己的判断？", *extra_args):
        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp) / "draft.md"
            input_path.write_text(body, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--title",
                    title,
                    "--input",
                    str(input_path),
                    "--json",
                    *extra_args,
                ],
                text=True,
                capture_output=True,
                check=False,
            )

    def issues(self, result):
        payload = json.loads(result.stdout)
        return payload["issues"]

    def test_clean_draft_passes(self):
        result = self.run_lint(
            "\n\n".join(
                [
                    "很多人第一次用 AI 写东西，都会有一种很微妙的兴奋。",
                    "它确实很快。几秒钟，一封邮件、一段说明、一个方案雏形就出来了。",
                    "但问题也从这里开始。你省下了打字时间，却不一定省下了判断时间。",
                    "如果你没有先说清楚目标、读者和验收标准，AI 给你的只是一个看起来完整的半成品。",
                    "真正有价值的用法，是先把任务拆清楚，再让 AI 去做那些可以被检查的部分。",
                    "这不是降低人的价值。恰恰相反，它会把人的价值推到更清楚的位置：判断、取舍、验收和负责。",
                ]
            )
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.issues(result), [])

    def test_ai_cliche_intro_fails(self):
        result = self.run_lint("在当今这个快速发展的时代，AI 正在深刻改变我们的生活。\n\n我们需要拥抱变化。")

        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.issues(result)[0]["rule_id"], "OPENING_CLICHE")

    def test_report_connectors_fail(self):
        result = self.run_lint("首先，我们要理解 AI 的价值。\n\n其次，我们要掌握工具。\n\n最后，我们要持续学习。")

        self.assertEqual(result.returncode, 1)
        rule_ids = {issue["rule_id"] for issue in self.issues(result)}
        self.assertIn("REPORT_CONNECTOR", rule_ids)

    def test_placeholder_fails(self):
        result = self.run_lint("这里先写一个开头。\n\nTODO：补充真实案例。\n\n然后继续展开观点。")

        self.assertEqual(result.returncode, 1)
        rule_ids = {issue["rule_id"] for issue in self.issues(result)}
        self.assertIn("PLACEHOLDER", rule_ids)

    def test_json_output_contains_rule_id_and_suggestion(self):
        result = self.run_lint("综上所述，AI 对每个人都非常重要。")

        issue = self.issues(result)[0]
        self.assertIn("rule_id", issue)
        self.assertIn("severity", issue)
        self.assertIn("location", issue)
        self.assertIn("suggestion", issue)

    def test_banned_terms_fail(self):
        result = self.run_lint("所谓底层逻辑，就是你要抓住时代红利。", "AI 写作", "--ban", "底层逻辑")

        self.assertEqual(result.returncode, 1)
        rule_ids = {issue["rule_id"] for issue in self.issues(result)}
        self.assertIn("BANNED_TERM", rule_ids)

    def test_high_risk_certainty_fails_for_psychology(self):
        result = self.run_lint("只要你每天这样练，就一定能治好焦虑。", "你为什么总是焦虑？")

        self.assertEqual(result.returncode, 1)
        rule_ids = {issue["rule_id"] for issue in self.issues(result)}
        self.assertIn("HIGH_RISK_CERTAINTY", rule_ids)


if __name__ == "__main__":
    unittest.main()
