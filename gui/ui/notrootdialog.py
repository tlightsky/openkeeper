# -*- coding: utf-8 -*-

"""
Module implementing NotrootDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_notrootdialog import Ui_NotrootDialog

class NotrootDialog(QDialog, Ui_NotrootDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
    def accept(self):
        self.parent().close()    
