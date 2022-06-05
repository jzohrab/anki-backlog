from aqt import mw
import aqt.utils
from aqt.qt import *

import aqt.operations.scheduling as opssched
import aqt.operations.tag as opstag

# Queue types
BACKLOGTAG = 'backlog'
BATCHSIZE = 10

import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    filename=f'{os.path.expanduser("~")}/anki-backlog.log',
    format='%(asctime)s %(message)s'
)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)


config = mw.addonManager.getConfig(__name__)
decks = config['decks']
logger.debug(decks)


def backlogDue() -> None:
    logger.info('backlogging due cards')

    def get_ids(hsh):
        deckname = hsh['deck']
        search = f"deck:{deckname} is:due -is:suspended"
        scids = mw.col.find_cards(search)
        snids = mw.col.find_notes(search)
        logger.debug(f'{search} => {len(scids)} cards, {len(snids)} notes')
        return { 'cids': scids, 'nids': snids }

    cids = []
    nids = []
    for hsh in decks:
        r = get_ids(hsh)
        cids += r['cids']
        nids += r['nids']

    logger.debug(f'Suspending {len(cids)} cards, tagging {len(nids)} notes')
    opssched.suspend_cards(
        parent = mw,
        card_ids = cids
    ).run_in_background()
    opstag.add_tags_to_notes(
        parent = mw,
        note_ids = nids,
        space_separated_tags = BACKLOGTAG
    ).run_in_background()


def releaseBacklogBatch() -> None:
    logger.debug('Releasing backlog')

    def get_ids(hsh):
        deckname = hsh['deck']
        batchsize = hsh['release-size']
        sortdesc = hsh['release-by'] == 'oldest'

        search = f"deck:{deckname} is:suspended tag:{BACKLOGTAG}"
        ids = mw.col.find_cards(search)
        logger.debug(f'Found {len(ids)} cards in backlog')
        cards = [mw.col.get_card(i) for i in ids]
        cards.sort(key=lambda c: c.ivl, reverse=sortdesc)
        cards = cards[0:batchsize]
        scids = [c.id for c in cards]
        snids = [c.note().id for c in cards]

        logger.debug(f'{search} => {len(scids)} cards, {len(snids)} notes')
        return { 'cids': scids, 'nids': snids }

    cids = []
    nids = []
    for hsh in decks:
        r = get_ids(hsh)
        cids += r['cids']
        nids += r['nids']

    logger.debug(f'Unsuspending {len(cids)} cards, untagging {len(nids)} notes')
    opssched.unsuspend_cards(
        parent = mw,
        card_ids = cids
    ).run_in_background()
    opstag.remove_tags_from_notes(
        parent = mw,
        note_ids = nids,
        space_separated_tags = BACKLOGTAG
    ).run_in_background()


logger.debug('Adding menus')
menus = [
    ['Backlog due cards', backlogDue],
    ['Release backlog batch', releaseBacklogBatch]
]
for m in menus:
    action = QAction(m[0], mw)
    aqt.utils.qconnect(action.triggered, m[1])
    mw.form.menuTools.addAction(action)
