#!/usr/bin/python

import logging
import threading  
  
class Log(object):  
    def __init__():  
        "disable the __init__ method"  
  
    __inst = None # make it so-called private  
  
    __lock = threading.Lock() # used to synchronize code  
 
    @staticmethod  
    def getInst():
        Log.__lock.acquire()  
        if not Log.__inst:  
            Log.__inst = Log.getLogger()
        Log.__lock.release()  
        return Log.__inst

    @staticmethod  
    def getLogger():
        """
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")
        """
        #create logger
        logger = None
        logger = logging.getLogger("openkeeper-gui")
        logger.setLevel(logging.DEBUG)
        #create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        #create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")
        #add formatter to ch
        ch.setFormatter(formatter)
        #add ch to logger
        logger.addHandler(ch)
        logger.info("logger init finish")
        return logger
        #"application" code

if __name__ == "__main__":
    lg = Log.getInst()
    lg.info("123")
    lg1 = Log.getInst()
    lg1.info("456")
    print lg is lg1
