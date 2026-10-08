#!/usr/bin/env python3
"""Build the profile's original, self-contained SVG artwork using only Python stdlib."""
from html import escape
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'playground'
FONT = 'Arial, Helvetica, sans-serif'
MONO = "'Courier New', monospace"
INK = '#25233D'
BLUE = '#4D5BF4'


def text(x, y, value, size=20, fill=INK, weight=400, mono=False, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(value)}</text>'


def svg(body, width, height, title, desc, css=''):
    style = f'<style>{css}</style>' if css else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
{style}
{body}
</svg>\n'''


def star(cx, cy, color, scale=1):
    return f'<g transform="translate({cx} {cy}) scale({scale})"><path d="M0 -32L8 -10L30 -17L16 1L31 17L9 13L0 34L-8 12L-30 18L-17 0L-30 -17L-8 -10Z" fill="{color}" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/></g>'


def hero(dark=False, still=False):
    bg, fg, muted, line = ('#202235', '#FFF8EC', '#C9C5D8', '#4B4D64') if dark else ('#FFF8ED', INK, '#686078', '#DDD6C8')
    blue = '#AFB5FF' if dark else BLUE
    css = '' if still else '''
.bob{animation:bob 2.4s ease-in-out 2;transform-box:fill-box;transform-origin:center}
.blink{animation:blink 4.8s linear 1;transform-box:fill-box;transform-origin:center}
.spark{animation:spark 4.8s ease-in-out 1;transform-box:fill-box;transform-origin:center}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@keyframes blink{0%,34%,39%,76%,81%,100%{transform:scaleY(1)}36%,78%{transform:scaleY(.12)}}
@keyframes spark{0%,100%{transform:rotate(0deg)}50%{transform:rotate(24deg)}}
@media(prefers-reduced-motion:reduce){.bob,.blink,.spark{animation:none!important}}
'''
    body = f'''<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{line}"/></pattern></defs>
<rect x="1" y="1" width="1198" height="518" rx="28" fill="{bg}" stroke="{line}" stroke-width="2"/>
<path d="M748 1H1172Q1199 1 1199 28V466H748Z" fill="url(#dots)"/>
{ text(52,46,'EASON / PLAYGROUND',16,fg,700,True, 'letter-spacing="2"') }
{ text(52,82,'A SMALL CORNER FOR BIG WHAT-IFS.',12,muted,400,True, 'letter-spacing="1.2"') }
<g transform="translate(397 62) rotate(-5)"><rect x="0" y="0" width="198" height="38" rx="8" fill="#DDF484" stroke="{INK}" stroke-width="2"/>{text(15,25,"AI STUDENT / '27",14,INK,700,True)}</g>
{ text(48,178,"Hey, I'm",75,fg,700,False,'letter-spacing="-4"') }
{ text(44,283,'Eason.',132,blue,800,False,'letter-spacing="-7"') }
<path d="M55 304Q187 286 356 305" stroke="#FF907A" stroke-width="9" fill="none" stroke-linecap="round"/>
{ text(52,355,'A little code. A lot of curiosity.',27,fg,700) }
{ text(52,391,'Agents, robots & ideas that escaped my notes.',20,muted) }
<g transform="translate(809 60) rotate(6)"><rect width="244" height="44" rx="8" fill="#FFAB95" stroke="{INK}" stroke-width="2"/>{text(22,29,'ALWAYS IN BETA :)',18,INK,700,True)}</g>
<ellipse cx="951" cy="305" rx="185" ry="159" fill="#DDF484" transform="rotate(-12 951 305)"/>
<ellipse cx="951" cy="433" rx="119" ry="13" fill="{INK}" opacity=".12"/>
<g transform="translate(790 131)"><g class="bob">
<path d="M163 16V-7" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<circle cx="163" cy="-15" r="12" fill="#FFAB95" stroke="{INK}" stroke-width="4"/>
<path d="M57 88V65C57 1 269 1 269 65V88" fill="none" stroke="{INK}" stroke-width="18"/>
<path d="M57 88V65C57 1 269 1 269 65V88" fill="none" stroke="{BLUE}" stroke-width="12"/>
<path d="M112 208Q72 214 67 238" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
<path d="M217 207Q267 208 285 162" fill="none" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>
<rect x="104" y="182" width="122" height="88" rx="27" fill="#FFAB95" stroke="{INK}" stroke-width="4"/>
<path d="M135 270L129 290M196 270L204 290" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>
<rect x="95" y="282" width="60" height="25" rx="12" fill="{BLUE}" stroke="{INK}" stroke-width="4" transform="rotate(-7 125 294)"/>
<rect x="181" y="282" width="60" height="25" rx="12" fill="{BLUE}" stroke="{INK}" stroke-width="4" transform="rotate(7 211 294)"/>
<rect x="58" y="41" width="212" height="143" rx="48" fill="#FFFEF9" stroke="{INK}" stroke-width="4"/>
<rect x="80" y="64" width="168" height="92" rx="29" fill="{INK}"/>
<g class="blink"><rect x="110" y="89" width="15" height="26" rx="7" fill="#DDF484"/><rect x="202" y="89" width="15" height="26" rx="7" fill="#DDF484"/></g>
<path d="M151 118Q165 132 179 118" fill="none" stroke="#DDF484" stroke-width="4" stroke-linecap="round"/>
<rect x="41" y="86" width="28" height="54" rx="12" fill="{BLUE}" stroke="{INK}" stroke-width="4"/>
<rect x="260" y="86" width="28" height="54" rx="12" fill="{BLUE}" stroke="{INK}" stroke-width="4"/>
<path d="M65 233Q45 229 46 245Q46 260 66 255Q82 256 83 244Q82 231 65 233Z" fill="#FFFEF9" stroke="{INK}" stroke-width="4"/>
<path d="M273 162L270 145Q270 137 277 140L282 148L281 130Q282 124 288 128L292 143L299 130Q304 126 307 132L303 150Q314 142 317 151Q313 171 294 178Z" fill="#FFFEF9" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
<path d="M164 202L170 218L187 219L174 230L178 247L164 238L150 247L154 230L141 219L158 218Z" fill="#FFFEF9" stroke="{INK}" stroke-width="2"/>
</g></g>
<g transform="translate(716 182)"><g class="spark">{star(0,0,'#C9B7FF',.83)}</g></g>
{star(1120,381,'#FFAB95',.62)}
<path d="M686 358Q704 407 757 408M744 395L759 408L744 419" fill="none" stroke="{blue}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{ text(1064,230,'+ +',23,INK,700,True) }
<path d="M30 465H1170" stroke="{line}" stroke-width="1.5"/>
{ text(52,497,'LEARN / BUILD / BREAK / REPEAT',14,muted,700,True,'letter-spacing="1"') }
{ text(917,497,'WORK IN PROGRESS',14,muted,700,True,'letter-spacing="1"') }
'''
    return svg(body,1200,520,"Hey, I'm Eason. AI student, class of 2027.", 'A cream and cobalt playground with a friendly headphone-wearing robot, a star and handwritten-style stickers. Decorative motion plays once and settles in under five seconds. No live status is implied.',css)


def icon(kind):
    common = f'stroke="{INK}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"'
    icons = {
    'memory': '<rect x="6" y="4" width="51" height="42" rx="9" fill="#FFF9EF"/><path d="M17 18H44M17 28H37M24 46L16 56V45" fill="none"/><rect x="30" y="38" width="36" height="30" rx="7" fill="#C9B7FF"/><path d="M39 49H57M39 58H50"/>',
    'runtime':'<rect x="2" y="5" width="66" height="53" rx="9" fill="#FFF9EF"/><path d="M2 20H68M14 34L22 41L14 48M32 47H46" fill="none"/><circle cx="12" cy="13" r="1"/><circle cx="20" cy="13" r="1"/><circle cx="57" cy="57" r="14" fill="#DDF484"/><path d="M52 51L62 57L52 63Z" fill="#25233D" stroke="none"/>',
    'evidence':'<rect x="11" y="2" width="44" height="57" rx="6" fill="#FFF9EF" transform="rotate(-8 33 30)"/><path d="M21 16H41M21 26H43M21 36H36" fill="none"/><circle cx="49" cy="46" r="17" fill="#FFAB95"/><path d="M61 58L70 69M41 46L47 52L58 40" fill="none"/>',
    'replay':'<path d="M9 16A28 28 0 1 1 3 46M9 16V3M9 16H23" fill="none"/><path d="M19 37H28L35 20L43 51L50 34H61" fill="none"/><circle cx="35" cy="37" r="3" fill="#82BDFF" stroke="none"/>',
    'robot':'<path d="M7 37H67M18 27L26 16H50L59 29" fill="none"/><rect x="13" y="25" width="51" height="24" rx="7" fill="#FFF9EF"/><path d="M28 27V14M48 26V15" fill="none"/><circle cx="23" cy="54" r="10" fill="#F5CD57"/><circle cx="56" cy="54" r="10" fill="#F5CD57"/><circle cx="50" cy="35" r="3" fill="#25233D" stroke="none"/><path d="M3 68H68" stroke-dasharray="4 6"/>',
    'api':'<path d="M36 3L61 13V34Q60 52 36 65Q12 52 11 34V13Z" fill="#FFF9EF"/><path d="M30 23L21 33L30 43M43 23L52 33L43 43" fill="none"/><circle cx="62" cy="57" r="12" fill="#C9B7FF"/><path d="M57 57L61 61L68 53" fill="none"/>'
    }
    return f'<g {common}>{icons[kind]}</g>'


PROJECTS = [
 ('chat-distiller','01 / AGENT CONTINUITY','CarryTrace','Your work continues.','Keep the evidence attached.','SKILL / CONTEXT / RECOVERY','#EDE6FF','memory'),
 ('deep-native','02 / CODING AGENTS','Deep Native','A lighter way to code with AI.','Inspect, experiment, verify.','SKILLS / DEEPSEEK / TOOLING','#ECF4CF','runtime'),
 ('flowcredit-research','03 / RESEARCH TOOLS','FlowCredit Research','Follow the idea.','Keep the evidence attached.','MEMORY / EVIDENCE / REASONING','#FFE2D5','evidence'),
 ('rl-sentinel','04 / REINFORCEMENT LEARNING','RL Sentinel','Rewind the run.','Understand the recommendation.','PYTHON / REPLAY / EXPERIMENTS','#DFEFFF','replay'),
 ('go2w-mora','05 / ROBOTICS','Go2W MoRA','Small robot.','Interesting navigation problems.','MUJOCO / PYTORCH / PPO','#FFF0BD','robot'),
 ('flowcredit','06 / API EXPERIMENTS','FlowCredit','From scattered evidence','to inspectable risk signals.','NODE.JS / RISK / API','#ECE8E0','api'),
]


def card(project):
    slug,label,name,one,two,tech,bg,kind = project
    title_size=32 if len(name)>16 else 36
    body=f'''<rect x="1" y="1" width="568" height="258" rx="18" fill="{bg}" stroke="{INK}" stroke-width="2"/>
{text(27,34,label,12,INK,700,True,'letter-spacing=".7"')}
{text(26,87,name,title_size,INK,700,False,'letter-spacing="-1"')}
{text(28,126,one,19,INK)}
{text(28,154,two,19,INK)}
<g transform="translate(465 84)">{icon(kind)}</g>
<path d="M27 191H543" stroke="{INK}" stroke-width="1" opacity=".25"/>
{text(28,226,tech,12,INK,700,True)}
<circle cx="525" cy="220" r="15" fill="{INK}"/>
<path d="M519 226L531 214M520 214H531V225" fill="none" stroke="{bg}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
'''
    return svg(body,570,260,f'{name}: {one} {two}',f'Project cover. {label}. The illustration is decorative, not a measured result. Click the surrounding link to open the repository.')


def build():
    assets = {f'hero-{theme}{suffix}.svg':hero(dark=theme=='dark',still=bool(suffix)) for theme in ('light','dark') for suffix in ('','-static')}
    assets.update({f'{p[0]}.svg':card(p) for p in PROJECTS})
    return assets


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if committed artwork differs from the generator.')
    args=parser.parse_args()
    assets=build()
    if args.check:
        bad=[name for name,content in assets.items() if not (OUT/name).exists() or (OUT/name).read_text(encoding='utf-8') != content]
        if bad:
            raise SystemExit('Out-of-date artwork: '+', '.join(bad))
        print(f'{len(assets)} SVGs match their source generator.')
    else:
        OUT.mkdir(parents=True,exist_ok=True)
        for name,content in assets.items():
            (OUT/name).write_text(content,encoding='utf-8')
        print(f'Built {len(assets)} self-contained SVGs.')


if __name__=='__main__':
    main()
