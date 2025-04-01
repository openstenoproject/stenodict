#!/bin/python
"""
Heavily inspired from https://github.com/gillescastel/inkscape-shortcut-manager
"""
from __future__ import annotations
from typing import Optional
import typing

Stroke_ = typing.Any  # instance of Stroke, define like this to satisfy mypy
def settings()->tuple[dict[Stroke_, str], dict[Stroke_, str], Stroke_, Stroke_, Stroke_]:

	adhoc_dict: dict[Stroke_, str] = {
			Stroke("P"  ): "{#p}",		   # pencil
			Stroke("KP" ): "{^}%{^}",	   # snap (x instead of %)
			Stroke("PW" ): "{#b}",		   # bezier
			Stroke("S"  ): "{#s}",		   # select
			StrokeH("R" ): "{#Shift(s)}",  # toggle between rotate and resize mode (in select mode)
			Stroke("TPH"): "{#n}",		   # node
			Stroke("R"  ): "{#r}",		   # rectangle
			Stroke("KR" ): "{#e}",		   # circle (*ellipse)
			Stroke("TK" ): "{#Control(d)}",# duplicate
			Stroke("T"  ): "{#Control(t)}",# my internal binding for TeXtext (it's slow to spawn though)
			Stroke("SKW"): "{#Control(z)}",# undo
			Stroke("STK"): "{#Control(y)}",# redo
			Stroke("SH"): "{#F12}", # show/hide dialogues
			StrokeH("KR"): copy_object,
			StrokeH("SR"): paste_object,
			Stroke("TPR"): "{#Escape}",
			StrokeH("K"): "{#Control(k)}",  # merge paths
			Stroke("KPW"): "{#BackSpace}", # shape following single-stroke-modifier
			Stroke("PHR"): "{#Page_Up}",
			Stroke("WHR"): "{#Page_Down}",
			StrokeH("PHR"): "{#Home}",
			StrokeH("WHR"): "{#End}",
			Stroke("PH" ): "{^}+{^}",      # zoom in
			Stroke("WR" ): "{^}-{^}",      # zoom out
			StrokeH("S" ): "{#Control(s)}",
			Stroke("WH" ): "{#Control(Slash)}",  # division
			Stroke("PWR"): "{#Delete}",
			Stroke("TKPW"): "{#Control(G)}",  # group
			StrokeH("TKPW"): "{#Control(Shift(G))}",  # ungroup
			Stroke("TKR"): "{#Control(Shift(R))}",  # resize page to selection/drawing
			}

	# ↓ used to use this but is too restrictive
	#colors = {	# shape following my internal okular set-color script
	#		"T"    : color_none.name,
	#		"R"    : "red"	  ,
	#		"PW"   : "blue"   ,
	#		"KR"   : "cyan"   ,
	#		"PH"   : "magenta",
	#		"TKPWR": "orange" ,
	#		"PWHR" : "black"  ,
	#		"TKPW" : "green"  ,
	#		"W"    : "white"  ,
	#		"PR"   : "#cccccc",  # 20% gray
	#		}

	color_bases = {
			"R"   :"red",    # Red
			#"PWR" :"orange",# doesn't work on my side because sticky keys
			"WR"  :"yellow", # Yellow (truncated)
			"HR"  :"lime",   # Lime
			"H"   :"green",
			"PWH" :"cyan",   # (mix of blue and green)
			"PW"  :"blue",   # BLue
			"PWHR":"sky",
			"PH"  :"fuchsia",# Magenta?
			"PR"  :"gray",   # gRay  (?)
			"WHR" :"teal",
			"W"   :"violet",
			"PHR" :"purple", # PurpLe
			"P"   :"pink",
			"WH"  :"rose",
			}

	colors = dict_merge(
			{
				"T"    : color_none.name,
				"TK"   : "white",
				"K"    : "black",
				},
			{Stroke(stroke_base) | "K": tailwind_colors[color_base][2] for stroke_base, color_base in color_bases.items()},
			{stroke_base              : tailwind_colors[color_base][5] for stroke_base, color_base in color_bases.items()},
			{Stroke(stroke_base) | "T": tailwind_colors[color_base][7] for stroke_base, color_base in color_bases.items()},
			)

	# hold with A to apply color on stroke (or with A# to fill)
	# the left * button on my keyboard is # so…
	styles: dict[Stroke_, str] = dict_merge(
			{
				Stroke(str(stroke)): create_style_str(stroke=Color(color))
				for stroke, color in colors.items()},
			{
				StrokeH(str(stroke)): create_style_str(fill_or_arrow=Color(color))
				for stroke, color in colors.items()},
			{
				# non-color style:
				# S: always pressed
				# thickness:
				#     T P -
				#   S - - -
				# transparency:
				#     - - -
				#   S K W -
				# arrow:
				#     T P -
				#   S K W -
				# (to cancel arrow press #TA = no fill)
				# line style (solid/dashed/dotted):
				#     - - H
				#   S - - R
				Stroke("STK") : create_style_str(fill_or_arrow=Arrow()),
				Stroke("STKPW"): create_style_str(fill_or_arrow=DoubleArrow()),
				Stroke("SHR"): create_style_str(stroke_style=StrokeStyle.solid),
				Stroke("SR"): create_style_str(stroke_style=StrokeStyle.dashed),
				Stroke("SH") : create_style_str(stroke_style=StrokeStyle.dotted),
				Stroke("S")  : create_style_str(thickness=Thickness.thin),
				Stroke("ST") : create_style_str(thickness=Thickness.normal),
				Stroke("STP"): create_style_str(thickness=Thickness.thick),
				Stroke("SK") : create_style_str(fill_opacity=0.3, stroke_opacity=0.3, opacity=0.3),
				Stroke("SW") : create_style_str(fill_opacity=0.6, stroke_opacity=0.6, opacity=0.6),
				Stroke("SKW"): create_style_str(fill_opacity=1, stroke_opacity=1, opacity=1),
				})

	toggle_enabled_stroke = Stroke("SKWR")
	
	object_load_stroke = Stroke("STPHO")
	object_save_stroke = StrokeH("STPHO")

	return adhoc_dict, styles, toggle_enabled_stroke, object_load_stroke, object_save_stroke

from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from threading import Thread
from typing import TypeVar
import re
import subprocess
import sys
import time
import tomlkit

try:
	from typing import TypedDict
except ImportError:
	from typing_extensions import TypedDict

T = TypeVar("T")
U = TypeVar("U")

def dict_merge(*dicts: dict[T, U])->dict[T, U]:
	merged: dict[T, U] = {}
	for d in dicts:
		duplicate_keys = set(merged.keys()) & set(d.keys())
		if duplicate_keys:
			raise ValueError(f"duplicate keys e.g. {duplicate_keys.pop()}")
		merged.update(d)
	return merged

notification_id=10000  # just some random number… (it accepts nonexistent id)
def notify_send(message: str)->None:
	subprocess.run(["notify-send", "-t", "2000", "-r", str(notification_id), "--", message])

def inkscape_window_focused()->bool:
	try:
		from getactivewindow import active_window_id, window_class
	except ImportError:
		notify_send(f"getactivewindow not installed, dictionary will always be enabled. Use {toggle_enabled_stroke} to disable")
		def _inkscape_window_focused()->bool:
			return True
		global inkscape_window_focused
		inkscape_window_focused=_inkscape_window_focused
		return True
	return "org.inkscape.Inkscape" in window_class(active_window_id())

copy_object = "{#Control(c)}"
paste_object = "{#Control(v)}"
paste_style = "{#Shift(Control(v))}"
no_op = "{#}"

# level: 50 100 200 300 400 500 600 700 800 900 950
# index: 0  1   2   3   4   5   6   7   8   9   10
tailwind_colors = {  # https://gist.github.com/user202729/f51f92bb5135eaafccd2ac2533b18caf
"red":     "#fef2f2 #ffe2e2 #ffc9c9 #ffa2a2 #ff6467 #fb2c36 #e7000b #c10007 #9f0712 #82181a #460809".split(), 
"orange":  "#fff7ed #ffedd4 #ffd6a7 #ffb86a #ff8904 #ff6900 #f54900 #ca3500 #9f2d00 #7e2a0c #441306".split(), 
"amber":   "#fffbeb #fef3c6 #fee685 #ffd230 #ffb900 #fe9a00 #e17100 #bb4d00 #973c00 #7b3306 #461901".split(), 
"yellow":  "#fefce8 #fef9c2 #fff085 #ffdf20 #fdc700 #f0b100 #d08700 #a65f00 #894b00 #733e0a #432004".split(), 
"lime":    "#f7fee7 #ecfcca #d8f999 #bbf451 #9ae600 #7ccf00 #5ea500 #497d00 #3c6300 #35530e #192e03".split(), 
"green":   "#f0fdf4 #dcfce7 #b9f8cf #7bf1a8 #05df72 #00c950 #00a63e #008236 #016630 #0d542b #032e15".split(), 
"emerald": "#ecfdf5 #d0fae5 #a4f4cf #5ee9b5 #00d492 #00bc7d #009966 #007a55 #006045 #004f3b #002c22".split(), 
"teal":    "#f0fdfa #cbfbf1 #96f7e4 #46ecd5 #00d5be #00bba7 #009689 #00786f #005f5a #0b4f4a #022f2e".split(), 
"cyan":    "#ecfeff #cefafe #a2f4fd #53eafd #00d3f2 #00b8db #0092b8 #007595 #005f78 #104e64 #053345".split(), 
"sky":     "#f0f9ff #dff2fe #b8e6fe #74d4ff #00bcff #00a6f4 #0084d1 #0069a8 #00598a #024a70 #052f4a".split(), 
"blue":    "#eff6ff #dbeafe #bedbff #8ec5ff #51a2ff #2b7fff #155dfc #1447e6 #193cb8 #1c398e #162456".split(), 
"indigo":  "#eef2ff #e0e7ff #c6d2ff #a3b3ff #7c86ff #615fff #4f39f6 #432dd7 #372aac #312c85 #1e1a4d".split(), 
"violet":  "#f5f3ff #ede9fe #ddd6ff #c4b4ff #a684ff #8e51ff #7f22fe #7008e7 #5d0ec0 #4d179a #2f0d68".split(), 
"purple":  "#faf5ff #f3e8ff #e9d4ff #dab2ff #c27aff #ad46ff #9810fa #8200db #6e11b0 #59168b #3c0366".split(), 
"fuchsia": "#fdf4ff #fae8ff #f6cfff #f4a8ff #ed6aff #e12afb #c800de #a800b7 #8a0194 #721378 #4b004f".split(), 
"pink":    "#fdf2f8 #fce7f3 #fccee8 #fda5d5 #fb64b6 #f6339a #e60076 #c6005c #a3004c #861043 #510424".split(), 
"rose":    "#fff1f2 #ffe4e6 #ffccd3 #ffa1ad #ff637e #ff2056 #ec003f #c70036 #a50036 #8b0836 #4d0218".split(), 
"slate":   "#f8fafc #f1f5f9 #e2e8f0 #cad5e2 #90a1b9 #62748e #45556c #314158 #1d293d #0f172b #020618".split(), 
"gray":    "#f9fafb #f3f4f6 #e5e7eb #d1d5dc #99a1af #6a7282 #4a5565 #364153 #1e2939 #101828 #030712".split(), 
"zinc":    "#fafafa #f4f4f5 #e4e4e7 #d4d4d8 #9f9fa9 #71717b #52525c #3f3f46 #27272a #18181b #09090b".split(), 
"neutral": "#fafafa #f5f5f5 #e5e5e5 #d4d4d4 #a1a1a1 #737373 #525252 #404040 #262626 #171717 #0a0a0a".split(), 
"stone":   "#fafaf9 #f5f5f4 #e7e5e4 #d6d3d1 #a6a09b #79716b #57534d #44403b #292524 #1c1917 #0c0a09".split(),
}

from plover.system import english_stenotype as e  # type: ignore
from plover_python_dictionary_lib import get_context_from_system

context=get_context_from_system(e)
Stroke=context.stroke_type
def StrokeH(s: str)->str:
	#return Stroke(s)|Stroke("*")
	return Stroke("#"+s)


def clipboard_copy(string: str, target: Optional[str]=None)->None:
	extra_args = []
	if target != None:
		extra_args += ['-target', target]

	subprocess.run(
			['xclip', '-selection', 'c'] + extra_args,
			universal_newlines=True,
			input=string
			)

def clipboard_get(target: Optional[str]=None)->str:
    extra_args = []
    if target != None:
        extra_args += ['-target', target]

    result = subprocess.run(
        ['xclip', '-selection', 'c', '-o'] + extra_args,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    stdout = result.stdout.strip()
    return stdout

TARGET = 'image/x-inkscape-svg'

"""
I use an ad hoc style dict, apply one style at once,
instead of gillescastel's method of "one stroke to apply all aspects of the style".
That said, more styles can also be defined in `settings()` above.

  T P H
S K W R #

three axes: (fill/arrow), stroke, thickness
left half for fill, right half for stroke
if omitted: no change

fill/arrow axis:
	unchanged
	none
	white
	gray
	black
	one arrow head
	two arrow head

stroke axis:
	unchanged
	none
	normal
	thin
	thick

stroke style axis:
	unchanged
	none
	solid/continuous
	dashed
	dotted
"""



@dataclass
class Color:
	name: str  # could be "none"
color_none = Color("none")

class Arrow: pass
class DoubleArrow: pass


# there is no "none" option below because it is tied to inkscape svg internal
# to explicitly "set stroke/thickness to none", set stroke color to color_none
class StrokeStyle(Enum):
	solid = auto()
	dashed = auto()
	dotted = auto()

class Thickness(Enum):
	# reminds me of tailwind
	thin = auto()
	normal = auto()
	thick = auto()

def _style_constants()->tuple[float, float, float, float]:
	# cf. inkscape-shortcut-manager
	pt = 1.327 # pixels
	w = 0.4 * pt
	thick_width = 0.8 * pt
	very_thick_width = 1.2 * pt
	return pt, w, thick_width, very_thick_width

# None: unchanged
def create_style_str(
		*,
		fill_or_arrow: Color|Arrow|DoubleArrow|None=None,
		fill_opacity: float|None=None,
		stroke: Color|None=None,
		stroke_opacity: float|None=None,
		stroke_style: StrokeStyle|None=None,
		thickness: Thickness|None=None,
		opacity: float|None=None,  # for image
		)->str:
	"""
	create a style string to be copied into inkscape
	the parameters are tied to inkscape svg internal
	so e.g. if you paste style of `create_style_str(stroke_style=StrokeStyle.dashed)`
	onto a shape with `stroke=color_none` you will not see any change
	"""
	style: dict[str, str] = {}
	pt, w, thick_width, very_thick_width = _style_constants()

	if isinstance(fill_or_arrow, Color):
		style['fill'] = fill_or_arrow.name
		style['marker-start'] = 'none'
		style['marker-end'] = 'none'
	elif isinstance(fill_or_arrow, Arrow):
		style['fill'] = 'none'
		style['marker-start'] = 'none'
		style['marker-end'] = f'url(#marker-arrow-{w})'
	elif isinstance(fill_or_arrow, DoubleArrow):
		style['fill'] = 'none'
		style['marker-start'] = f'url(#marker-arrow-{w})'
		style['marker-end'] = f'url(#marker-arrow-{w})'
	else:
		assert fill_or_arrow is None

	if isinstance(fill_opacity, (int, float)):
		style['fill-opacity'] = str(fill_opacity)
	else:
		assert fill_opacity is None

	if isinstance(stroke, Color):
		style['stroke'] = stroke.name
	else:
		assert stroke is None

	if isinstance(stroke_opacity, (int, float)):
		style['stroke-opacity'] = str(stroke_opacity)
	else:
		assert stroke_opacity is None

	if isinstance(stroke_style, StrokeStyle):
		if stroke_style == StrokeStyle.solid:
			style['stroke-dasharray'] = 'none'
		elif stroke_style == StrokeStyle.dashed:
			style['stroke-dasharray'] = f'{w},{2*pt}'
		elif stroke_style == StrokeStyle.dotted:
			style['stroke-dasharray'] = f'{3*pt},{3*pt}'
		else:
			raise ValueError(f"unknown stroke_style {stroke_style}")
	else:
		assert stroke_style is None

	if isinstance(thickness, Thickness):
		if thickness == Thickness.thin:
			style['stroke-width'] = str(w)
		elif thickness == Thickness.normal:
			style['stroke-width'] = str(thick_width)
		elif thickness == Thickness.thick:
			style['stroke-width'] = str(very_thick_width)
		else:
			raise ValueError(f"unknown thickness {thickness}")
	else:
		assert thickness is None

	if isinstance(opacity, (int, float)):
		style['opacity'] = str(opacity)
	else:
		assert opacity is None

	style_string = ';'.join('{}:{}'.format(key, value)
							for key, value in sorted(style.items(), key=lambda x: x[0])
							)
	return style_string


def _marker_helper()->str:
	# cf. inkscape-shortcut-manager
	pt, w, thick_width, very_thick_width = _style_constants()
	return f'''
		<defs id="marker-defs">
		<marker
		id="marker-arrow-{w}"
		orient="auto-start-reverse"
		refY="0" refX="0"
		markerHeight="1.690" markerWidth="0.911">
		  <g transform="scale({(2.40 * w + 3.87)/(4.5*w)})">
			<path
			   d="M -1.55415,2.0722 C -1.42464,1.29512 0,0.1295 0.38852,0 0,-0.1295 -1.42464,-1.29512 -1.55415,-2.0722"
			   style="fill:none;stroke:context-stroke;stroke-width:{0.6};stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;stroke-dasharray:none;stroke-opacity:1"
			   inkscape:connector-curvature="0" />
		   </g>
		</marker>
		</defs>
		'''

# to investigate the paste format can run
#	  xclip -o -t image/x-inkscape-svg -selection clipboard
# after copying something from inkscape

adhoc_dict, styles, toggle_enabled_stroke, object_load_stroke, object_save_stroke = settings()
assert toggle_enabled_stroke not in adhoc_dict

def is_style_stroke(s: Stroke_)->bool:
	"""
	press a style stroke will apply a style
	"""
	return s in StrokeH("STKPWHRA") and "A" in s

def is_object_stroke(s: Stroke_)->bool:
	"""
	check whether s is an object stroke.

	press an object stroke will paste an object
	(we reserve #O for saving an object)
	"""
	return s in StrokeH("STKPWHRO") and "O" in s

assert is_object_stroke(object_load_stroke)
assert is_object_stroke(object_save_stroke)


@dataclass
class SavedObject:
	# actually snippet, can also be repurposed as style by using {paste_style} instead of {paste_object}
	# to be implemented later
	name: str
	stroke: str|None
	content: str

from plover.oslayer.config import CONFIG_DIR  # type: ignore
saved_object_file_path: Path = Path(CONFIG_DIR) / "saved_object.toml"

objects: list[SavedObject]

saved_object_file_last_modification_time: Optional[float]=None

def get_saved_object_file_last_modification_time()->Optional[float]:
	try:
		return saved_object_file_path.stat().st_mtime
	except FileNotFoundError:
		return None

def reload_saved_objects()->None:
	global objects
	try:
		d: typing.Any = tomlkit.loads(saved_object_file_path.read_text())
		objects = [
				SavedObject(
					name=str(o["name"]),
					stroke=str(o["stroke"]) if "stroke" in o else None,
					content=str(o["content"]))
				for o in d.get("objects", [])]
	except FileNotFoundError:
		objects = []
	except Exception as e:
		notify_send(f"file {saved_object_file_path} is corrupted, consider deleting it yourself. Exception detail: {e}")
		objects = []

def maybe_reload_saved_objects()->None:
	global saved_object_file_last_modification_time
	last_modification_time = get_saved_object_file_last_modification_time()
	if last_modification_time != saved_object_file_last_modification_time:
		saved_object_file_last_modification_time = last_modification_time
		reload_saved_objects()

maybe_reload_saved_objects()

rofi_running: bool = False

def rofi(prompt: str, options: list[str], rofi_args: list[str]=[], fuzzy: bool=True)->tuple[int, str]:
	# cf. inkscape-shortcut-manager
	global rofi_running
	assert not rofi_running, "rofi is already running"
	rofi_running = True
	try:
		assert not any("\n" in option for option in options), "newline is not allowed in options"
		optionstr = '\n'.join(options)
		args = ['rofi', '-sort', '-no-levenshtein-sort']
		if fuzzy:
			args += ['-matching', 'fuzzy']
		args += ['-dmenu', '-p', prompt, '-format', 's', '-i']
		args += rofi_args
		args = [str(arg) for arg in args]
		result = subprocess.run(args, input=optionstr, stdout=subprocess.PIPE, universal_newlines=True)
		return result.returncode, result.stdout.removesuffix('\n')
	finally:
		rofi_running = False

def select_object(prompt: str)->tuple[Optional[str], Optional[Stroke_]]:
	"""
	prompt user with rofi and return (name, stroke)
	"""
	maybe_reload_saved_objects()
	returncode, stdout = rofi(prompt, [
		f"{o.name} [{o.stroke}]" if o.stroke is not None else o.name
		for o in objects])
	if returncode != 0:  # probably canceled
		return None, None
	match = re.fullmatch(r"(.*)\[(.*)\]", stdout.strip())
	if match:
		name, stroke = match.groups()
		try:
			return name.strip(), Stroke(stroke)
		except ValueError as e:
			notify_send(str(e))
			return None, None
	else:
		return stdout.strip(), None

def do_load_object()->None:
	"""
	open a dialog to prompt the user which object to load
	should be spawned in a separate thread.
	"""
	name, stroke = select_object("select object to load")
	if name is None: return
	try:
		o=next(o for o in objects if o.name==name)
	except StopIteration:
		notify_send(f"no object with name {name!r}")
		return
	clipboard_copy(o.content, TARGET)
	time.sleep(0.2)
	subprocess.run(["xdotool", "key", "Control_L+v"])

def do_save_object()->None:
	"""
	open a dialog to prompt the user where to save the object
	should be spawned in a separate thread.
	"""
	global objects
	time.sleep(0.2)  # wait until the key is processed and the object is copied
	content = clipboard_get(TARGET)
	if "svg" not in content:
		notify_send("no svg content copied")
		return
	name, stroke = select_object("save object as (format: 'name' or 'name [stroke]')")
	if name is None:
		return
	if stroke is not None and not is_object_stroke(Stroke(stroke)):
		notify_send(f"stroke {stroke} is not a valid stroke for object")
		return
	if any(o.name==name for o in objects):
		returncode, stdout = rofi(
				f"overwrite {name!r}? (note Ctrl-Enter avoids selecting partial match)",
				["y", "n"])
		if not (returncode == 0 and stdout == "y"):
			return
	objects = [o for o in objects if o.name!=name]
	objects.append(SavedObject(name=name, stroke=stroke, content=content))
	saved_object_file_path.write_text(tomlkit.dumps({"objects": [
		dict(
			name=o.name,
			**({"stroke": str(o.stroke)} if o.stroke is not None else {}),
			content=tomlkit.string(o.content, multiline=True),
			) for o in objects]}))
	notify_send(f"object {name!r} saved"
			 + (f" with stroke {stroke}" if stroke else ""))

for stroke in adhoc_dict.keys():
	assert not is_style_stroke(stroke), f"ad hoc stroke {stroke} can be misrecognized as style"
	assert not is_object_stroke(stroke), f"ad hoc stroke {stroke} can be misrecognized as object"
enabled = True

def copy_style(style_string: str)->None:
	# style_string should be output of create_style_str()
	clipboard_copy(
			'<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
			'<svg xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">'
			+ _marker_helper() +
			f'<inkscape:clipboard style="{style_string}" />'
			'</svg>', TARGET)

left_hand = StrokeH("STKPWHRAO")

def lookup(strokes: tuple[str, ...])->Optional[str]:
	# NOTE it is very wrong to make `lookup` not a pure function
	# should use command plugin or https://github.com/user202729/plover-python-dictionary-cmd instead
	# (probably the former, more flexible)
	# (in practice it works anyway)
	if not inkscape_window_focused():
		return None
	if rofi_running:
		return None
	global enabled
	if len(strokes)==1:
		stroke = Stroke(strokes[0])
		if stroke == toggle_enabled_stroke:
			enabled = not enabled
			if enabled:
				notify_send("inkscape dict enabled")
			else:
				notify_send("inkscape dict disabled")
			return no_op
		if not enabled:
			# `toggle_enabled_stroke` must be checked before this
			return None
		if stroke in StrokeH("TKPWRAO") and StrokeH("PWR") in stroke:
			# overlap with a certain other dictionary I use, hide the warning
			return None
		if stroke in adhoc_dict:
			return adhoc_dict[stroke]
		if is_style_stroke(stroke):
			style_string = styles.get(stroke-Stroke("A"), None)
			if style_string is not None:
				copy_style(style_string)
				return paste_style
		if is_object_stroke(stroke):
			if stroke==object_load_stroke:
				Thread(target=do_load_object).start()
				return no_op
			if stroke==object_save_stroke:
				Thread(target=do_save_object).start()
				return copy_object
			maybe_reload_saved_objects()
			try:
				o = next(o for o in objects if o.stroke is not None and Stroke(o.stroke)==stroke)
			except StopIteration:
				notify_send(f"no object with stroke {stroke}")
				return no_op
			clipboard_copy(o.content, TARGET)
			return paste_object
		if stroke in left_hand:
			notify_send(f"invalid stroke {stroke}")
			return no_op
	elif all(Stroke(s) in left_hand for s in strokes):
		# another consequence of not using proper macro
		# require https://github.com/openstenoproject/plover/pull/1160
		# just comment out if you don't have the patch (but tool will be slightly less functional)
		return "{plover:deleted}"
	return None

LONGEST_KEY = 3
