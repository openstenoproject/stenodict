---
layout: dictionary
title: Vim Captioning
version: 1
date: 2015-11-5
filename: vim_captioning
author: Mirabai
tags: commands shortcuts program-specific windows linux captioning
what: Useful realtime captioning commands for Vim
formats:
  - json
---

## Why

Vim can be a powerful text editor for realtime captioning. These commands help to streamline the process.

## How

- `STPHA*EUF`: Save silently
- `H-F/STPHA*EUF`: Save silently after question mark
- `SKHRAPL/STPHA*EUF`: Save silently after exclamation mark
- `SKWR-RBGS/STPHA*EUF`: Save silently after ellipses
- `SKWRAURBGS/STPHA*EUF`: Save silently after paragraph 
- `KH-FG`: Shift-tab (useful for rewinding in Amara)
- `KHR*F`: Paste
- `KHR*T`: Close tab in Chrome (useful for searching spellings)
- `KHR*BG`: Search in Chrome address bar
- `KHR-BG`: Copy
- `KR*T`: Double chevron for unidentified speakers
- `KW-RPB`: "Quarantine" stroke in text file. Customize this for your own path.
- `KWORD`: Copy word under cursor
- `PRO*F`: Generic "Professor" speaker stroke for academic captioning
- `PW-FP`: Backspace
- `R-R`: Return
- `SKHR*EBGS`: Cancel current selection highlighting
- `SKWRAURBGS`: Paragraph
- `SKWRO*EUP`: Join current paragraph with previous paragraph
- `SPA*EL`: Jump to most recent misspelled word
- `SPHR*EBGT`: Add most recent misspelled word to spelling dictionary
- `TP-PL/SPHR*EBGT`: Add most recent misspelled word to spelling dictionary after period 
- `SPHR*EUPBG`: Turn off cursor blinking
- `SPO*EL`: Turn off spellcheck
- `SPWAO*UT`: Bring up whole-file find/replace dialogue
- `SR-RS`: Jump to end of file in insert mode 
- `STPAO*EUL`: Save file as .txt. Customize this for your own path. 
- `STPH*EPBT`: Shift-Enter. Useful for breaking lines within captions in Amara.
- `STPH-BG`: Right by word (works in both insert and command modes)
- `STPH-RB`: Left by word (works in both insert and command modes)
- `TA*B`: Tab. Useful for play/pause in Amara and for making Plover definitions.
- `TABT`: Alt-Tab. Useful to switch between windows when looking up word spellings.
- `TKRORPLT`: Reformat file with large font size and slate colorscheme. Useful for big screen projected captioning.
- `TKHREPBD`: Delete from cursor to end of document. Only works in command mode.
- `TPEFBG`: Escape. Useful for making Plover definitions.
- `TW*EUT`: Reformat complete file to default textwidth, eliminating triple line breaks and multiple spaces.
- `TWO*EUT`: Reformat complete file to large font textwidth, eliminating triple line breaks and multiple spaces.

This dictionary also includes fingerspelling alphabets that force uppercase and lowercase, meaning "KPA" and such won't mess with your Vim commands

#### One-Stroke Google Plugin

I recommend the very useful [Vim-g one-stroke Google plugin](https://github.com/szw/vim-g)
