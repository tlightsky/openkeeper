# -*- coding: utf-8 -*-

"""
Module implementing AccountDialog.
"""

from PyQt4 import QtCore
from PyQt4.QtGui import QDialog, QTreeWidgetItem
from PyQt4.QtCore import pyqtSignature, QStringList

from Ui_accountdialog import Ui_AccountDialog
from ui.addaccountdialog import AddAccountDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
    _toUtf8 = QtCore.QString.toUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    _toUtf8 = lambda s: s
def to_s(s):
    return str(_toUtf8(s))

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
        self.refreshAccounts()
    
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        添加账户
        """
        AddAccountDialog(self).show()
        
    def refreshAccounts(self):
        self.accounts.clear()
        conf = self.parent().config
        for item in conf["outter_users"].keys():
            if item == conf["outter_default_user"]:
                self.accounts.addTopLevelItem(
                    QTreeWidgetItem( QStringList([_fromUtf8(item),_fromUtf8("YES"),_fromUtf8("是")])))
            else:
                self.accounts.addTopLevelItem(
                    QTreeWidgetItem( QStringList([_fromUtf8(item),_fromUtf8("YES"),_fromUtf8("否")])))
        
    @pyqtSignature("")
    def on_pushButton_edit_clicked(self):
        user = to_s(self.accounts.currentItem().text(0))
        self.parent().log.info(user)
        if True: # for outter
            AddAccountDialog(self,
                {"user":user,"pass":self.parent().config["outter_users"][user],"type":"outter"}
            ).show()
    
    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        delete a user
        """
        conf = self.parent().config
        user = to_s(self.accounts.currentItem().text(0))
        type = to_s(self.accounts.currentItem().text(1))
        if user in conf["outter_users"].keys() and "YES" == type:
            del conf["outter_users"][user]
        self.refreshAccounts()
        self.parent().save_config()
        self.parent().refresh_gui()
    
    @pyqtSignature("")
    def on_pushButton_setDefault_clicked(self):
        """
        Set it as default
        """
        conf = self.parent().config
        user = to_s(self.accounts.currentItem().text(0))
        type = to_s(self.accounts.currentItem().text(1))
        if user in conf["outter_users"].keys() and "YES" == type:
            self.parent().log.info("setting outter user %s as default "%user)
            conf["outter_default_user"]=user
        self.refreshAccounts()
        self.parent().save_config()
        self.parent().refresh_gui()
