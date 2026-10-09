# e-NABLE at W&L website

Type: CURRENT-STATE. Audience: group organizers and website maintainers.

A short, plain HTML/CSS page in `docs/`, with system light/dark mode. No build step, accounts, trackers or backend. The October 9, 2026 revision uses the agreed workshop paper/navy direction: a broad student introduction, one team photo, an Instagram profile link and FAQ on a smooth paper background. The latest user direction removes the count, project details, dated updates, extra media and community-logo block from the page for now. Earlier drafts remain locally in `archive/`.

The existing public address is https://onionviolet.github.io/enable-wlu-site/. GitHub Pages serves `docs/`. After pushing to `main`, check the Pages deployment status before treating the live page as updated.

## Preview

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory docs
```

Open http://127.0.0.1:8766/. Review at 390 px in light/dark mode, 320 px and desktop. Tab through links and FAQ controls.

## Routine editing

- **Introduction and FAQ:** edit `docs/index.html`. Keep the introduction broad and factual; add specific outcomes, status or dates only when intentionally restoring those details. The page currently shows one team photo and four FAQ disclosures.
- **Contact:** the hero and joining FAQ use `https://www.instagram.com/enablewlu/`, verified from the organizer's screenshot October 9, 2026. Keep both links consistent. A monitored inbox and meeting schedule are not confirmed.
- **Photo and sharing:** see `MEDIA.md` for provenance and consent. Update caption, alt text, dimensions and `srcset` when replacing the team photo. The share image also uses that photo; update the HTML head if its filename or public URL changes.
- **Future details:** the existing hand photos, video and community logo remain in `docs/media/` but are not displayed. The earlier build details are preserved in local review notes. This simpler page does not claim chapter listing, university recognition, recipients or deliveries.

## Officer handover

Recommended, not established: put GitHub and Instagram under group-controlled ownership, give incoming officers individual access where supported, and keep recovery details in the group's private records. Before handover, document the current owner, collaborators, recovery contact, who checks messages and who can publish. Have the next officer make and preview one small edit before the outgoing officer leaves. Transfer access deliberately; do not put passwords, planning-vault notes or private recipient details in this repository.

Routine edits need only `docs/index.html`; visual rules are in `docs/styles.css`. `docs/site.js` is an inert note documenting visitor-initiated video playback and is not loaded. The unused community logo remains credited in `MEDIA.md`. Research, recommendations, review evidence and social drafts are gitignored local material.
