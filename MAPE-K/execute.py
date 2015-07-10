#!/usr/bin/env python

import socket
import json
import requests

TCP_IP = '127.0.0.1'
EXECUTE_PORT = 6004
MONITOR_PORT = 6001
BUFFER_SIZE = 1024

# EXECUTE COMPONENT
# sends the request for a change to the effectors
# of the managed resource

# listen at the analyze port
e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
e.bind((TCP_IP, EXECUTE_PORT))
e.listen(1)
conn, addr = e.accept()
print 'Connected to listener port:', addr

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        pass
    else:
        print "received data: ", data

        # if recieved a message to decrease the number of spiders
        if data == 'decrease spiders':
            jobs = requests.get('http://scrapyd-3d423455-1.nocturnedesign.cont.tutum.io:6802/listjobs.json?project=ManagedScraper')
            jobs = json.loads(jobs.text)
            job_id = jobs['running'][-1]['id']
            print "killing job: " + str(job_id)
            payload = {'project': 'ManagedScraper', 'job': job_id}
            r = requests.post("http://scrapyd-3d423455-1.nocturnedesign.cont.tutum.io:6802/cancel.json", data=payload)
            print(r.text)

        #if recieved message to increase number of spiders
        elif data == 'increase spiders':
            payload = {'project': 'ManagedScraper', 'spider':'dmoz-spider'}
            r = requests.post("http://scrapyd-3d423455-1.nocturnedesign.cont.tutum.io:6802/schedule.json", data=payload)
            print(r.text)

conn.close()
