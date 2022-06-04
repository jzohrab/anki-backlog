# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
from aqt import gui_hooks

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
    logger.debug('backlogging due cards')
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
