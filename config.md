# Configuration

The `decks` entry describes the decks this add-on helps you manage, and how the backlog is cleared.

## `deck`

This is the "deck name" as used in the Anki browser search, *excluding* the `deck:` indicator.  Backslashes must be replaced with double backslashes, due to the way that python handles the data.

For example, if you had a parent deck, "Spanish", with child deck "01_Spanish_Vocab":

* The browser search string would be `deck:Spanish::01\_Spanish\_Vocab`
* The add-on config string would be `"deck": "Spanish::01\\_Spanish\\_Vocab"`

## `release-by`

This can be either "oldest" or "newest".

Each have plusses and minuses.  If you select "oldest", your newer cards might get stale as you go through the backlog, and so you might end up forgetting a lot of them.  If "newest", you might rip through those, but then get slower as you get further along.

## `release-size`

The number of cards to be released.

# A full example:

