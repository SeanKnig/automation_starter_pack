import os
import sys

import threading
import datetime


class Robot():

    def __init__(self):
        print("Robot start")
    
    def heartBeat(self):
        threading.Timer(5, self.heartBeat).start()
        print("C3PO heartbeat", datetime.datetime.now())

    def doSomething(self):
        threading.Timer(2, self.doSomething).start()
        print("This happens every two seconds")
    
if __name__ == '__main__':
    c3po = Robot()

    c3po.heartBeat()
    c3po.doSomething()
