# -*- coding: utf-8 -*-

"""
Module implementing AboutDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_aboutdialog import Ui_AboutDialog

class AboutDialog(QDialog, Ui_AboutDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("QAbstractButton*")
    def on_buttonBox_clicked(self, button):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
