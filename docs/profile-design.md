# Eason's Playground

A student-first GitHub profile: curious, playful and readable, with the technical detail one click away. This is a README redesign, not a separate website.

## Visual system

Cream `#FFF8ED`, ink `#25233D`, cobalt `#4D5BF4`, lime `#DDF484`, coral `#FFAB95` and lilac `#C9B7FF`. A large typographic introduction, an original headphone-wearing robot and six illustrated project covers replace the previous badge-heavy layout. Covers use the same geometry and type scale but distinct motifs. All charts and icons are decorative, not experimental evidence.

The artwork uses built-in font fallbacks. No font files, remote images, third-party statistics service or secrets are needed. Existing unrelated repository assets are preserved. The old README remains available through Git history.

## GitHub-native interaction

- Clickable covers and section anchors.
- Four keyboard-operable native `details` panels, including a text-only project index.
- Light/dark covers selected through `picture`; full-color cards work in either theme.
- A brief SVG float, blink and star animation. Every animation ends within 4.8 seconds. It does not loop forever. Reduced-motion readers receive static artwork through explicit picture source selection and direct static links. The default image is static; animation is opt-in through the no-preference media condition.

This is not an interactive Canvas app: GitHub does not execute arbitrary README JavaScript. No hover effects, custom theme buttons, live agent status, music or cursor tracking are claimed. The avatar, account biography and GitHub's native pinned-repository settings are outside this repository change.

## Edit and verify

Python 3.10+; the generation and validation paths need only the standard library.

```sh
python3 scripts/build_assets.py
python3 scripts/build_assets.py --check
python3 -m unittest discover -s tests -v
```

Edit artwork in `scripts/build_assets.py`, not the generated SVGs. Edit descriptive copy in `README.md`. The workbench is explicitly hand-curated. Update it after reviewing the linked repositories; never infer scientific progress from commit count.

CI checks committed artwork, file safety, motion limits, local references, navigation and project destinations. It does not measure model quality or claim that a robot is safe. It is read-only and never generates activity commits.

## Review scope

Local Chromium checks can establish typography bounds, image loading, motion, reduced-motion behavior, disclosure interaction and a representative README layout. They do not by themselves prove pixel-identical rendering through GitHub's production sanitizer, theme settings or image proxy.

Production verification must distinguish a successful GitHub API readback from an actual browser inspection of the public profile. Do not describe a local preview as a live GitHub screenshot.

## Content boundaries

Student status and expected 2027 graduation come from the existing profile. Project links are retained from that profile; G1 is a current-work link rather than a seventh featured cover. Deep Native's negative pilot is retained in the copy. G1 is described as simulation research, and FlowCredit as an experimental risk API. There are no invented usage, revenue, benchmark or success-rate figures.

The previous external portfolio navigation is not featured in this version because its availability was not verified. It can be restored after checking the destination. No private contact information was added.

## Platform references

- [Theme-aware README images](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/)
- [Native collapsed sections](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections)

## Retained browser finding

The first exploratory raster test of an animated SVG embedded directly as a data-URI `img` did not stay static under Chromium's emulated reduced-motion preference. The internal SVG media query alone is therefore **not** treated as a verified accessibility control. The shipping README instead selects a separate, animation-free SVG in `picture`, and defaults to a static image when no source matches. Reduced-motion selection is checked at the rendered README level. The internal CSS remains only defense in depth.
