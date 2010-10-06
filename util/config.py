#!/usr/bin/python

from ConfigParser import ConfigParser
import os

class OK_Config:
    OK_GUI_CONF="ok-gui.cfg"
    OK_GUI_SECTION="ok-gui"
    def __init__(self,cfg=None):
        self.cfg = cfg or self.OK_GUI_CONF
        self.cf  = ConfigParser()
        if os.path.isfile(self.cfg):
            self.cf.read(self.cfg)
        else:
            self.cf.add_section(self.OK_GUI_SECTION)
            
    def set(self,opt,val):
        self.cf.set(self.OK_GUI_SECTION, opt, val)
    def get(self,opt):
        self.cf.get(self.OK_GUI_SECTION, opt)
    def write(self):
        self.cf.write(open(self.cfg,"w"))

if __name__=="__main__":
    okc = OK_Config()
    okc.write()
    