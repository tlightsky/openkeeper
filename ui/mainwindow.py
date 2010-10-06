#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os
import subprocess
from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_mainwindow import Ui_MainWindow
from aboutdialog import AboutDialog
from util import logger

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    outterCommandProcess=QtCore.QProcess();
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        # 配置主程序相关
        self.statusBar.showMessage(_fromUtf8("主程序开始\n填入帐号密码就可以拨号了～"))
        self.log = logger.Log.getInst() # 从单例获得logger
        
        #重定向命令输出
        QtCore.QObject.connect(self.outterCommandProcess, QtCore.SIGNAL(_fromUtf8("readyReadStandardOutput()")), self.outter_outputCommand)
        QtCore.QObject.connect(self.outterCommandProcess, QtCore.SIGNAL(_fromUtf8("readyReadStandardError()")), self.outter_outputCommand)
        
        #remove inner net sth
        #self.inner_login.hide()

    def outter_outputCommand(self):
        self.log.info("outter_outputCommand")
        # 处理标准输出流
        cmdoutput = QtCore.QByteArray()
        cmdoutput = self.outterCommandProcess.readAllStandardOutput()
        txtoutput = QtCore.QString(_fromUtf8(cmdoutput))
        
        # 处理标准错误流
        self.outter_textBrowser.append(txtoutput)
        cmdoutput = self.outterCommandProcess.readAllStandardError()
        txtoutput = QtCore.QString(_fromUtf8(cmdoutput))
        self.outter_textBrowser.append(txtoutput)
        
    @pyqtSignature("")
    def on_action_about_triggered(self):
        """
        Slot documentation goes here.
        """
        AboutDialog(self).show()
    
    @pyqtSignature("")
    def on_outter_net_off_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_outter_net_on_clicked(self):
        """
        实现点击后拨号
        """
        # 先检查存储帐号否，若是，则存储
        # 调用脚本设置参数
        # 调用脚本进行拨号处理
        self.log.info("outter net on...")
        #args = QtCore.QStringList()
        program = QtCore.QString("ok")
        self.outterCommandProcess.terminate()
        self.outterCommandProcess.start(program)
        #self.outterCommandProcess.
    
    @pyqtSignature("")
    def on_outter_remember_passwd_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("bool")
    def on_start_onboot_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_account_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
