---
layout: dictionary
title: Di’s Vim Commands
version: 1
date: 2016-10-12
filename: vim_di
author: Di
tags: briefs commands mac neovim vim iterm program-specific programming shortcuts words
what: Vim and steno were made for each other
formats:
  - json
---

## Why

Stenography allows efficient text input and editing. Vim allows efficient text input and editing. This dictionary provides briefs for using the two together.

## How

Most strokes use `STPR` to indicate vim (`SR` => `V`).

- `"SREUPL"`: Phonetic brief for "vim".
- `"SR*EUPL"`: Restore brief for "victim" using additional star.
- Punctuation with suppressed spaces to run vim commands (see also: unspaced punctuation dictionary):
    - `"P-P"`: Unspaced period for vim's "last edit" command.
    - `"T*EULD"`: Unspaced tilde for capitalisation. That is, `~`. This brief follows format for tilde `TEULD` with additional star.
    - `"TPHRORB"` => `FLOSH`: Unspaced dollar sign for end of line command.
    - `HR*PB`: Unspaced `<` for left indent.
    - `TKPWR*PB`: Unspaced `>` for right indent.
    - `KW-L`: Unspaced `=`.
    - `OEU`: Unspaced `/` for searching.
- `STPR` and `*`, `-B`, `-G`, `-R` for vim style navigation keys `hjkl`:
    - `"STPR*"`: `h`
    - `"STPR-B"`: `k`
    - `"STPR-G"`: `l`
    - `"STPR-R"`: `j`
- Move lines up and down in any mode:
    - `.vimrc` mappings are:

            " Move lines up/down using alt j/k when iTerm is set to:
            " Left option (⌥) key acts as Normal
            " In mapping, press opt/alt+j/k to type these characters
            nnoremap ∆ :m .+1<CR>
            nnoremap ˚ :m .-2<CR>

            inoremap ∆ <Esc>:m .+1<CR>gi
            inoremap ˚ <Esc>:m .-2<CR>gi

            vnoremap ∆ :m '>+1<CR>gv=gv
            vnoremap ˚ :m '<-2<CR>gv=gv

    - Briefs are:
        - `"PHR-B"` => `MLB`: Move line up using vim style navigation `k`.
        - `"PHR-R"` => `MLR`: Move line down using vim style navigation `j`.
- `"SPWAO*UT"`: Exit insert mode and start substitution. That is, Escape and `:%s/`.
- `"SR*F"`: Exit insert mode and run command to write buffer (i.e. save the file). That is, Escape, `:w`, and Return. Brief format follows brief for Save command `"S*F"`.
- `"STPR*F"`: Exit insert mode and run command to write buffer (i.e. save the file). That is, Escape, `:w`, and Return. This alternative brief format follows brief for Save command `"S*F"` combined with brief format for most of these vim strokes using `STPR`.
- `"STPROEUFRL"`: Steno lookup shortcut that exits insert mode, yanks inside word to system clipboard (this might be Neovim only) using `"yiw` and runs my shortcut for steno lookup tool `⌃⌘⌥⇧s`. Brief format combines vim brief and regular steno lookup brief `STOEUFRL`. To use your own shortcut, replace this part of the translation `{#Control_L(Alt_L(Shift_L(Super_L(s))))}` with your shortcut command.
- `"STPREFBG"`: Exit insert mode and prepare command to write buffer (i.e. save the file) and quit. That is, Escape and `:x`. Brief format follows vim brief format `STPR` and brief for Escape `TPEFBK`.
- `"STPR-FPLT"`: Exit insert mode and write unspaced colon to enter command mode. That is, Escape and `:`.
- `"STPR-L"`: Runs `gt` to go to next tab. Follows brief format of tabs from tab navigation dictionary.
- `"STPR-F"`: Runs `gT` to go to previous tab. Follows brief format of tabs from tab navigation dictionary.

