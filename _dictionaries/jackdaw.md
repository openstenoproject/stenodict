---
layout: dictionary
title: Jackdaw orthographic chords
date: 2016-06-22
version: 1
filename: jackdaw
author: Lindsay Winkler
tags: words briefs
what: Implement proposed Jackdaw orthographic chords
formats:
  - json
---

## Why
This dictionary implements orthographic chords from the 
[Jackdaw proposal](https://sites.google.com/site/ploverdoc/jackdaw) for use with Plover.

This is a first pass at the dictionary, and is intended to enable hands on experimentation
with what's described in the proposal, to assist in further refining it.

Jackdaw intends to provide orthographic, rather than phonetic chords, and therefore
behaves somewhat differently to a regular steno theory.  Chords are divided into onset (with
the left hand), vowels (with the thumbs) and coda (with the right hand).  These three elements
are combined in a deterministic way to produce the output.

Because the two leftmost keys in Plover are both logically `S`, the leading `A` key in
the Jackdaw proposal can't be implemented with a standard Plover dictionary.  That means
none of the chords beginning with `A` are available.

The proposed fourth part of the chord - the inflection - is not implemented here.

Keys in Jackdaw are named and ordered differently to those on the standard steno keyboard
that Plover works with. 

This is a fairly inefficient way to implement Jackdaw: because the parts of the chord are
combined by concatenating left to right, there's no need to have a dictionary with every possible
key combination.  Jackdaw can be implemented directly in keyboard firmware, and fit in memory
on a keyboard, for example.  This dictionary, though, offers the possibility for existing Plover
users to explore the concept.
## How

Just add this dictionary to Plover's list, such that it takes precedence over
your core Plover dictionary (`dict.json` or `main.json`).
