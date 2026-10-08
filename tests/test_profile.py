"""Offline structural checks for the published profile, not scientific project tests."""
import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'README.md').read_text(encoding='utf-8')
ASSETS = ROOT / 'assets' / 'playground'
EXPECTED = {
 'chat-distiller': 'chat-distiller', 'deep-native': 'deep-native',
 'flowcredit-research': 'flowcredit-research', 'rl-sentinel': 'RL-Sentinel',
 'go2w-mora': 'Go2w-MoRA-navigation', 'flowcredit': 'flowcredit',
}


class Tags(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class ProfileChecks(unittest.TestCase):
    def test_generated_assets_are_current(self):
        spec = importlib.util.spec_from_file_location('artwork', ROOT/'scripts/build_assets.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name, expected in module.build().items():
            with self.subTest(name=name):
                self.assertEqual((ASSETS/name).read_text(encoding='utf-8'), expected)

    def test_ten_well_formed_svgs(self):
        files = list(ASSETS.glob('*.svg'))
        self.assertEqual(len(files), 10)
        for file in files:
            with self.subTest(name=file.name):
                root = ET.parse(file).getroot()
                self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg')
                self.assertIsNotNone(root.find('{http://www.w3.org/2000/svg}title'))
                self.assertIsNotNone(root.find('{http://www.w3.org/2000/svg}desc'))
                self.assertIn('viewBox', root.attrib)

    def test_assets_have_no_active_or_external_content(self):
        for path in ASSETS.glob('*.svg'):
            source = path.read_text(encoding='utf-8')
            self.assertNotRegex(source, r'<(?:script|foreignObject|iframe|image)\b')
            self.assertNotRegex(source, r'\bon\w+\s*=')
            self.assertNotIn('javascript:', source.lower())
            self.assertNotIn('@import', source.lower())
            self.assertNotIn('@font-face', source.lower())
            self.assertNotRegex(source, r'url\(\s*[\'\"]?(?:https?:|data:)')

    def test_readme_has_no_unsupported_active_styling(self):
        self.assertNotRegex(README, r'<(?:script|style|iframe|svg)\b')
        self.assertNotRegex(README, r'\b(?:style|onclick|onload)\s*=')

    def test_illustrations_are_lightweight(self):
        sizes = [p.stat().st_size for p in ASSETS.glob('*.svg')]
        self.assertLess(max(sizes), 16000)
        self.assertLess(sum(sizes), 70000)

    def test_html_local_asset_references_exist(self):
        for tag, attrs in Tags(README).tags:
            for key in ('src', 'srcset'):
                value = attrs.get(key)
                if value:
                    self.assertTrue(value.startswith('assets/playground/'))
                    self.assertTrue((ROOT/value).is_file(), value)

    def test_markdown_local_references_exist(self):
        for dest in re.findall(r'\]\(([^)]+)\)', README):
            if not dest.startswith(('https://', '#')):
                self.assertTrue((ROOT/dest).is_file(), dest)

    def test_all_images_have_meaningful_alt(self):
        images = [attrs for tag,attrs in Tags(README).tags if tag == 'img']
        self.assertEqual(len(images), 7)
        for attrs in images:
            self.assertGreater(len(attrs.get('alt','')), 30)

    def test_project_destinations_match_covers(self):
        pairs = re.findall(r'<a href="([^"]+)"><img src="assets/playground/([^"/]+)\.svg"',README)
        self.assertEqual(len(pairs), 6)
        self.assertEqual(len({slug for _,slug in pairs}), 6)
        for href, slug in pairs:
            self.assertEqual(href, 'https://github.com/Anhao1314/'+EXPECTED[slug])

    def test_navigation_anchors_resolve(self):
        ids = {a['id'] for _, a in Tags(README).tags if 'id' in a}
        anchors = [a['href'][1:] for _, a in Tags(README).tags if a.get('href','').startswith('#')]
        self.assertEqual(len(anchors), 3)
        for anchor in anchors:
            self.assertIn(anchor, ids)

    def test_disclosures_and_text_fallback(self):
        self.assertEqual(README.count('<details>'), 4)
        self.assertEqual(README.count('</details>'), 4)
        self.assertEqual(README.count('<summary>'), 4)
        self.assertIn('text-only project index', README)

    def test_static_covers_have_no_animation(self):
        for theme in ('light','dark'):
            source = (ASSETS/f'hero-{theme}-static.svg').read_text(encoding='utf-8')
            self.assertNotIn('@keyframes', source)
            self.assertNotIn('animation:', source)

    def test_motion_ends_before_five_seconds(self):
        for theme in ('light','dark'):
            source = (ASSETS/f'hero-{theme}.svg').read_text(encoding='utf-8')
            self.assertNotIn('infinite', source)
            declarations = re.findall(r'animation:(\w+) ([\d.]+)s [\w-]+ (\d+);',source)
            self.assertEqual(len(declarations), 3)
            for _,duration,iterations in declarations:
                self.assertLessEqual(float(duration)*int(iterations), 4.8)
            self.assertIn('@media(prefers-reduced-motion:reduce)', source)
            self.assertIn('animation:none!important', source)

    def test_picture_has_theme_and_motion_fallbacks(self):
        sources=[a for t,a in Tags(README).tags if t=='source']
        self.assertEqual(len(sources), 3)
        self.assertTrue(sources[0]['srcset'].endswith('hero-dark.svg'))
        self.assertTrue(sources[1]['srcset'].endswith('hero-light.svg'))
        self.assertTrue(sources[2]['srcset'].endswith('hero-dark-static.svg'))
        fallback = next(a for t,a in Tags(README).tags if t == 'img')
        self.assertTrue(fallback['src'].endswith('hero-light-static.svg'))
        self.assertIn('prefers-reduced-motion: no-preference', sources[0]['media'])
        self.assertIn('prefers-reduced-motion: no-preference', sources[1]['media'])

    def test_student_and_research_boundaries_remain(self):
        for phrase in ['AI undergraduate','2027','Simulation research','not a live activity feed','did not show a quality improvement','not calibrated lending decisions']:
            self.assertIn(phrase, README)

    def test_no_external_stats_widgets(self):
        for host in ['shields.io','readme-typing-svg','github-stats-alpha','github-profile-summary-cards']:
            self.assertNotIn(host, README)


if __name__=='__main__':
    unittest.main()
