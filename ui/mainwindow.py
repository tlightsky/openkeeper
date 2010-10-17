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
from ui.aboutdialog import AboutDialog
from ui.accountdialog import AccountDialog
from util import logger, config

try:
    _fromUtf8 = QtCore.QString.fromUtf8
    _toUtf8 = QtCore.QString.toUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    _toUtf8 = lambda s: s
def to_s(s):
    return str(_toUtf8(s))

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
        self.log  = logger.Log.getInst() # 从单例获得logger
        self.read_config()
        
        # 配置主程序相关
        self.statusBar.showMessage(_fromUtf8("主程序开始\n填入帐号密码就可以拨号了～"))
        
        #重定向命令输出
        QtCore.QObject.connect(self.outterCommandProcess, QtCore.SIGNAL(_fromUtf8("readyReadStandardOutput()")), self.outter_outputCommand)
        QtCore.QObject.connect(self.outterCommandProcess, QtCore.SIGNAL(_fromUtf8("readyReadStandardError()")), self.outter_outputCommand)
        
        #remove inner net sth
        #self.inner_login.hide()
    def read_config(self):
        self.config = config.OK_Config().read_config() 
        self.refresh_gui()
        
    def refresh_gui(self):
        self.outter_net_username.clear()
        #添加outter_users
        for item in self.config["outter_users"].keys():
            self.outter_net_username.addItem(_fromUtf8(item))
        self.outter_net_username.setEditText(_fromUtf8(self.config["outter_default_user"]))
        self.outter_net_password.setText(_fromUtf8(self.config["outter_users"][self.config["outter_default_user"]]))

        #添加outter_eths
        for item in self.config["outter_eths"]:
            self.outter_eth_select.addItem(_fromUtf8(item))
        self.outter_eth_select.setEditText(_fromUtf8(self.config["outter_default_eth"]))
    
        
    def save_config(self):
        config.OK_Config().save_config(self.config) 
    def check_save_user(self):    
        """
        拨号过程中会自动检测本帐号是否需要记录进入配置文件，网关信息自动记录
        """
        
        outter_eth_select=to_s(self.outter_eth_select.currentText())
        self.log.info("默认网关(eth)改为:%s" % outter_eth_select)
        self.config["outter_default_eth"]=outter_eth_select
        if outter_eth_select not in self.config["outter_eths"]:
            self.log.info("添加网关(eth):%s" % outter_eth_select)
            self.config["outter_eths"].append(outter_eth_select)
            
        self.log.info(self.config["outter_users"])
        if to_s(self.outter_net_username.currentText()) in self.config["outter_users"]:
            if self.outter_remember_passwd.isChecked():
                self.log.info("refresh old user password")
                self.config["outter_users"][to_s(self.outter_net_username.currentText())] = to_s(self.outter_net_password.text())
        else:
            if self.outter_remember_passwd.isChecked():
                self.config["outter_users"][to_s(self.outter_net_username.currentText())] = to_s(self.outter_net_password.text())
            else:
                self.config["outter_users"][to_s(self.outter_net_username.currentText())] = ""
        self.save_config()
                
    def outter_outputCommand(self):
        self.log.info("outter_outputCommand")
        # 处理标准输出流
        cmdoutput = QtCore.QByteArray()
        cmdoutput = self.outterCommandProcess.readAllStandardOutput()
        self.log.info(cmdoutput)
        txtoutput = QtCore.QString(_fromUtf8(cmdoutput))
        
        # 处理标准错误流
        self.outter_textBrowser.append(txtoutput)
        cmdoutput = self.outterCommandProcess.readAllStandardError()
        self.log.info(cmdoutput)
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
        实现挂断
        """
        self.statusBar.showMessage(_fromUtf8("外网挂断..."))
        self.outter_textBrowser.clear()
        program = QtCore.QString(_fromUtf8("ok-stop"))
        self.outterCommandProcess.terminate()
        # 防止UI卡死，只尝试三次
        for i in range(3):
            if QtCore.QProcess.NotRunning==self.outterCommandProcess.state():
                self.outterCommandProcess.start(program)
                break
            else:
                self.outterCommandProcess.kill()
                
    
    @pyqtSignature("")
    def on_outter_net_on_clicked(self):
        """
        实现点击后拨号
        """
        self.outter_textBrowser.clear()
        self.statusBar.showMessage(_fromUtf8("外网拨号中...，完成后可关闭"))
        self.check_save_user()
        
        # 调用脚本设置参数
        ok_config_program = " ".join(("ok-config",
                        "-u",str(self.outter_net_username.currentText()
                              +self.outter_net_username_extra.text()),
                        "-p",str(self.outter_net_password.text()),
                        "-e",str(self.outter_eth_select.currentText()),
                        "-s",)
                       )
        #self.log.info("ok_config_program : "+ok_config_program)
        os.system(ok_config_program)
        # 调用脚本进行拨号处理
        self.log.info("outter net on...")
        #args = QtCore.QStringList()
        program = QtCore.QString(_fromUtf8("ok"))
        self.outterCommandProcess.terminate()
        # 防止UI卡死，只尝试三次
        for i in range(3):
            if QtCore.QProcess.NotRunning==self.outterCommandProcess.state():
                self.outterCommandProcess.start(program)
                break
            else:
                self.outterCommandProcess.kill()
    
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
        账户管理模块
        """
        self.log.info("managin account")
        AccountDialog(self).show()
    
    @pyqtSignature("QString")
    def on_outter_net_username_currentIndexChanged(self, p0):
        """
        add password and checked to gui
        """
        text = to_s(p0)
        self.log.info("currentIndexChanged to %s"%text)
        if text in self.config["outter_users"] and self.config["outter_users"][text]:
            self.log.info("auto fill user %s" % text)
            self.outter_net_password.setText(
                    _fromUtf8(self.config["outter_users"][text]))
