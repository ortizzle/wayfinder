# tools/ — the verification and content pipeline

These lived in per-session scratch space until v74, which meant they died with
the session and got rebuilt from memory each time — slightly differently. Now
they live with the app they verify. **Nothing in here ships**: the service
worker's shell is a fixed list and never includes `tools/`.

## Running the tests

Everything drives the real app in a real Chromium via Playwright.

```sh
npm i playwright            # once, anywhere on the machine
node tools/serve.js . 8123  # serve the app (python http.server drops
                            # connections under the SW's fetch pattern)
node tools/sweep.js 8123 wayfinder        # every screen, seeded
node tools/sweep_fresh.js 8123 wayfinder  # every screen, fresh install
node tools/test_batch6.js 8123 wf        # growth chips, diff view, ramp, swbar…
node tools/test_swflow.js 8123 .         # the real SW update flow (bumps sw.js
                                         # on disk and restores it afterwards)
node tools/contrast_batch6.js 8123       # accent × sky × theme on new surfaces
```

Chromium path: set `CHROMIUM_PATH` if yours is not `/opt/pw-browsers/chromium`.

## Hard-won rules encoded in these scripts

- **Measure against the opaque surface underneath.** Chrome reports accent
  tints as `color(srgb … / 0.08)`; a naive probe reads that as opaque and the
  ratios come out wildly wrong.
- **Kill transitions before reading colours.** `.tool` transitions its
  `color`, so `getComputedStyle` right after a theme flip returns the
  interpolated value — a probe once reported 3.11:1 for a surface that
  measures 5.75:1 at rest.
- **Assert the probe's knob actually turned.** Set `--ac` / `data-theme`
  directly on `documentElement` and verify it took; routing through `prefs()`
  once silently did nothing and reported one ratio twelve times as a pass.
- **Don't wait on `load` after a SW swap** — a hung third-party fetch can hold
  it open forever. Wait on the committed navigation plus observable state.

## builders/

Shared Python for content files: `unit_common.py` (generic units),
`math_common.py` (Accelerated Math lessons and topic reviews — remember
`sround()`: the school rounds 5 up, Python does not), `ww_common.py`
(Wordly Wise Book 5), and
`check_content.py`, which validates every file in `content/` against the
rules in CLAUDE.md — run it before shipping any content change:

```sh
python3 tools/builders/check_content.py
```
