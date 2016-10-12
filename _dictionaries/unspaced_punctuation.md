---
layout: dictionary
title: Unspaced punctuation
version: 1
date: 2016-10-12
filename: unspaced_punctuation
author: Di
tags: punctuation
what: Punctuation with all the spaces suppressed
formats:
  - json
---

## Why

This dictionary uses common briefs for punctuation, but with translations that suppress surrounding spaces (before and after the punctuation) for more precise input. This might be handy for programming, for example.

## How

Usual strokes for punctuation:

- `EPB/TKA*RB`: –
- `EPL/TKA*RB`: —
- `KH-FG`: \`
- `KR-RT`: ^
- `KA*RT`: ^
- `T*LD`: ~
- `T*EULD`: ~
- `AEPBGT`: <
- `AEPBG`: <
- `A*EPBGT`: >
- `A*EPBG`: >
- `HR*PB`: <
- `TKPWR*PB`: >
- `PWRABG`: <
- `PWRA*BG`: >
- `KWA*LS`: =
- `KW-L`: =
- `KW-LS`: ==
- `KW*LS`: ===
- `PAO*EUP`: |
- `R*UPB`: _
- `R*UPBD`: _
- `RUPBD`: _
- `H-PB`: -
- `PH*PBS`: -
- `TK-RB`: --
- `OEU`: /
- `SPWHRAERB`: \
- `P-P`: .
- `HR-PS`: ...
- `A*E`: '
- `AE`: '
- `KW-GS`: "
- `KR-GS`: "
- `PREPB`: (
- `PR*EPB`: )
- `PWR*BGT`: ]
- `PWR-BGT`: [
- `TPR-BGT`: {
- `TPR*BGT`: }
- `TK-PL`: $
- `STA*R`: *
- `SP-PBD`: &
- `HAERB`: #
- `PERS`: %
- `PHR*US`: +

There is an additional stroke for unspaced double quotation mark combining the opening and closing double quotation mark briefs:

- `KWR-GS`: "

You might then remove the usual strokes for opening and closing double quotation marks so you can still use them with spacing on demand. You might also replace them with smart or curly double quotation marks, for example:

```
"KW-GS": "{“^}",
"KR-GS": "{^”}",
```

You could then write `Test “test” test.` using `KPA* TEFT KW-GS TEFT KR-GS TEFT TP-PL`.

Similarly with single quotation marks (not included in this dictionary):

```
"TP-P": "{‘^}",
"TP-L": "{^’}",
```

