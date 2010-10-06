#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple.py
import sys, os
from PyQt4 import QtGui
from ui.mainwindow import MainWindow
from util import logger
log = logger.Log.getInst()
log.info("init main program")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mw= MainWindow()
    mw.show()
    sys.exit(app.exec_())
