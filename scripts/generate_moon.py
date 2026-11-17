#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_moon.py — 生成主页唯一的图片：1-bit 像素观测板（月亮 + 观测窗）

设计语言采样自月之暗面招聘站：纯黑板、Bayer 抖动像素月、像素星空、
等宽字体、终端式角标。月相按真实日期计算——页面上没有一样东西在冒充现状。

用法: python generate_moon.py [--date 2026-11-18] [--out moon.svg]
落地版将读取 claims.yaml；演示版数据内置。
"""
import argparse
import math
import random
from datetime import date, datetime, timezone

# ---------- 月相 ----------
REF_NEW_MOON = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
SYNODIC = 29.530588853

def moon_phase(d: date):
    dt = datetime(d.year, d.month, d.day, 12, 0, tzinfo=timezone.utc)
    age = ((dt - REF_NEW_MOON).total_seconds() / 86400.0) % SYNODIC
    phase = age / SYNODIC                      # 0=新月 0.5=满月
    illum = (1 - math.cos(2 * math.pi * phase)) / 2
    return age, phase, illum

# ---------- 抖动 ----------
BAYER4 = [
    [0, 8, 2, 10],
    [12, 4, 14, 6],
    [3, 11, 1, 9],
    [15, 7, 13, 5],
]

def thresh(gx: int, gy: int) -> float:
    return (BAYER4[gy % 4][gx % 4] + 0.5) / 16.0

# ---------- 画布 ----------
W, H = 1200, 300
PANEL = "#050505"        # 观测板底色（永远纯黑，不随 GitHub 主题翻转）
BORDER = "#262626"
INK = "#f2f2f2"          # 亮点
MUT = "#c2c2c2"          # 次级文字
DIM = "#9a9a9a"          # 装饰
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,'Courier New',monospace"

MOON_CX, MOON_CY, MOON_R, CELL = 1050, 158, 88, 5
AXIS_Y = 158
AXIS_X0, AXIS_X1 = 48, 928
WIN_START = date(2026, 8, 1)
SILENCE = "此前沉默 22 个月"

# 变更事件（offset 天, 状态）——落地版从 claims.yaml 生成
EVENTS = [
    (16, "◐"), (21, "◐"), (37, "◐"), (43, "○"), (50, "◐"),
    (65, "○"), (66, "○"), (70, "○"), (75, "✕"), (78, "◐"),
    (80, "✕"), (87, "◐"), (95, "◐"),
]

# 月海（相对月心，单位 r：dx, dy, 半径）——亮度压暗
MARE = [(-0.22, -0.14, 0.30), (0.16, 0.22, 0.24), (-0.10, 0.30, 0.16),
        (0.32, -0.30, 0.18), (-0.02, -0.36, 0.13), (0.10, 0.02, 0.10)]
MARE_DIM = 0.42

def luminance(px, py, phase):
    """像素格中心在月面坐标系下的亮度：0.92=月面亮部 0=月海/阴影/空。"""
    dx, dy = px - MOON_CX, py - MOON_CY
    dist = math.hypot(dx, dy)
    if dist > MOON_R * 0.995:
        return 0.0
    lum = 0.92
    for mx, my, mr in MARE:                 # 月海 = 实心暗斑
        if math.hypot(dx - mx * MOON_R, dy - my * MOON_R) < mr * MOON_R:
            lum = 0.0
            break
    # 相位阴影：盈月亮部在右。terminator 椭圆 rx = r·|cos(2πp)|
    c = math.cos(2 * math.pi * phase)
    rx_t = abs(c) * MOON_R
    in_term = (dx / rx_t) ** 2 + (dy / MOON_R) ** 2 <= 1 if rx_t > 1e-6 else False
    if phase < 0.5:                          # 盈：左侧为阴影
        shadow = (dx < 0) and not in_term
    else:                                    # 亏：右侧为阴影
        shadow = (dx > 0) and not in_term
    return 0.0 if shadow else lum

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")

def build(today: date) -> str:
    age, phase, illum = moon_phase(today)
    span = (today - WIN_START).days
    px_per_day = (AXIS_X1 - AXIS_X0) / span
    n_claims = 8

    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img" aria-label="观测板：今天的月亮与声明观测窗。'
        f'月相按真实日期计算，由 Actions 每日重绘。">'
    )
    # 面板与终端角标
    out.append(f'<rect width="{W}" height="{H}" fill="{PANEL}"/>')
    out.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" fill="none" stroke="{BORDER}"/>')
    for (x, y, dx, dy) in [(14,14,14,0),(14,14,0,14),(W-14,14,-14,0),(W-14,14,0,14),
                           (14,H-14,14,0),(14,H-14,0,-14),(W-14,H-14,-14,0),(W-14,H-14,0,-14)]:
        out.append(f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{INK}" stroke-width="2"/>')

    # 像素星空（固定种子，避开月亮）
    rng = random.Random(20260817)
    for _ in range(130):
        sx, sy = rng.uniform(24, W - 24), rng.uniform(30, H - 40)
        if math.hypot(sx - MOON_CX, sy - MOON_CY) < MOON_R + 16:
            continue
        if abs(sy - AXIS_Y) < 14 and sx < MOON_CX - 20:
            continue
        size = rng.choice((1.4, 1.8, 2.2))
        op = rng.uniform(0.18, 0.6)
        out.append(f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{size}" height="{size}" fill="{INK}" fill-opacity="{op:.2f}"/>')

    # 头部：mono 标签
    out.append(f'<text x="28" y="46" font-family="{MONO}" font-size="17" letter-spacing="2" fill="{INK}">EASON · OBSERVATION LOG</text>')
    out.append(f'<text x="28" y="70" font-family="{MONO}" font-size="15" fill="{MUT}">'
               f'{WIN_START.isoformat()} → {today.isoformat()} · {len(EVENTS)} EVENTS · {n_claims} CLAIMS</text>')
    out.append(f'<text x="{W-28}" y="46" font-family="{MONO}" font-size="17" fill="{INK}" text-anchor="end">&gt;&gt;&gt; 现在</text>')

    # 观测窗轴（像素化方点虚线）
    out.append(f'<line x1="{AXIS_X0}" y1="{AXIS_Y-16}" x2="150" y2="{AXIS_Y-16}" stroke="{DIM}" stroke-width="1.5" stroke-dasharray="2 6"/>')
    out.append(f'<text x="{AXIS_X0}" y="{AXIS_Y-26}" font-family="{MONO}" font-size="15" fill="{MUT}">{SILENCE}</text>')
    out.append(f'<line x1="{AXIS_X0}" y1="{AXIS_Y}" x2="{AXIS_X1}" y2="{AXIS_Y}" stroke="#b9b9b9" stroke-width="2"/>')
    for off in (31, 61, 92):
        x = AXIS_X0 + off * px_per_day
        out.append(f'<line x1="{x:.0f}" y1="{AXIS_Y-9}" x2="{x:.0f}" y2="{AXIS_Y+9}" stroke="#b9b9b9" stroke-width="1.5"/>')
        label = ("9月", "10月", "11月")[(31, 61, 92).index(off)]
        out.append(f'<text x="{x:.0f}" y="{AXIS_Y+27}" font-family="{MONO}" font-size="15" fill="{MUT}" text-anchor="middle">{label}</text>')
    out.append(f'<text x="{AXIS_X0}" y="{AXIS_Y+27}" font-family="{MONO}" font-size="15" fill="{MUT}">{WIN_START.strftime("%m-%d")}</text>')

    # 事件标记：emoji（与声明台账同一套记号），沿轴上下交错避免相邻重叠
    EMOJI = {"◐": "🟡", "○": "⚪", "✕": "❌"}
    emoji_font = "'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif"
    for i, (off, mark) in enumerate(EVENTS):
        x = AXIS_X0 + off * px_per_day
        dy = -12 if i % 2 == 0 else 12
        out.append(f'<text x="{x:.0f}" y="{AXIS_Y+dy:.0f}" font-family="{emoji_font}" font-size="15" '
                   f'text-anchor="middle" dominant-baseline="central">{EMOJI[mark]}</text>')

    # 像素月亮：Bayer 抖动，连续段合并成 rect
    g0 = int(MOON_CY - MOON_R) - CELL
    g1 = int(MOON_CY + MOON_R) + CELL
    rects = []
    for gy in range(g0, g1, CELL):
        run = None
        for gx in range(int(MOON_CX - MOON_R) - CELL, int(MOON_CX + MOON_R) + CELL, CELL):
            cx, cy = gx + CELL / 2, gy + CELL / 2
            lum = luminance(cx, cy, phase)
            on = lum > thresh(int((gx - MOON_CX) / CELL + 40), int((gy - MOON_CY) / CELL + 40))
            x, y = round(gx, 1), round(gy, 1)
            if on:
                if run is None:
                    run = [x, y, x + CELL]
                else:
                    run[2] = x + CELL
            else:
                if run is not None:
                    rects.append((run[0], run[1], run[2] - run[0], CELL))
                    run = None
        if run is not None:
            rects.append((run[0], run[1], run[2] - run[0], CELL))
    for x, y, w, h in rects:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{INK}"/>')

    # 注记
    out.append(f'<text x="{MOON_CX}" y="{MOON_CY+MOON_R+36}" font-family="{MONO}" font-size="15" fill="{MUT}" text-anchor="middle">'
               f'月龄 {age:.1f} 天 · 照度 {illum*100:.0f}%</text>')
    out.append(f'<text x="28" y="{H-16}" font-family="{MONO}" font-size="15" fill="{MUT}">本页唯一的图片 · 月相真实 · Actions 每日重绘</text>')
    out.append("</svg>")
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD，默认今天（本地）")
    ap.add_argument("--out", default="moon.svg")
    a = ap.parse_args()
    d = date.fromisoformat(a.date) if a.date else date.today()
    svg = build(d)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"written {a.out}  date={d}  size={len(svg)} bytes")

if __name__ == "__main__":
    main()
