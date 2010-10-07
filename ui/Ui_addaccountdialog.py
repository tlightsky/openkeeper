# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/FILES/source/py/qt/openkeeper/ui/addaccountdialog.ui'
#
# Created: Thu Oct  7 09:34:34 2010
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddAccountDialog(object):
    def setupUi(self, AddAccountDialog):
        AddAccountDialog.setObjectName(_fromUtf8("AddAccountDialog"))
        AddAccountDialog.resize(249, 167)
        AddAccountDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AddAccountDialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(AddAccountDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_type = QtGui.QComboBox(AddAccountDialog)
        self.comboBox_type.setObjectName(_fromUtf8("comboBox_type"))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_type)
        self.label = QtGui.QLabel(AddAccountDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_username = QtGui.QLineEdit(AddAccountDialog)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_username)
        self.label_2 = QtGui.QLabel(AddAccountDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_password = QtGui.QLineEdit(AddAccountDialog)
        self.lineEdit_password.setEnabled(False)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_password)
        self.checkBox_remember = QtGui.QCheckBox(AddAccountDialog)
        self.checkBox_remember.setObjectName(_fromUtf8("checkBox_remember"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_remember)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AddAccountDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(AddAccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddAccountDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddAccountDialog.accept)
        QtCore.QObject.connect(self.checkBox_remember, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_password.clear)
        QtCore.QObject.connect(self.checkBox_remember, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_password.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AddAccountDialog)

    def retranslateUi(self, AddAccountDialog):
        AddAccountDialog.setWindowTitle(QtGui.QApplication.translate("AddAccountDialog", "添加帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddAccountDialog", "帐号类型", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_type.setItemText(0, QtGui.QApplication.translate("AddAccountDialog", "内网帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_type.setItemText(1, QtGui.QApplication.translate("AddAccountDialog", "外网帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddAccountDialog", "用户名：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddAccountDialog", "密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_remember.setText(QtGui.QApplication.translate("AddAccountDialog", "记住密码", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddAccountDialog = QtGui.QDialog()
    ui = Ui_AddAccountDialog()
    ui.setupUi(AddAccountDialog)
    AddAccountDialog.show()
    sys.exit(app.exec_())

