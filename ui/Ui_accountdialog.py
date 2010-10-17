# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ok/gui/ui/accountdialog.ui'
#
# Created: Sat Oct 16 03:44:37 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        AccountDialog.setObjectName("AccountDialog")
        AccountDialog.resize(407, 245)
        AccountDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(AccountDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accounts = QtGui.QTreeWidget(AccountDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounts.sizePolicy().hasHeightForWidth())
        self.accounts.setSizePolicy(sizePolicy)
        self.accounts.setFrameShape(QtGui.QFrame.StyledPanel)
        self.accounts.setAutoScroll(True)
        self.accounts.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.accounts.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.accounts.setIndentation(0)
        self.accounts.setUniformRowHeights(True)
        self.accounts.setAnimated(False)
        self.accounts.setWordWrap(False)
        self.accounts.setHeaderHidden(False)
        self.accounts.setObjectName("accounts")
        self.accounts.header().setVisible(True)
        self.accounts.header().setCascadingSectionResizes(True)
        self.accounts.header().setDefaultSectionSize(100)
        self.accounts.header().setHighlightSections(False)
        self.accounts.header().setSortIndicatorShown(False)
        self.horizontalLayout.addWidget(self.accounts)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_add = QtGui.QPushButton(AccountDialog)
        self.pushButton_add.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_edit = QtGui.QPushButton(AccountDialog)
        self.pushButton_edit.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout_2.addWidget(self.pushButton_edit)
        self.pushButton_delete = QtGui.QPushButton(AccountDialog)
        self.pushButton_delete.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_setDefault = QtGui.QPushButton(AccountDialog)
        self.pushButton_setDefault.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_setDefault.setObjectName("pushButton_setDefault")
        self.verticalLayout_2.addWidget(self.pushButton_setDefault)
        self.buttonBox = QtGui.QDialogButtonBox(AccountDialog)
        self.buttonBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("clicked(QAbstractButton*)"), AccountDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AccountDialog)

    def retranslateUi(self, AccountDialog):
        AccountDialog.setWindowTitle(QtGui.QApplication.translate("AccountDialog", "帐号管理", None, QtGui.QApplication.UnicodeUTF8))
        self.accounts.headerItem().setText(0, QtGui.QApplication.translate("AccountDialog", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.accounts.headerItem().setText(1, QtGui.QApplication.translate("AccountDialog", "是否外网", None, QtGui.QApplication.UnicodeUTF8))
        self.accounts.headerItem().setText(2, QtGui.QApplication.translate("AccountDialog", "默认值", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add.setText(QtGui.QApplication.translate("AccountDialog", "添加帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_edit.setText(QtGui.QApplication.translate("AccountDialog", "修改帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setText(QtGui.QApplication.translate("AccountDialog", "删除帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_setDefault.setText(QtGui.QApplication.translate("AccountDialog", "设为默认值", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AccountDialog = QtGui.QDialog()
    ui = Ui_AccountDialog()
    ui.setupUi(AccountDialog)
    AccountDialog.show()
    sys.exit(app.exec_())

