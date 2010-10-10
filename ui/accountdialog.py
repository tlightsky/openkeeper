# -*- coding: utf-8 -*-

"""
Module implementing AccountDialog.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_accountdialog import Ui_AccountDialog
from ui.addaccountdialog import AddAccountDialog

class AccountDialog(QDialog, Ui_AccountDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        添加账户
        """
        AddAccountDialog(self).show()
    
    @pyqtSignature("")
    def on_pushButton_edit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_setDefault_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
