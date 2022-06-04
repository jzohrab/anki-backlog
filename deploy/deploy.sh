#!/bin/bash
# This must be run from project root.

source ./deploy/deploy.config

mkdir -p "${DESTDIR}/anki-backlog"
cp -R . "${DESTDIR}/anki-backlog" 2>&1 > /dev/null

pushd "${DESTDIR}/anki-backlog"
rm -rf .git
rm -rf deploy
popd

echo "done.  Deployed:"
tree "${DESTDIR}/anki-backlog"
