# Media list

Type: CURRENT-STATE. Audience: whoever maintains the site.

Originals live in the organizer's Box folder `e-NABLE Photos/Build Photos` (`Photo Sources.csv` lists origin and checksum). Everyone pictured agreed to publication (confirmed by the organizer, October 9, 2026). Dates come from photo metadata; dates and counts are not used as outcome claims on the page.

The October 10 working draft displays the team photo, five build photos and one silent video. Photo stems below each have `-800.jpg` and `-1600.jpg` versions unless otherwise noted. Only files in `docs/` are served publicly.

| File stem | Original | Date | Location | Used in |
| --- | --- | --- | --- | --- |
| `team-session` | IMG_2893 | Jun 30 | `docs/media/` | Hero; Open Graph share image |
| `two-hands` | 2026-09-12_Two_Hands_Comparison.jpeg | Sep 12 | `docs/media/` | Build gallery |
| `cad-and-parts` | IMG_2898 | Jun 30 | `docs/media/` | People set |
| `palm-channel` | IMG_0942 | Jul 7 | `docs/media/` | Build gallery |
| `forming-bath` | IMG_0737 | Jun 30 | `docs/media/` | Build gallery |
| `fingertips` | Jul 9 Photos export | Jul 9 | `docs/media/` | Build gallery |
| `fingers-close.mp4` + `fingers-close-poster.jpg` | IMG_4487.MOV (6.0 to 11.2 s, no audio) | Jul 8 | `docs/media/` | Build gallery, native video controls; poster shown before play |
| `hand-one`, `hand-two` | Crops of the same Sep 12 photo, so light and scale match | Sep 12 | `media_spare/` | Spare crops, not published |
| `first-hand` | IMG_0939 | Jul 7 | `media_spare/` | Spare, not published |
| `assembly` | IMG_4382 | Jun 30 | `docs/media/` | People set |
| `printer-watch` | IMG_4386 (sent by the organizer via Messages, Oct 10; not in the Box folder) | Jun 30 | `docs/media/` | People set |
| `pla-gauntlet` | IMG_0945 | Jul 7 | `media_spare/` | Spare, not published |
| `printer-bed` | IMG_4628 | Sep 12 | `media_spare/` | Not used: shows a failed print; excluded from this draft |

On October 10, both JPEG sizes of `cad-and-parts`, `forming-bath` and `fingertips` were moved from `media_spare/` into `docs/media/`. These images add a screen-and-parts view, a beaker-and-part view, and a clear close-up. `two-hands` and `palm-channel` were already in `docs/media/`. All candidates were inspected before selection. The individual hand crops repeated `two-hands`, so they stay spare. `assembly` moved in later the same day for the people set.

On October 10 the owner removed all visible captions, since the draft wording might be wrong; only `alt` text remains, describing what is visible. The owner also asked for a separate set of candid photos of members at work (`assembly`, `printer-watch`, `cad-and-parts`), shown above the sideways build gallery. People-set images are cropped to 3:4; gallery images keep their proportions at a fixed height. The video is silent, has a descriptive accessible label, and loads only after the visitor starts it (`preload="none"`, no autoplay).

## Replacing a photo

1. Export a JPEG about 1600 px on the long side and another about 800 px. Keep each under about 400 KB.
2. Put both sizes in `docs/media/`, using the existing naming pattern. Move unused pairs to local `media_spare/` when intentionally retiring them.
3. Update `alt`, intrinsic `width`/`height`, `srcset` and `sizes` in `docs/index.html`. Use actual pixel widths for `srcset` descriptors, not the long-side number in a portrait filename. Keep below-fold images lazy-loaded.
4. Update the table with the source, date, publication consent and "Used in" location. Update share metadata if changing the team image.

Or rerun `python3 tools/prepare_media.py "<Build Photos folder>"` from the project root after adding the file to its list. Check generated dimensions and output locations before using them.

## Community logo

`docs/media/e-nable-logo.png` is the unmodified black community logo downloaded October 9, 2026 from [Enabling the Future's official media asset](https://enablingthefuture.org/wp-content/uploads/2020/01/e-NABLElogoblack-e1578870415939.png), located through its public WordPress media API. It is retained in the asset folder but not displayed. It does not represent chapter listing or university recognition. This draft uses photos and type, with no diagrams, illustrations or decorative icons.
