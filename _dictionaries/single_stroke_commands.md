---
layout: dictionary
title: Single Stroke Commands
version: 1
date: 2018-04-01
filename: single_stroke_commands
author: Kevin Knox
tags: commands shortcuts windows linux mac
what: A single-stroke brief for virtually all keyboard shortcuts
formats:
  - json
---
 
## Why
 
Gives Plover the ability to reproduce every modifier for every key by (admittedly bizarre) rules. The function keys are only represented from f1 to f5, but those can be hit with every modifier. It allows the user to access all the actions (ctrl-x, ctrl-alt-tab, shift-esc, alt-f4, ctrl-shift-end, etc.) available to a qwerty user.
 
## How
 
Everything that makes sense about this dictionary was copied from Ted Morin's [cross_platform_movement dictionary](/stenodict/dictionaries/cross_platform_movement.html). The rest I added to make all the functions I use reachable to me.
 
Loosely from the code that generates the dictionary, here are the critical snippets:

### The list of modifiers. Hold these with the right hand to choose modifiers to apply

- $nav = `-FRLG`
- $shift = `-FRBLG`
- $alt = `-FRLGTS`
- $shift_alt = `-FRBLGTS`
- $ctrl_nav = `-*FRLG`
- $ctrl_shift = `-*FRBLG`
- $ctrl_alt = `-*FRLGTS`
- $ctrl_shift_alt = `-*FRBLGTS`
- $super = `-TSDZ`
- $alt_super = `-PTSDZ`
- $shift_super = `-BTSDZ`
- $shift_alt_super = `-PBTSDZ`
 
### Hold these with the left hand to choose the key you want to hit and modify

- Any letter = Its steno alphabet equivalent
- Function key (1-5 only) = Its steno number equivalent
- `KPW-` = BackSpace
- `PWR-` = Delete
- `TWH-` = Down
- `KPR-` = Up
- `WR-` = Right
- `SK-` = Left
- `TPWH-` = End
- `KPWR-` = Home
- `WHR-` = Page_Down
- `PHR-` = Page_Up
- `SP-` = Space
- `TKP-` = Escape
- `TKW-` = Tab
- `SHR-` = Return
 
The special keys are mostly shape-based, rather than phonetic, per Ted's dictionary. Delete and backspace both center on the `PW` (`B`) shape, then add the lower left key to backspace or the lower right key to forward delete.

Up and down are arrow-shaped and point in their directions.

End and home are the arrow keys "filled in" with the W or P key.

Left and right are the pair of lower keys to the left or right.

Page up and page down are arrows pointed up or down and to the right.

Escape and tab are like page up and down, but pointed to the left.

Return is just the outermost keys.