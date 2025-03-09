---
layout: dictionary
title: Inkscape Commands
version: 1
date: 2025-03-07
filename: inkscape
author: user202729
tags: commands linux inkscape
what: Convenient commands for Inkscape
formats:
   - py
---

## Why

Convenient shortcut for working with Inkscape.
Port of [Gilles Castel's shortcut manager](https://castel.dev/post/lecture-notes-2/) to Plover.

## Requirements

- Executables: `xclip`, `inkscape`, `xdotool`, `notify-send`, `rofi`
- Python packages: `getactivewindow-x` (optional), `tomlkit`, `plover_python_dictionary_lib`

## Installation

First install https://pypi.org/project/plover-python-dictionary/, then (restart Plover and)
add the `inkscape.py` file as a dictionary to Plover.

**Important**: If you're not running Plover with the patch in https://github.com/openstenoproject/plover/pull/1160,
comment out the following lines from the file:

```python
elif all(Stroke(s) in left_hand for s in strokes):
    # another consequence of not using proper macro
    # require https://github.com/openstenoproject/plover/pull/1160
    # just comment out if you don't have the patch (but tool will be slightly less functional)
    return "{plover:deleted}"
```

## Documentation

This script is a dictionary for Plover to use with Inkscape. It allows you to bind strokes to Inkscape actions,
such as selecting the pencil tool, creating a rectangle, or applying a style.

For convenience, all functionalities are accessible from the left hand.

It is likely that you would want to heavily customize the script to suit your needs.
As such, you need to know Python programming to use this script.
The default settings are as follows:

1. General-purpose strokes (specified in pseudo-steno, for example `X` is `KP`):

   - `P`: pencil tool
   - `X`: toggle snap
   - `B`: bezier tool
   - etc.

   See `adhoc_dict` in the script for more examples.

2. To apply a style, press a stroke containing `A`.
   For example:

   - `TA`: set stroke color to none (transparent)
   - `#TA`: set fill color to none
   - `KA`: set stroke color to black
   - `#KA`: set fill color to black
   - `BA`: set stroke color to blue
   - `KBA`: set stroke color to light blue
   - `TBA`: set stroke color to dark blue
   - `SA`: set stroke width to thin
   - `STPA`: set stroke width to thick
   - etc.

   See `colors` and `styles` in the script for more examples.

3. Because of the limited number of possible strokes on the left hand side,
   the script overrides several commonly-used strokes. For example `S` and `T` and `R` no longer type out `is` or `it`
   or `are` but instead are used for Inkscape actions.

   As such, use `SKWR` to toggle enable/disable the dictionary.
   (You can also use `plover-dict-commands` project for this purpose, but it is bundled for convenience)

4. There is a system to save and load objects.
   The information is kept in `saved_object.toml` file in Plover configuration directory.
   (Plover GUI → `File` → `Open config folder`)

   Select an object and press `#STPHO` to save an object, for example type in `circle [KRO]`
   and press `Ctrl-Enter` to add the object.

   To load (paste) the object, type either `KRO` (as typed in above), or `STPHO` then select the object
   by name.

   Objects cannot be easily deleted this way, you need to go to the TOML file and manually delete.

5. Independently from this dictionary, I have a patch to Plover that I use internally
   (see https://github.com/user202729/plover/blob/dev/plover/machine/keyboard.py#L176-L187 )
   to allow holding down/release modifier keys (Ctrl, Shift, Alt). This is crucial for Inkscape
   because many of the features are accessed through holding a modifier key while moving the mouse.

   So for example I can first hold down `#BR`, then if I want to hold `Ctrl`,
   I additionally hold `K`. When I want to release `Ctrl`, I release `K`.

   The way it works is follows: that part of the code converts individual events (`K` pressed, `K` released)
   into never-used strokes (e.g. when `#BR` is already held and `K` is *additionally* pressed,
   the machine sends `#KBR-FBLSD`, when `K` is then released, the machine sends `#KBR-RPGTZ`)

   Then, these strokes are then interpreted by another dictionary of mine to become
   `{#Control_L:down}` and `{#Control_L:up}` respectively.

   Finally, another patch to Plover https://github.com/user202729/plover/blob/dev/plover/key_combo.py#L168-L174
   translates them to key events.

   Obviously this only works if you are using the keyboard instead of some steno protocol like Gemini.

   Unfortunately, neither of https://github.com/openstenoproject/plover/pull/1161 nor
   https://github.com/openstenoproject/plover/pull/1161 gets merged.

   Side note: I also have a patch to Plover that only enables Plover on designated steno keyboards
   https://github.com/user202729/plover/blob/dev/plover/oslayer/linux/keyboardcontrol_x11.py#L229-L230 ,
   as such the disadvantages of keyboard input method is not present for me.

## Note

1. It's not difficult to avoid using `getactivewindow` (in fact it's somewhat flaky),
   just modify the source code below. See https://pypi.org/project/getactivewindow-x/0.3.0/
   for a list of replacements.

2. I have left `*` map to `#` because Starboard. Change `StrokeH` function if you use something else.

3. It may be possible to eliminate `xdotool` if there's some way to access the `Engine` object from Plover,
   then the `KeyboardEmulation` object can be accessed that way.
   One way to do that is to use https://github.com/user202729/plover-startup-py to pass `engine`
   (provided as a global variable to the script) somewhere then the Python dictionary can access it
   (very hacky).
