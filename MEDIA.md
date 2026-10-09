# Media list

Type: CURRENT-STATE. Audience: whoever maintains the site.

Originals live in the organizer's Box folder `e-NABLE Photos/Build Photos` (`Photo Sources.csv` lists origin and checksum). Everyone pictured agreed to publication (confirmed by the organizer, October 9, 2026). Dates come from photo metadata.

| File (in `docs/media/`) | Original | Date | Used in |
| --- | --- | --- | --- |
| `two-hands` | 2026-09-12_Two_Hands_Comparison.jpeg | Sep 12 | Retained, not displayed |
| `hand-one`, `hand-two` | Crops of the same Sep 12 photo, so light and scale match | Sep 12 | Spare crops, not published |
| `first-hand` | IMG_0939 | Jul 7 | Spare |
| `assembly` | IMG_4382 | Jun 30 | Spare |
| `palm-channel` | IMG_0942 | Jul 7 | Retained, not displayed |
| `forming-bath` | IMG_0737 | Jun 30 | Spare |
| `fingers-close.mp4` | IMG_4487.MOV (6.0 to 11.2 s, no audio); hand partly assembled, two fingers working | Jul 8 | Retained, not displayed |
| `printer-bed` | IMG_4628 | Sep 12 | Not used: shows a failed print |
| `team-session` | IMG_2893 | Jun 30 | Hero |
| `pla-gauntlet`, `fingertips`, `cad-and-parts` | IMG_0945, Jul 9 Photos export, IMG_2898 | Jul 7, Jul 9, Jun 30 | Spare |

Captions on the page were drafted from the photos and dates. The person who took each photo should confirm or rewrite its caption.

## Replacing a photo

1. Export a JPEG about 1600 px on the long side and another about 800 px. Keep each under about 400 KB.
2. Name them like the file you're replacing (`two-hands-1600.jpg`, `two-hands-800.jpg`) and drop them into `docs/media/`. The page layout crops to a fixed frame, so any orientation works.
3. Update the `alt` text and the caption in `docs/index.html` if the picture shows something different.
4. Add a row above, with the date and who agreed to publish.

Or rerun `python3 tools/prepare_media.py "<Build Photos folder>"` from the project root after adding the file to its list.

Files marked Spare or Not used live in the local, untracked `media_spare/` folder so they are not published. Move a pair back into `docs/media/` when the page uses it.

## Community logo

`docs/media/e-nable-logo.png` is the unmodified black community logo downloaded October 9, 2026 from [Enabling the Future's official media asset](https://enablingthefuture.org/wp-content/uploads/2020/01/e-NABLElogoblack-e1578870415939.png), located through its public WordPress media API. It is retained locally in the public asset folder but not displayed in the simplified page. It does not represent chapter listing or university recognition.
