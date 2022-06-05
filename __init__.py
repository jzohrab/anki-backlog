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


def backlogDue() -> None:
    logger.info('backlogging due cards')
    deckname = 'Spanish::03\_Spanish\_audio'
    search = f"deck:{deckname} is:due -is:suspended"
    col = mw.col
    ids = col.find_cards(search)
    nids = col.find_notes(search)
    logger.debug(f'Suspending {len(ids)} cards, tagging {len(nids)} notes')
    opssched.suspend_cards(
        parent = mw,
        card_ids = ids
    ).run_in_background()
    opstag.add_tags_to_notes(
        parent = mw,
        note_ids = nids,
        space_separated_tags = BACKLOGTAG
    ).run_in_background()


def releaseBacklogBatch() -> None:
    logger.debug('Releasing backlog')
    deckname = 'Spanish::03\_Spanish\_audio'
    search = f"deck:{deckname} is:suspended tag:{BACKLOGTAG}"
    ids = mw.col.find_cards(search)

    logger.debug(f'Found {len(ids)} cards in backlog')
    cards = [mw.col.get_card(i) for i in ids]
    cards.sort(key=lambda c: c.ivl, reverse=True)
    cards = cards[0:BATCHSIZE]
    ids = [c.id for c in cards]
    nids = [c.note().id for c in cards]

    logger.debug(f'Unsuspending {len(ids)} cards, untagging {len(nids)} notes')
    opssched.unsuspend_cards(
        parent = mw,
        card_ids = ids
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
