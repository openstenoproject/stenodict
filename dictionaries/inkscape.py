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
			StrokeH("KR"): copy_object,
			StrokeH("SR"): paste_object,
			Stroke("TPR"): "{#Escape}",
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

	colors = {	# shape following my internal okular set-color script
			"T"    : color_none.name,
			"R"    : "red"	  ,
			"PW"   : "blue"   ,
			"KR"   : "cyan"   ,
			"PH"   : "magenta",
			"TKPWR": "orange" ,
			"PWHR" : "black"  ,
			"TKPW" : "green"  ,
			"W"    : "white"  ,
			"PR"   : "#cccccc",  # 20% gray
			}

	# hold with A to apply color on stroke (or with A# to fill)
	# the left * button on my keyboard is # so…
	styles: dict[Stroke_, str] = dict_merge(
			{
				Stroke(stroke): create_style_str(stroke=Color(color))
				for stroke, color in colors.items()},
			{
				StrokeH(stroke): create_style_str(fill_or_arrow=Color(color))
				for stroke, color in colors.items()},
			{
				Stroke("WR") : create_style_str(fill_or_arrow=Arrow()),
				Stroke("KWR"): create_style_str(fill_or_arrow=DoubleArrow()),
				Stroke("SHR"): create_style_str(stroke_style=StrokeStyle.solid),
				Stroke("STK"): create_style_str(stroke_style=StrokeStyle.dashed),
				Stroke("TK") : create_style_str(stroke_style=StrokeStyle.dotted),
				Stroke("S")  : create_style_str(thickness=Thickness.thin),
				Stroke("ST") : create_style_str(thickness=Thickness.normal),
				Stroke("STP"): create_style_str(thickness=Thickness.thick),
				Stroke("SK") : create_style_str(fill_opacity=0.3, stroke_opacity=0.3, opacity=0.3),
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

	style_string = ';'.join('{}: {}'.format(key, value)
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

def reload_saved_objects():
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

def lookup(strokes: tuple[str, ...])->Optional[str]:
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
				clipboard_copy(
						'<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
						'<svg xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape">'
						+ _marker_helper() +
						f'<inkscape:clipboard style="{style_string}" />'
						'</svg>', TARGET)
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
		if stroke in StrokeH("STKPWHRAO"):
			notify_send(f"invalid stroke {stroke}")
			return no_op
	return None

LONGEST_KEY = 1
