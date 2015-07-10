#!/usr/bin/env python

import socket
import requests
import json
import time

TCP_IP = '127.0.0.1'
MONITOR_PORT = 6001
ANALYZE_PORT = 6002
BUFFER_SIZE = 1024


# MONITOR COMPONENT:
# it communicates with the sensors to determine the 
# current number of crawlers and number of pages then 
# passes this information to the analyzer

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((TCP_IP, ANALYZE_PORT))
print 'Connected to send port'

while 1:

    # keep from sending to many requests
    time.sleep(3)

    # send request to the managed elements rest API
    data = requests.get('http://scrapyd-3d423455-1.nocturnedesign.cont.tutum.io:6802/listjobs.json?project=ManagedScraper')
    data = json.loads(data.text)

    # send the data to the analyze component
    data = "100," + str(len(data['running']))
    print "received data:", data
    a.send(data)
    print "sent data:", data


conn.close()
a.close()