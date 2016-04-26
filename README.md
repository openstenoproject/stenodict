# Stenodict

Stenodict aims to help shape how to use stenography in our modern world.
There is much more to text now than there ever was, between new
weird words, all the way to extended symbols such as emoji. We type cryptic
nonsense in the form of programming languages. We use function keys and movement
keys and modifiers and shortcuts. We have a whole set of problems
to deal with that the *writers of olde* never had to.

If stenography is ever really going to replace a keyboard for everyday use,
people need to use shortcuts, commands, and preferably they shouldn't have to
reinvent the wheel each time they want to do something.

This repository is a set of free, open source stenographic dictionaries to help
you with the task of evolving beyond a traditional keyboard.

## Adding a dictionary

**To submit a dictionary, you can do one of the following:**

1. Send me an email with your dictionary: morinted@gmail.com
2. Submit a GitHub issue with the needed information
3. Make a GitHub pull request on the gh-pages branch with your `dictname.md`

To submit a dictionary, you'll need:

- A steno dictionary in JSON or RTF/CRE format, or both.
- To create a description file, formatted like this one, but with your dictionary information filled in, instead. Note: "dictname" below would need to match the name of your actual dictionary, like `dictname.json` or `dictname.rtf`

```md
---
layout: dictionary
title: A Cool Title
version: 1
date: 2016-01-01
filename: dictname
author: My Name
tags: briefs captioning commands linux mac windows program-specific programming shortcuts symbols words
what: One-liner about my cool dictionary
formats:
  - json
  - rtf
---

## Why

This is a really cool dictionary. I'll describe it in about one paragraph. It's really great because when you use it you can write more words with the steno machine and it makes you cooler.

## How

Here you can extend on how to use the dictionary, offer tips and advice.

Feel free to spread out across multiple paragraphs...

- Use a bulleted list.
- Make your points.
- You can show raw steno: `STKPWHRAO*EUFRPBLGTSDZ`
- `STK`: "and"

And that's why you should use my dictionary!
```
