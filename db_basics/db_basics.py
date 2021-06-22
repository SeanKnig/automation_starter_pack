import os
import sys

import threading
import datetime
import logging
import json
import pymongo
from pymongo import MongoClient

logging.basicConfig(filename='c3po.log', level=logging.DEBUG)

class DB_Scout():
    def __init__(self):
        logging.info('c3po has started')
        self.db_mongo = MongoClient('localhost', 27017)
        self.now = datetime.datetime.now()

    def heartBeat(self):
        logging.info('c3po heartbeat'+ str(self.now))
        threading.Timer(5, self.heartBeat).start()
        print("_scout here", datetime.datetime.now())

    def insertDocument(self):
        threading.Timer(20, self.insertDocument).start()
        logging.info('newShip inserted at'+ str(self.now))
        try:
            #Database proclaimation
            self._insert_to_starships = self.db_mongo['StarShips']
            #CollectionName
            self.ship_class = self._insert_to_starships['Galaxy']

            myDict = {
                "blasters": "ultra 5000 photon plus",
                "solarSystem": "octahedral"
            }

            myShip = {
                "modelNum" : "GX-1907-P",
                "specifications": myDict
            }

            self.ship_class.insert_one(myShip)
            print("starship was inserted")
        except Exception as e:
            print("Startship was not inserted")
        

if __name__ == '__main__':
    c3po = DB_Scout()

    c3po.heartBeat()
    c3po.insertDocument()


