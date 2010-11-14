# -*- coding: utf-8 -*-

"""
Module implementing AddAccountDialog.
"""

from PyQt4 import QtCore 
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_addaccountdialog import Ui_AddAccountDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
    _toUtf8 = QtCore.QString.toUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    _toUtf8 = lambda s: s
def to_s(s):
    return str(_toUtf8(s))

class AddAccountDialog(QDialog, Ui_AddAccountDialog):
    """
    Add or edit an account
    """
    def __init__(self, parent = None, param = None ):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        if param is None:
            self.is_new = True
        else:
            self.is_new = False
            self.lineEdit_username.setText(_fromUtf8(param["user"]))
            self.type = param["type"]
    
    @pyqtSignature("")
    def on_buttonBox_accepted(self):
        """
        确定添加或者修改
        """
        conf = self.parent().parent().config
        log  = self.parent().parent().log
        user = to_s(self.lineEdit_username.text())
        if user in conf["outter_users"]:
            log.info("already exist,edit it..")
            
        if self.checkBox_remember.isChecked():
            conf["outter_users"][user] = to_s(self.lineEdit_password.text())
        else:
            conf["outter_users"][user] = ""
                    
        self.parent().refreshAccounts()
        self.parent().parent().save_config()
        self.parent().parent().refresh_gui()
        