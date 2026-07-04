import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "zh-viral-knowledge-writing"


class TitleSystemQualityTests(unittest.TestCase):
    def test_title_is_verified_promise_not_title_first(self):
        text = (SKILL_DIR / "references" / "title-system.md").read_text(encoding="utf-8")

        self.assertIn("Title is not the first step", text)
        self.assertIn("validated promise", text)

    def test_title_system_requires_emotion_logic_solution_ladder(self):
        text = (SKILL_DIR / "references" / "title-system.md").read_text(encoding="utf-8")

        self.assertIn("Emotion Escalation Ladder", text)
        self.assertIn("Logic Chain", text)
        self.assertIn("Solution Delivery", text)

    def test_quality_system_checks_three_deliveries(self):
        text = (SKILL_DIR / "references" / "quality-system.md").read_text(encoding="utf-8")

        self.assertIn("Emotion delivery", text)
        self.assertIn("Logic delivery", text)
        self.assertIn("Solution delivery", text)

    def test_skill_workflow_verifies_title_promise(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Verify the title promise", text)

    def test_title_data_scale_reference_exists(self):
        text = (SKILL_DIR / "references" / "title-data-scale.md").read_text(encoding="utf-8")

        self.assertIn("Title Data Scale", text)
        self.assertIn("1026 valid titles", text)
        self.assertIn("12-18 Chinese characters", text)
        self.assertIn("Forwardable stance", text)

    def test_skill_loads_title_data_scale_for_title_requests(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("references/title-data-scale.md", text)


if __name__ == "__main__":
    unittest.main()
