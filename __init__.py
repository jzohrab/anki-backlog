# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from aqt import gui_hooks

# Queue types
QUEUE_SUSPENDED = -1
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
    logger.debug(f'Found {len(ids)} cards to backlog')
    for i in ids:
        c = mw.col.get_card(i)
        n = c.note()
        n.add_tag(BACKLOGTAG)
        col.update_note(n)
        c.queue = QUEUE_SUSPENDED
        col.update_card(c)

    # TODO

def releaseBacklogBatch() -> None:
    logger.debug('Releasing backlog')
    # TODO

logger.debug('Adding menus')

menus = [
    ['Backlog due cards', backlogDue],
    ['Release backlog batch', releaseBacklogBatch]
]
for m in menus:
    action = QAction(m[0], mw)
    qconnect(action.triggered, m[1])
    mw.form.menuTools.addAction(action)
