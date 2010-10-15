# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ok/gui/ui/addaccountdialog.ui'
#
# Created: Sat Oct 16 01:22:48 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddAccountDialog(object):
    def setupUi(self, AddAccountDialog):
        AddAccountDialog.setObjectName("AddAccountDialog")
        AddAccountDialog.resize(249, 187)
        AddAccountDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(AddAccountDialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(AddAccountDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_type = QtGui.QComboBox(AddAccountDialog)
        self.comboBox_type.setEnabled(False)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_type)
        self.label = QtGui.QLabel(AddAccountDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_username = QtGui.QLineEdit(AddAccountDialog)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_username)
        self.label_2 = QtGui.QLabel(AddAccountDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_password = QtGui.QLineEdit(AddAccountDialog)
        self.lineEdit_password.setEnabled(True)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_password)
        self.checkBox_remember = QtGui.QCheckBox(AddAccountDialog)
        self.checkBox_remember.setCursor(QtCore.Qt.PointingHandCursor)
        self.checkBox_remember.setChecked(True)
        self.checkBox_remember.setObjectName("checkBox_remember")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBox_remember)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AddAccountDialog)
        self.buttonBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(AddAccountDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddAccountDialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddAccountDialog.accept)
        QtCore.QObject.connect(self.checkBox_remember, QtCore.SIGNAL("clicked()"), self.lineEdit_password.clear)
        QtCore.QObject.connect(self.checkBox_remember, QtCore.SIGNAL("toggled(bool)"), self.lineEdit_password.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AddAccountDialog)

    def retranslateUi(self, AddAccountDialog):
        AddAccountDialog.setWindowTitle(QtGui.QApplication.translate("AddAccountDialog", "添加帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddAccountDialog", "帐号类型", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_type.setItemText(0, QtGui.QApplication.translate("AddAccountDialog", "外网帐号", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_type.setItemText(1, QtGui.QApplication.translate("AddAccountDialog", "内网帐号", None, QtGui.QApplication.UnicodeUTF8))
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

