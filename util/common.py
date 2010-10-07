#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def is_root():
    return 0==os.geteuid()

if __name__=="__main__":
    print "test root:"
    if is_root():
        print "You are root!Take care."
    else:
        print "You are not root!Goodbye"
        
    