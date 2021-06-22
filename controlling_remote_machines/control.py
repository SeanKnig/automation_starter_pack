import os
import sys

import threading
import datetime
import logging
import json
import pexpect
import getpass
from pymongo import MongoClient

logging.basicConfig(filename='c3po.log', level=logging.DEBUG)

class Control():
    def __init__(self):
        logging.info('c3po has started')
        self.db_mongo = MongoClient('localhost', 27017)
        self.now = datetime.datetime.now()

    def heartBeat(self):
        logging.info('c3po heartbeat'+ str(self.now))
        threading.Timer(5, self.heartBeat).start()
        print("_scout here", datetime.datetime.now())
    
    def controlKthulu(self):
        logging.info('Trying to access Kthulu' + str(self.now))
        threading.Timer(15, self.controlKthulu).start()
        print('Accessing Kthulu')

        collecting_volume_by_rank = self.db['vol_history_by_rank']
        try:
            child = pexpect.spawn ('ftp ftp.openbsd.org')
            child.expect ("'s password: ")
            child.sendline ('')
            child.expect (" ")
            child.sendline('cd asp/automation_starter_pack/intro_to_scraping/squid/spiders; python3 kthulu.py')

        except Exception as e:
            print(e)


        netScan = "netBotv0_01: \n ___________________Network Status__________________\n                    %s \n %s \n"%(result['status'], result['output'])
        print(netScan)


if __name__ == '__main__':
    c3po = Control()
    c3po.heartBeat()



