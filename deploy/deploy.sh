#!/bin/bash
# This must be run from project root.

source ./deploy/deploy.config

mkdir -p "${DESTDIR}/anki-backlog"
cp -R . "${DESTDIR}/anki-backlog" 2>&1 > /dev/null

pushd "${DESTDIR}/anki-backlog"
rm -rf .git
rm -rf deploy
popd

cp deploy/config.json "${DESTDIR}/anki-backlog"

echo
cat "${DESTDIR}/anki-backlog/config.json"
echo

echo "done.  Deployed:"
tree "${DESTDIR}/anki-backlog"

# Start Anki, with console window:
# ref https://addon-docs.ankiweb.net/console-output.html
/Applications/Anki.app/Contents/MacOS/AnkiMac
