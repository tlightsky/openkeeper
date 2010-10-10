# -*- coding: utf-8 -*-

"""
Module implementing AddAccountDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_addaccountdialog import Ui_AddAccountDialog

class AddAccountDialog(QDialog, Ui_AddAccountDialog):
    """
    Add or edit account
    """
    def __init__(self, parent = None, type = None ):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        # if type is None,
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        确定添加或者修改
        """
        
