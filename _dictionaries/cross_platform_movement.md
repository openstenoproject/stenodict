---
layout: dictionary
title: Cross Platform Movement
version: 1
date: 2015-11-7
filename: cross_platform_movement
author: Ted Morin
tags: commands shortcuts windows linux mac
what: Movement and selection across Mac, Windows, and Linux
formats:
  - json
---

## Why

I learned Plover on Windows, and then found myself using OS X. Mac uses different hotkeys to achieve the same actions as Windows, and I had to work around that. This is how I solved the issue. The dictionary is slightly easier to use on Windows than Mac, due to chronological order.

## How

#### Movement

Like the Plover default dictionary, you activate movement keys by using `STPH-` and then select the movement key with the right hand, as below.

Use `-R`, `-P`, `-B`, and `-G` for **left, up, down, and right**.

In addition, page up and down are arrows made with the right hand: **Page Up** is `-RPG` (up arrow). **Page Down** is `-FBL` (down arrow).

**Home** is `-FPL` (all three fingers up), **End** is `-RBG` (all three fingers down.)

Finally, `-RB` is **Control(Left)**, `-BG` is **Control(Right)**. These jump words left and right on Windows and Linux. For Mac, add an asterisk, and `*RB` will make **Option(Left)**, and `*BG` will make **Option(Right)**.

#### Selection

To add Shift to any of the above (which will select text that you move over), use `SKWR-` instead of `STPH-`.

#### Utility

Included for convenient is a set of arrow keys with the Super key (Windows/Meta/Command depending on OS). On Windows, this will snap windows to the sides of screens, maximize, and minimize them. On Mac, you can jump to the beginning or end of lines or files. On Linux, the behavior varies. To use this, it's simply `KPH*` (**c**o**m**mand) and the four arrows.

#### Deletion

Finally, I have a delete-word stroke for when Plover runs out of buffer. Simply `#*` on Windows & Linux; I tend to use right index finger for the asterisk, and the middle right finger for the number bar. On Mac, I just use `*F` or `*6` if I accidentally hit the number bar.
