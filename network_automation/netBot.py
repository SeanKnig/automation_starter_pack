import os, sys, threading

import logging
import datetime
from pymongo import MongoClient
from subprocess import Popen, PIPE, STDOUT
import threading

import json
import re

logging.basicConfig(filename='netBot.log', level=logging.DEBUG)

class Robot():
    def __init__(self):
        logging.info("Starting NetBot v0_01")
        print("\nNetBot at your service", datetime.datetime.now())
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['netBot'] 
        self.now = datetime.datetime.today().replace(microsecond=0)

    def heartBeat(self):
        threading.Timer(5, self.heartBeat).start()
        logging.info("netBot heartbeat"+ str(self.now))
        print("netBot Heartbeat:", self.now)
    
    def netWorkScan(self):
        threading.Timer(30, self.netWorkScan).start()
        logging.info("netWorkScan start")

        collecting_network_scan = self.db['network_history']
        command = ["bash", "./scripts/scanNetwork.sh"]
        devices_ = {}
        monitor_ = {}

        try:
            scanNetProcess = Popen(command, stdout=PIPE, stderr=STDOUT)
            output = scanNetProcess.stdout.read()
            exitstatus = scanNetProcess.poll()

            string_of_output = str(output)
            
            lines = re.split(r'\\nNmap scan report for +|\\n +', string_of_output)
            #Get summary and monitor metrics
            summary = lines.pop(-1)
            summary = summary.replace('\\nHost is up.\\nNmap done: ', ' ')
            summary = summary.replace(' IP addresses ', ' ')
            summary = summary.replace(' scanned in ', '')
            summary = summary.replace('hosts up', '')
            summary = summary.replace(' seconds\\n', '')
            summary = summary.replace('(', '')
            summary = summary.replace(')', '')
            monitor = summary.split(" ")
        
            monitor = summary.split(" ")
            print(monitor)
            
            monitor_ = {
                "mother_device": monitor[0],
                'mother_ip': monitor[1],
                "ip_address_count": monitor[2],
                "hosts_connected": monitor[3],
                "scan_time": monitor[4]
            }

            self.host_count = monitor[3]
            for line in lines[1::1]:
                #Discard unwanted strings
                line = line.replace('\\nHost is up ', ' ')
                line = line.replace('.\\nMAC Address: ', ' ')
                line = line.replace('\\nHost is up.\\nNmap done: ', '\n')
                line = line.replace(' latency', '')
                line = line.replace('(', '')
                line = line.replace(')', '')
                line = line.replace('.lan', '_lan')

                device = line.split(" ")
                device_detail = {
                    device[0]:
                    {
                        "ip_address": device[1],
                        "latency": device[2],
                        "mac_address": device[3],
                        "mac_details": device[4:]
                    }
                }
                devices_.update(device_detail)

            netMap = {
                "netBotv0_01Scan_%s"%(self.now): {
                    "Summary": monitor_,
                    "Device_Details": devices_
                }
            }
            netMapReport = json.dumps(netMap, indent=4)

            if (exitstatus==0):
                result= {"status": "ScanSuccess", "output": lines}
                collecting_network_scan.insert_one(netMap)
                logging.info('netBotv0_01 Success at: '+str(self.now)+" Inserted into database successfully")
                netMap.clear()
                monitor_.clear()
                devices_.clear()
            else:
                result = {"status": "FAILED || NETWORK SCAN UNSUCCESSFUL", "output": netMapReport}
            
        except Exception as e:
            result = {"status": "failed", "output": str(e)}
            pass
            
        netScan = "netBotv0_01: \n ___________________Network Status__________________\n                    %s \n %s \n"%(result['status'], result['output'])
        print(netScan)

if __name__ == "__main__":
    c3po = Robot()

    c3po.heartBeat()
    c3po.netWorkScan()
    
