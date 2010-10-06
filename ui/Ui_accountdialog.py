# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/FILES/source/py/qt/openkeeper/ui/accountdialog.ui'
#
# Created: Thu Oct  7 18:32:06 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        AccountDialog.setObjectName(_fromUtf8("AccountDialog"))
        AccountDialog.resize(407, 245)
        AccountDialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(AccountDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(AccountDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_add = QtGui.QPushButton(AccountDialog)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_edit = QtGui.QPushButton(AccountDialog)
        self.pushButton_edit.setObjectName(_fromUtf8("pushButton_edit"))
        self.verticalLayout_2.addWidget(self.pushButton_edit)
        self.pushButton_delete = QtGui.QPushButton(AccountDialog)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.verticalLayout_2.addWidget(self.pushButton_delete)
        self.pushButton_setDefault = QtGui.QPushButton(AccountDialog)
        self.pushButton_setDefault.setObjectName(_fromUtf8("pushButton_setDefault"))
        self.verticalLayout_2.addWidget(self.pushButton_setDefault)
        self.buttonBox = QtGui.QDialogButtonBox(AccountDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), AccountDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AccountDialog)

    def retranslateUi(self, AccountDialog):
        AccountDialog.setWindowTitle(QtGui.QApplication.translate("AccountDialog", "帐号管理", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("AccountDialog", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("AccountDialog", "类型", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("AccountDialog", "默认值", None, QtGui.QApplication.UnicodeUTF8))
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

