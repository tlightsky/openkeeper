#!/usr/bin/python
# -*- coding: utf-8 -*-

from ConfigParser import ConfigParser
import os, stat

class OK_Config:
    OK_GUI_CONF="/usr/local/openkeeper/ok-gui.cfg"
    OK_GUI_SECTION="ok-gui"
    def __init__(self,cfg=None):
        self.cfg = cfg
        self.load()
        
    def load(self):
        self.cfg = self.cfg or self.OK_GUI_CONF
        self.cf  = ConfigParser()
        if os.path.isfile(self.cfg):
            self.cf.read(self.cfg)
        else:
            self.cf.add_section(self.OK_GUI_SECTION)
            self.set("outter_users","chongzhi")
            self.set("outter_passes","123456")
            self.set("outter_default_user","chongzhi")
            self.set("outter_eths","eth0,eth1,wlan0")
            self.set("outter_default_eth","eth0")
            
    def set(self,opt,val):
        self.cf.set(self.OK_GUI_SECTION, opt, val)
    def get(self,opt):
        self.cf.get(self.OK_GUI_SECTION, opt)
    def save(self):
        self.cf.write(open(self.cfg,"w"))
    
    def read_config(self):
        """
        参数： outter_users,outter_passes,outter_default_user,outter_eths,outter_default_eth
        """
        ret = {}
        for item in self.cf.items(self.OK_GUI_SECTION):
            ret[item[0]] = item[1]
        tmp = {}    
        for item in zip(ret["outter_users"].split(','),ret["outter_passes"].split(',')):
            tmp[item[0]] = item[1]
        ret['outter_users']=tmp
        del ret['outter_passes'] 
        ret['outter_eths'] = ret['outter_eths'].split(',')
        return ret
        
    def save_config(self,conf):
        outter_users = conf["outter_users"].keys()
        outter_passes= conf["outter_users"].values()
        self.set("outter_users",','.join(outter_users))
        self.set("outter_passes",','.join(outter_passes))
        self.set("outter_default_user",conf["outter_default_user"])
        self.set("outter_eths",",".join(conf["outter_eths"]))
        self.set("outter_default_eth",conf["outter_default_eth"])
        self.save()
        os.chmod(self.cfg, 0600);
     
if __name__=="__main__":
    okc = OK_Config()
    cfg = okc.read_config()
    okc.save_config(cfg)
    