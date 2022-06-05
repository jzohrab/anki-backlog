# Anki backlog management add-on.

Add-on: https://ankiweb.net/shared/info/1480367353

This add-on adds a few nice-to-have items to the tools menu:

| Tools menu entry | Action |
| --- | --- |
| "Backlog due cards" | Suspend all due cards in the decks this add-on helps manage, and tag as "backlog". |
| "Release backlog batch" | Unsuspend cards tagged with "backlog". |

The decks managed by the add-on, the size of each backlog release batch, and the backlog release order, are configured in the add-on config.

## Install

Install this add-on the usual way, or (?) clone this repo and put it in your Anki add-ons folder.

## Config

In the add-on config, Tools > Add-Ons, select this add-on and click "Config".  See config.md for more.  Anki shows this same config.md as help during configuration.


# Development

## Local deploy

I do development in a folder outside of Anki AddOns, and then I "deploy" (copy) the code to the addons folder.

To do so (at least on a Mac):

```
cd deploy/
cp deploy.config.example deploy.config
# ... now edit deploy/deploy.config for your system
cd ..
```

Run the deployment script from root:

```
$ ./deploy/deploy.sh
```

## Releasing

Ref https://addon-docs.ankiweb.net/sharing.html re sharing the zip.

On Mac:

Run `./zipping.sh`

Upload the .zip file to https://ankiweb.net/shared/info/1480367353


# Change log:

* 2022-06-05: Handle deck names with spaces.
* 2022-06-04: Initial release