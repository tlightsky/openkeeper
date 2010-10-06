# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/FILES/source/py/qt/openkeeper/ui/aboutdialog.ui'
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

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(494, 236)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(AboutDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.graphicsView = QtGui.QGraphicsView(self.splitter)
        self.graphicsView.setMinimumSize(QtCore.QSize(150, 150))
        self.graphicsView.setMaximumSize(QtCore.QSize(150, 150))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/logo/logo.png);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:24pt; font-weight:600;\">OpenKeeper</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'LiHei Pro\'; font-size:24pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:12pt;\">版本：GUI 1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:12pt;\">程序设计：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:12pt;\">    Qt代码实现：王超（TLightSky）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:12pt;\">    登陆器脚本 ：王超（TLightSky）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'LiHei Pro\'; font-size:12pt;\">    Qt界面设计：郭安琪</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutDialog = QtGui.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())

