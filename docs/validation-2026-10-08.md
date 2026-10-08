# Profile validation: 2026-10-08

Scope: Eason's Playground README and original SVG assets. These checks do not validate the scientific performance of the featured projects.

## Local results

- `python scripts/build_assets.py --check`: all 10 SVGs match their source generator.
- `python -m unittest discover -s tests -v`: 16 tests passed.
- Local Chromium rendering: 20 assertions passed after the reduced-motion fix.
- Total SVG payload: 35,936 bytes. No remote fonts, tracking pixels or statistics widgets.

The 20 browser assertions comprise four checks across each of four configurations (light/dark theme crossed with reduced/normal motion): seven images load, the correct cover is selected, the six project covers form three two-column rows without overflow, and four disclosure panels work from the keyboard. Four additional checks cover text bounds in all 10 SVGs, actual motion observed through raster differences, motion settling after 4.8 seconds, and static reduced-motion output through the shipping picture element.

The representative desktop preview uses a 1,280-pixel viewport and a GitHub-like Markdown content area. The preview is not a pixel-identical copy of GitHub's production renderer. No mobile-specific redesign was claimed.

## Retained negative result and correction

An initial isolated animated SVG, embedded as a data-URI image, still changed between raster frames under Chromium's emulated reduced-motion preference. Relying only on the SVG's internal media query was therefore rejected as the accessibility control.

The README now defaults to an animation-free cover. Explicit no-preference picture sources opt into motion; reduced-motion readers receive a separate static SVG. The revised shipping picture element passed selection and raster checks. The original failure is not counted as a passing test.

## External verification boundary

Direct Git access from the local execution environment failed DNS resolution, and its browser rejected navigation to GitHub with `ERR_BLOCKED_BY_ADMINISTRATOR`. GitHub connector API reads and writes are a separate, available path.

Local screenshots must be labeled as local previews. A successful API commit/readback proves repository state, not that GitHub's image proxy and production browser rendering were visually inspected. Remote CI results must be reported from the actual GitHub run, separately from the local checks above.
