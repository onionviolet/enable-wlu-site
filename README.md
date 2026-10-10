# e-NABLE at W&L website

Type: CURRENT-STATE. Audience: group organizers and website maintainers.

A static HTML/CSS page in `docs/`, with small vanilla JavaScript and no build step, accounts, trackers or backend. **The October 10, 2026 design is a working draft pending owner acceptance.** It refines the baseline layout: the group leads, with a W&L student headline in self-hosted Source Serif 4, a short intro and the Instagram link beside the team photo (stacked on phones). The attributed e-NABLE mission quote sits beneath as secondary context. Below are three large candid photos of members at work, then a sideways-scrolling gallery of four build photos and a visitor-controlled video, with no visible captions, then FAQ, Contact and the footer. Cream, navy and amber remain; simpler photo presentation lets the work speak for itself.

The quote describes the global e-NABLE community. The introduction identifies this group as W&L students learning to build prosthetic hands with e-NABLE's free, open-source designs. The site makes no claims about recipients, deliveries, build counts, chapter listing, university recognition, endorsement or partnerships. Instagram is the only contact route; a monitored inbox and meeting schedule are not confirmed.

The existing public address is https://onionviolet.github.io/enable-wlu-site/. GitHub Pages serves `docs/`. This revision is saved locally, **not committed, pushed or deployed**. After a future authorized push, check the Pages deployment before treating the public page as updated.

The complete pre-edit `docs/` copy is preserved in `archive/v3-polish-draft-2026-10-09/`. Earlier concepts and review notes are historical, not current design direction. Current screenshots, results and open questions are in [research/phase2/REVIEW.md](research/phase2/REVIEW.md). Research and archives are gitignored local evidence.

## Preview and review

```sh
python3 -m http.server 8770 --bind 127.0.0.1 --directory docs
```

Open http://127.0.0.1:8770/. Review at 320, 390 and 1440 px. Tab through links, native video controls and FAQ summaries. Press Enter on a summary to open or close it. Check reduced motion and JavaScript disabled; every photograph should remain visible. The page stays light when the device prefers dark mode.

With Python Playwright and installed Google Chrome, run `python3 research/tools/check_phase2.py` while the server is running. It saves fold/full-page, focus, FAQ, reduced-motion and JavaScript-disabled captures plus measurements in `research/phase2/`. Inspect the screenshots as well as `checks.json`; native video controls have internal keyboard stops that appear as `VIDEO` in the DOM focus log.

## Routine editing

- **Copy and facts:** edit `docs/index.html`. Keep the student headline first and the mission visibly quoted and attributed to [Enabling the Future](https://enablingthefuture.org/) beneath it. Preserve the FAQ facts and the distinction between the global community and this initiative.
- **Contact:** keep both profile links set to `https://www.instagram.com/enablewlu/`, verified from the organizer's screenshot October 9, 2026. Do not promise DM responses or invent a meeting time or email.
- **Photos and sharing:** see [MEDIA.md](MEDIA.md) for provenance, consent, captions and file locations. Gallery images use `loading="lazy"`, `srcset`, `sizes` and intrinsic dimensions. Portrait filenames ending in `-800` and `-1600` have actual widths of 600 and 1200 px; use actual widths in `srcset`. Photos have no visible captions (removed October 10 because draft wording could be wrong); keep `alt` text to what is visible. The team photo remains the share image; update `og:image` and `og:image:alt` if it changes.
- **Layout and type:** edit `docs/styles.css`. The gallery is one sideways-scrolling row with scroll snapping: photos keep their proportions at a fixed height (380 px desktop, 300 px phones, capped at 78vw on phones so the next photo peeks in). Add a photo by adding another `figure.build-photo` inside `.gallery`. Body and supporting text are at least 16 px. Source Serif 4 Regular is self-hosted in `docs/fonts/` with its SIL Open Font License; `font-synthesis: none` prevents artificial bold and italic. No fonts or other third-party assets are requested.
- **Motion and video:** `docs/site.js` adds previous/next buttons under the gallery (the gallery still scrolls by touch, trackpad and keyboard without JS) and uses IntersectionObserver to gently reveal offscreen gallery figures once. It adds the concealment class only when an observer exists; default HTML/CSS is visible without JS. Reduced motion bypasses the observer, disables authored animation/transition/hover effects, and restores photos if the preference changes. Hero entry, photo brightness on hover and progressive native FAQ opening are CSS. Browsers without disclosure animation support still open FAQ normally. Keep video `controls`, `playsinline`, `preload="none"` and its poster; no autoplay or scripted playback.

## Officer handover

Recommended, not established: put GitHub and Instagram under group-controlled ownership, give incoming officers individual access where supported, and keep recovery details in the group's private records. Before handover, document the current owner, collaborators, recovery contact, who checks messages and who can publish. Have the next officer make and preview one small edit before the outgoing officer leaves. Transfer access deliberately; do not put passwords, planning-vault notes or private recipient details in this repository.
