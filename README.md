# README

Stenodict runs on [Jekyll](https://jekyllrb.com/).



## Adding a dictionary

1. Fork Stenodict and checkout `gh-pages`.

2. Copy template dictionary info Markdown file:

        $ cp _dictionaries/_template_dictionary.md _dictionaries/YOUR_DICTIONARY_NAME.md

3. Add your dictionary to the `dictionaries/` directory. For example:

        $ cp dictionaries/_template_dictionary.json _dictionaries/YOUR_DICTIONARY_NAME.json
        $ $EDITOR _dictionaries/YOUR_DICTIONARY_NAME.json

4. Edit your new dictionary file and Markdown info file about your new dictionary. Check your dictionary using `jsonlint`:

        $ jsonlint dictionaries/*.json

5. Make a [Pull Request to Stenodict's `gh-pages` branch](https://github.com/openstenoproject/stenodict/pull/new/gh-pages).



## Running Jekyll

1. Install bundler at the command prompt if you haven't yet:

        $ gem install bundler

2. At the command prompt, install gems from `Gemfile`, including `jekyll`:

        $ bundle install

3. Serve Jekyll site:

        $ bundle exec jekyll serve

4. Browse to <http://localhost:4000/stenodict/>.

