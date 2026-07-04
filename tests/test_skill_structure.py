import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "lanlan-writing-skill"
SKILL_MD = SKILL_DIR / "SKILL.md"


class SkillStructureTests(unittest.TestCase):
    def frontmatter(self):
        text = SKILL_MD.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        fields = {}
        for line in match.group(1).splitlines():
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
        return fields, text

    def test_skill_frontmatter_has_only_name_and_description(self):
        fields, _ = self.frontmatter()

        self.assertEqual(set(fields), {"name", "description"})
        self.assertEqual(fields["name"], "lanlan-writing-skill")
        self.assertLessEqual(len(fields["name"] + fields["description"]), 1024)
        self.assertIn("WeChat Official Account", fields["description"])

    def test_skill_references_exist(self):
        _, text = self.frontmatter()
        expected = [
            "title-system.md",
            "article-archetypes.md",
            "domain-adaptation.md",
            "quality-system.md",
            "style-examples.md",
        ]

        for filename in expected:
            self.assertTrue((SKILL_DIR / "references" / filename).exists(), filename)
            self.assertIn(f"references/{filename}", text)

    def test_openai_yaml_mentions_skill_name(self):
        metadata = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")

        self.assertIn('display_name: "Lanlan Writing Skill"', metadata)
        self.assertIn("$lanlan-writing-skill", metadata)

    def test_root_v1_skill_files_removed(self):
        self.assertFalse((ROOT / "SKILL.md").exists())
        self.assertFalse((ROOT / "agents" / "openai.yaml").exists())
        self.assertFalse((ROOT / "references" / "mimeng-patterns.md").exists())
        self.assertFalse((ROOT / "references" / "topic-adaptation.md").exists())
        self.assertFalse((ROOT / "references" / "output-recipes.md").exists())

    def test_no_stale_platform_promises_in_skill(self):
        haystack = "\n".join(
            path.read_text(encoding="utf-8")
            for path in [SKILL_MD, *sorted((SKILL_DIR / "references").glob("*.md"))]
        )

        self.assertNotIn("小红书笔记、短视频", haystack)
        self.assertNotIn("mimeng-patterns", haystack)
        self.assertNotIn("topic-adaptation", haystack)
        self.assertNotIn("output-recipes", haystack)


if __name__ == "__main__":
    unittest.main()
