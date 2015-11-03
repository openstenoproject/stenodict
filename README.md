# Stenodict

-------

# WIP

Stenodict isn't quite ready to publish. You can star or follow this repository. The site should be up sometime before mid-November

-------

Stenodict aims to help shape how to use stenography in our modern world.
There is much more to text now than there ever was, between new
weird words, all the way to extended symbols such as emoji. We type cryptic
nonsense in the form of programming languages. We use function keys and movement
keys and modifiers and shortcuts. We have a whole set of problems
to deal with that the writers of olde never had to deal with.

If stenography is ever really going to replace a keyboard for everyday use,
people need to use shortcuts, commands, and preferably they shouldn't have to
reinvent the wheel each time they want to do something.

This repository is a set of free, open source stenographic dictionaries to help
you with the task of evolving beyond a traditional keyboard.

## Adding a dictionary

To add a dictionary, you only need to add the dictionary file and edit the
dictionary list with information about your dictionary.

### What makes a dictionary

The required bits that make up a dictionary are:

- A dictionary file in either JSON or RTF/CE. JSON is preferable, as that's
what most Plover users are familiar with.
- An entry in the dictionary list with information about your dictionary:
	+ Name: title of the dictionary
	+ Filename: the filename of the dictionary that you added to the dictionary folder
	+ Description:
		- What: short summary of what the dictionary is. Limit to one sentence where possible.
		- Why: longer explanation of why you think people might use this dictionary and what its contents may be. Limit to one paragraph where possible.
		- How: explain the theory behind your dictionary, you can use as much detail as you think is necessary. You can use multiple paragraphs: this is where the user is learning how to use your dictionary.
	+ Tags: the categories that your dictionary fits into. There are a few tags that are pre-defined, you are welcome to define new ones if you feel it is necessary. You can see dictionaries.json for a full list of tags, which, for example, are along the lines of briefs, words, symbols, commands, and shortcuts.

There are examples with the other dictionaries in the repository. Because dictionaries
are manually approved, you can assume that any dictionaries on the site are in a format
that you can copy for your own submission.

### Option 1. Submit a Pull Request

This is the preffered method, if you are familiar with GitHub. Just fork, on the `gh-pages`
branch add your dictionary to `dictionaries.json` and place your dictionary in the
`dictionaries` folder.

The JSON format may look a little weird to you, it's just an alternative style called diffy that aims to make maintaining JSON a little bit easier for programmers. Please maintain this style when submitting a PR. If you don't want to style it manually, you can use the npm tool `format-json` which defaults to diffy format.

### Option 2. Submit an Issue

If you are not comfortable making a GitHub Pull Request,
you are welcome to just submit an issue with the required information
for a dictionary and we can make the code changes.

### Option 3. Email

If you for some reason
cannot create a GitHub account and still want to submit a dictionary, you
can always email [Ted](https://github.com/morinted) using the email on his GitHub profile.

## Development

The scripts for the website assume that you have both the `master` and the `gh-pages` branches pulled and available, side-by-side in a parent folder. I.e., you have `stenodict/master` and `stenodict/gh-pages`. To achieve this, you can run these commands wherever you want to store Stenodict for development:

```
mkdir stenodict && cd stenodict
git clone https://GitHub.com/morinted/stenodict master
git clone https://GitHub.com/morinted/stenodict gh-pages && cd gh-pages
git checkout gh-pages && git branch -D master
cd .. && pwd && ls

```

Now you will have a `stenodict` directory with folders `master` and `gh-pages` in it.

In order to develop the JavaScript component of the website, in the master branch, run `npm install`. After grabbing the dependencies, you should be able to start a server locally with `npm start`. `npm run build` places your `index.html` and needed files in `../gh-pages`, so it's best to have the folder structure explained above.
