"""Checks for the moon-lit GitHub profile, not for project capabilities.

单一真值源：本文件拥有本页的状态 emoji 词汇表、声明集合与字节预算上限——
README 只能指向它们，写不出它们的定义。检查器只验证结构与在场性，
不验证真伪——结论的真伪，在链接里。
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
README_EN = (ROOT / "README.en.md").read_text(encoding="utf-8")
MOON = (ROOT / "assets" / "moon.svg").read_text(encoding="utf-8")
GENERATOR = (ROOT / "scripts" / "generate_moon.py").read_text(encoding="utf-8")

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

SECTIONS = ["## 声明台账", "## 败诉记录", "## 现在", "## 校验"]
SECTIONS_EN = ["## Claim ledger", "## Failed tests", "## Now", "## Verify"]

# 状态 emoji 词汇表：✅ 已复现 · 🟡 有证据·样本小 · ⚪ 未证明 · ❌ 已证伪·在案 · ⚡️ 争议中
STATUS_EMOJI = ["✅", "🟡", "⚪", "❌", "⚡️"]
ALLOWED_CODEPOINTS = {0x1F52D, 0x2705, 0x1F7E1, 0x26AA, 0x274C, 0x26A1, 0xFE0F}
EMOJI_RANGES = ((0x2600, 0x27BF), (0x1F300, 0x1FAFF))

BYTE_BUDGET = 8192


def ledger_section(text, header):
    """截取台账章节正文（从该章节标题到下一个章节标题）。"""
    start = text.index(header) + len(header)
    ends = [text.find(next_h, start) for next_h in SECTIONS + SECTIONS_EN
            if text.find(next_h, start) != -1]
    return text[start:min(ends) if ends else len(text)]


def emoji_codepoints(text):
    found = []
    for ch in text:
        cp = ord(ch)
        if any(lo <= cp <= hi for lo, hi in EMOJI_RANGES) or cp == 0xFE0F:
            found.append(cp)
    return found


class TestStructure(unittest.TestCase):
    def test_files_exist(self):
        for p in ("README.md", "README.en.md", "assets/moon.svg",
                  "scripts/generate_moon.py"):
            self.assertTrue((ROOT / p).exists(), p)

    def test_section_order(self):
        idx = [README.index(s) for s in SECTIONS]
        self.assertEqual(idx, sorted(idx), SECTIONS)
        idx_en = [README_EN.index(s) for s in SECTIONS_EN]
        self.assertEqual(idx_en, sorted(idx_en), SECTIONS_EN)

    def test_all_repositories_linked(self):
        for repo in REPOSITORIES:
            for text, name in ((README, "zh"), (README_EN, "en")):
                self.assertIn(REPO_PREFIX + repo + ")", text, f"{repo} missing in {name}")

    def test_creed_present(self):
        self.assertIn("人负责定义值得解决的问题", README)
        self.assertIn("真实证据决定保留什么", README)
        self.assertIn("Real evidence decides what survives", README_EN)

    def test_verdict_line_present(self):
        self.assertIn("✅ 至今无一行适用", README)
        self.assertIn("has never applied to a single row", README_EN)

    def test_colophon_present(self):
        self.assertIn("未立声明者不上墙", README)
        self.assertIn("Claims without a ledger entry stay off this page", README_EN)
        self.assertIn("生命会自己寻求出路", README)
        self.assertIn("LIFE FINDS A WAY", README)
        self.assertIn("LIFE FINDS A WAY", README_EN)

    def test_footer_right_aligned(self):
        for text, name in ((README, "zh"), (README_EN, "en")):
            self.assertIn('<div align="right">', text, name)


class TestStatusEmoji(unittest.TestCase):
    def test_vocabulary_present(self):
        for mark in STATUS_EMOJI:
            self.assertIn(mark, README, mark)
            self.assertIn(mark, README_EN, mark)

    def test_only_allowed_emoji(self):
        for text, name in ((README, "zh"), (README_EN, "en")):
            bad = set(emoji_codepoints(text)) - ALLOWED_CODEPOINTS
            self.assertFalse(bad, f"unexpected emoji in {name}: {bad}")

    def test_no_replicated_mark_on_ledger_rows(self):
        """✅ 是判决线：任何台账行都不得佩戴它。"""
        body = ledger_section(README, "## 声明台账")
        rows = [ln for ln in body.splitlines() if ln.startswith("- ")]
        self.assertEqual(len(rows), 8, f"expected 8 ledger rows, got {len(rows)}")
        for ln in rows:
            self.assertNotIn("✅", ln, ln[:40])

    def test_old_marks_are_gone(self):
        for old in ("●", "◐", "○", "✕", "⚡︎"):
            self.assertNotIn(old, README, old)
            self.assertNotIn(old, README_EN, old)


class TestMoonBoard(unittest.TestCase):
    def test_both_readmes_embed_moon(self):
        for text, name in ((README, "zh"), (README_EN, "en")):
            self.assertIn("](assets/moon.svg)", text, name)

    def test_board_carries_emoji_marks(self):
        for mark in ("🟡", "⚪", "❌"):
            self.assertIn(mark, MOON, mark)

    def test_board_is_generated_not_drawn(self):
        self.assertIn("OBSERVATION LOG", MOON)
        self.assertIn("月龄", MOON)

    def test_generator_computes_real_phase(self):
        self.assertIn("SYNODIC", GENERATOR)
        self.assertIn("math.cos", GENERATOR)
        self.assertIn("REF_NEW_MOON", GENERATOR)

    def test_workflow_redraws_daily(self):
        wf = (ROOT / ".github" / "workflows" / "moon.yml").read_text(encoding="utf-8")
        self.assertIn("cron:", wf)
        self.assertIn("generate_moon.py", wf)


class TestDiscipline(unittest.TestCase):
    def test_byte_budget(self):
        for text, name in ((README, "zh"), (README_EN, "en")):
            size = len(text.encode("utf-8"))
            self.assertLessEqual(size, BYTE_BUDGET, f"{name}: {size} bytes")

    def test_moon_svg_budget(self):
        size = len(MOON.encode("utf-8"))
        self.assertLessEqual(size, 32768, f"moon.svg: {size} bytes")


if __name__ == "__main__":
    unittest.main(verbosity=2)
