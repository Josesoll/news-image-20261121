[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Josesoll/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Josesoll/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# news-image-20261121

A newspaper front page for **Saturday 21 November 2026**, drawn as one image.

Five stories carry the day, each happened or was first reported on
Saturday 21 November 2026 (verified against the source's own timestamp):

- **Lead — Riyadh & Ukraine:** Saudi defences intercepted three Houthi
  ballistic missiles fired at Riyadh early Saturday (Reuters, 21 Nov);
  Russia launched 148 drones and 3 ballistic missiles at Ukraine
  overnight, and AP reported on 21 Nov that the Kryvyi Rih toll stood at
  2 killed (a boy of 7 and a paramedic) and about 60 wounded.
- **COP31, Antalya:** Climate talks continued into Saturday in overtime
  with no deal; fossil-fuel language dropped from the draft (AP, 21 Nov).
- **Geneva:** UN talks on autonomous ("killer robot") weapons ended
  Saturday with only an agreement to keep talking for two more years,
  to 2028 — no binding rules (published 21 Nov).
- **Florida:** By Saturday morning the St. Johns River remained near
  record levels after up to 24 inches of rain on the Space Coast, with
  the flood storm moving north (Florida Today / AP, 21 Nov).
- **Europe:** Gen Z protests continued into Saturday — a transport
  strike in Italy and marches expected in France and Spain — over living
  costs, education and war spending (CNN, updated 21 Nov).

Stories from 19–20 November (the Myanmar genocide ruling, the Shenzhen
summit, Thursday's UK–EU deal, Friday's US market close) were
deliberately left out: mixing another day's news loses this contest.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies the shipped
`entry.png` (1024×1024 PNG, under 1 MiB) to `/output/entry.png`
(or `$MAKEFUN_OUTPUT_DIR/entry.png`). It runs offline and writes
byte-identical output on every run.

## Regenerate the image

```sh
python3 generate.py   # Pillow + Liberation fonts; deterministic
```

`generate.py` renders the front page deterministically (fixed layout,
fixed-seed star field) and writes `entry.png`.
