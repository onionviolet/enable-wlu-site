# e-NABLE at W&L website

Type: CURRENT-STATE. Audience: group organizers and website maintainers.

The site is plain HTML, CSS and a small script in `docs/`, ready for free GitHub Pages hosting (publish from the `docs` folder). No build step, accounts, trackers or backend. Version 3 (one short page, about 300 words) was built October 9, 2026, following `research/org_audit/00_SYNTHESIS.md`. Earlier drafts are in `archive/v1/` and `archive/v2/`. Not yet published.

## Preview

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory docs
```

Then open http://127.0.0.1:8766/.

## Everyday edits (all in `docs/index.html`)

- **Join box:** the `<!-- EDIT -->` comments for the first session and the group email. Update "Where things stand" and both "Updated" dates when something changes.
- **Projects:** one card per build, in the style of Duke's team list. Copy a card to add a project; the dashed "Your project" card stays last. Fill hand two's `<!-- EDIT -->` details when known.
- **Photos:** see `MEDIA.md`.
- **Share preview image:** after deploying, put the full `https://` address in the `og:image` tag.

## Facts the site relies on

Built from the organizer's confirmed facts: the first hand was printed in SLS nylon, powder blocked the tendon channels and pin holes, a new channel was cut through the palm, the first gauntlet snapped during forming and a white PLA replacement formed cleanly, and a second (navy) hand, printed in PLA on a Prusa, was finished by September 12, 2026. Campus recognition, an adviser, officers, a meeting schedule and chapter affiliation are not confirmed, so the page only says they are in progress or coming. No recipients, deliveries, sponsors or donations are claimed.

## Handover

Keep the repository under an account the group controls (or transfer it to a group GitHub organization) and add each new officer as a collaborator. The planning vault and private notes never go in this repository.
