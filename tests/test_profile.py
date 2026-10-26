"""Checks for the developer-first GitHub profile, not for project capabilities.

单一真值源：本文件拥有本页的禁用词汇表与字节预算上限——README 只能指向它们，
写不出它们的字面。
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
README_EN = (ROOT / "README.en.md").read_text(encoding="utf-8")

REPO_PREFIX = "https://github.com/Anhao1314/"
REPOSITORIES = {
    "ClaimLedger",
    "FCode",
    "lastgreen",
    "go2w-locomotion",
    "g1-jev-swarm-lab",
    "RL-Sentinel",
    "flowcredit",
    "flowcredit-research",
    "life-finds-a-way",
}

SECTIONS = [
    "## 项目",
    "## 主线：ClaimLedger",
    "## 研发宪章",
    "## 边界，不藏在口号里",
    "## 校验",
    "## 现在",
]

# 状态列只允许从这张词汇表取值（对齐 DESIGN.md 的语义 token 思路）。
STATUS_VOCABULARY = {"开发中", "实验中", "工具", "维护中"}
STATUS_VOCABULARY_EN = {"active", "experiment", "tool", "maintenance"}

BYTE_BUDGET = 6144

# 这是开发者的工作台页面，不是简历。禁用词汇在本页任何地方都不许出现——
# 包括"校验"一节的自我描述。
FORBIDDEN_ZH = ("实习", "简历", "求职", "招聘", "应届", "校招", "秋招", "春招", "offer")
FORBIDDEN_EN = re.compile(r"\b(intern|internship|resume|recruiter|hiring)\b", re.IGNORECASE)

EMOJI = re.compile(r"[\u2600-\u27BF\u2B00-\u2BFF\uFE0F\U0001F000-\U0001FAFF]")


class TextProfileTests(unittest.TestCase):
    def test_identity_and_thesis(self):
        for phrase in (
            "# Eason",
            "怎样让复杂系统的结论可靠、可审计、不冒充现状",
            "人负责定义值得解决的问题",
            "失败也是证据",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, README)

    def test_section_order_and_count(self):
        positions = [README.index(section) for section in SECTIONS]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(len(re.findall(r"(?m)^## ", README)), len(SECTIONS))

    def test_all_project_links_are_present(self):
        destinations = set(
            re.findall(r"https://github\.com/Anhao1314/([A-Za-z0-9_.-]+)", README)
        )
        self.assertEqual(destinations, REPOSITORIES)
        for repo in REPOSITORIES:
            with self.subTest(repo=repo):
                self.assertIn(REPO_PREFIX + repo, README)

    def test_project_table_status_comes_from_vocabulary(self):
        rows = [line for line in README.splitlines() if line.startswith("| [")]
        self.assertGreaterEqual(len(rows), 7)
        for row in rows:
            status = row.rstrip().split("|")[-2].strip()
            with self.subTest(status=status):
                self.assertIn(status, STATUS_VOCABULARY)

    def test_limitations_stay_visible(self):
        for phrase in (
            "不是生产系统",
            "尚未证明质量提升",
            "不代表已经校准的信用评级",
            "仿真结果不等于实物可靠",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, README)

    def test_forbidden_vocabulary_absent(self):
        for word in FORBIDDEN_ZH:
            with self.subTest(word=word):
                self.assertNotIn(word, README)
                self.assertNotIn(word, README_EN)
        for name, text in (("zh", README), ("en", README_EN)):
            match = FORBIDDEN_EN.search(text)
            if match is not None:
                self.fail(f"{name}: forbidden word {match.group(0)!r}")

    def test_section_headers_carry_no_emoji(self):
        for line in README.splitlines():
            if line.startswith("#"):
                with self.subTest(line=line):
                    self.assertIsNone(EMOJI.search(line), "章节标题不用 emoji")

    def test_byte_budget(self):
        for name, text in (("README.md", README), ("README.en.md", README_EN)):
            used = len(text.encode("utf-8"))
            with self.subTest(file=name, used_bytes=used, budget=BYTE_BUDGET):
                self.assertLessEqual(used, BYTE_BUDGET)

    def test_bilingual_pairing(self):
        self.assertIn("[中文](README.md)", README)
        self.assertIn("[English](README.en.md)", README)
        self.assertIn("[中文](README.md)", README_EN)
        self.assertIn("[English](README.en.md)", README_EN)


class EnglishProfileTests(unittest.TestCase):
    def test_identity_and_thesis(self):
        for phrase in (
            "# Eason",
            "unable to masquerade as present state",
            "Failure is evidence",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, README_EN)

    def test_link_set_matches_chinese(self):
        destinations = set(
            re.findall(r"https://github\.com/Anhao1314/([A-Za-z0-9_.-]+)", README_EN)
        )
        self.assertEqual(destinations, REPOSITORIES)

    def test_status_vocabulary(self):
        rows = [line for line in README_EN.splitlines() if line.startswith("| [")]
        self.assertGreaterEqual(len(rows), 7)
        for row in rows:
            status = row.rstrip().split("|")[-2].strip()
            with self.subTest(status=status):
                self.assertIn(status, STATUS_VOCABULARY_EN)


if __name__ == "__main__":
    unittest.main()
