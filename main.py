#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple.py
import sys, os
from PyQt4 import QtGui
from ui.mainwindow import MainWindow
from util import logger
from util.common import *
from ui.notroot import NotrootDialog

log = logger.Log.getInst()
log.info("init main program")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw= MainWindow()
    mw.show()
    #检查是否root
    if not is_root():
        nd = NotrootDialog(mw)
        nd.show()
        mw.setFocusProxy(nd)
        log.info("Not root,click to close!")
    
    sys.exit(app.exec_())
