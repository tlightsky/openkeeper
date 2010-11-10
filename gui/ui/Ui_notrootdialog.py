# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/ok/gui/ui/notrootdialog.ui'
#
# Created: Sat Oct 16 03:44:39 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NotrootDialog(object):
    def setupUi(self, NotrootDialog):
        NotrootDialog.setObjectName("NotrootDialog")
        NotrootDialog.resize(399, 151)
        self.buttonBox = QtGui.QDialogButtonBox(NotrootDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(NotrootDialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 281, 81))
        self.label.setObjectName("label")

        self.retranslateUi(NotrootDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NotrootDialog.accept)
        QtCore.QObject.connect(NotrootDialog, QtCore.SIGNAL("finished(int)"), NotrootDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(NotrootDialog)

    def retranslateUi(self, NotrootDialog):
        NotrootDialog.setWindowTitle(QtGui.QApplication.translate("NotrootDialog", "提示", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NotrootDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">请退出并使用root身份运行！</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NotrootDialog = QtGui.QDialog()
    ui = Ui_NotrootDialog()
    ui.setupUi(NotrootDialog)
    NotrootDialog.show()
    sys.exit(app.exec_())

