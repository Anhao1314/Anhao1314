"""Checks for the text-first GitHub profile, not for project capabilities."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
REPO_PREFIX = "https://github.com/Anhao1314/"
REPOSITORIES = {
    "g1-jev-swarm-lab",
    "Go2w-MoRA-navigation",
    "RL-Sentinel",
    "CarryTrace",
    "flowcredit-research",
    "flowcredit",
    "deep-native",
    "life-finds-a-way",
}


class TextProfileTests(unittest.TestCase):
    def test_identity_and_personal_thesis(self):
        for phrase in ("# Eason", "人工智能本科生", "2027 届", "生命会自己寻求出路"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, README)

    def test_editorial_order(self):
        sections = [
            "## 🔭 我在关注什么",
            "## 🧩 项目记录",
            "## 🌱 我如何看待 AI Coding",
            "## ✍️ 研究之外",
        ]
        positions = [README.index(section) for section in sections]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(len(re.findall(r"(?m)^## ", README)), len(sections))

    def test_all_project_links_are_present(self):
        destinations = set(re.findall(
            r"https://github\.com/Anhao1314/([A-Za-z0-9_.-]+)", README
        ))
        self.assertEqual(destinations, REPOSITORIES)
        for repo in REPOSITORIES:
            with self.subTest(repo=repo):
                self.assertIn(REPO_PREFIX + repo, README)

    def test_research_limits_remain_visible(self):
        for phrase in ("仿真结果不等于", "尚未证明质量提升", "不代表已经校准的信用评级", "失败也是证据"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, README)

    def test_no_playground_visual_debt(self):
        for legacy in (
            "<picture", "<img", "<svg", "<details", "assets/playground/",
            "EASON / PLAYGROUND", "ALWAYS IN BETA", "Things I've built",
            "Side quests",
        ):
            with self.subTest(legacy=legacy):
                self.assertNotIn(legacy, README)
        self.assertFalse((ROOT / "assets/playground").exists())
        self.assertFalse((ROOT / "scripts/build_assets.py").exists())
        self.assertFalse((ROOT / "docs/profile-design.md").exists())
        self.assertFalse((ROOT / "docs/validation-2026-10-08.md").exists())

    def test_no_tracking_or_false_live_data(self):
        for host in ("shields.io", "readme-typing-svg", "github-stats-alpha", "github-profile-summary-cards"):
            self.assertNotIn(host, README)
        self.assertLess(len(README), 8000)


if __name__ == "__main__":
    unittest.main()
