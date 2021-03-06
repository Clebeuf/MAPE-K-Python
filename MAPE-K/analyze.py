#!/usr/bin/env python

import socket
import math

TCP_IP = '127.0.0.1'
ANALYZE_PORT = 6002
PLAN_PORT = 6003
BUFFER_SIZE = 1024


# ANALYZER COMPONENT
# recieves current state of the system information 
# from the monitor and identifies changes that need to
# be made. For example, if there are more spiders than 
# needed close the extras

# listen at the analyze port
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind((TCP_IP, ANALYZE_PORT))
a.listen(1)
conn, addr = a.accept()
print 'Connected to listener port:', addr

# send message to the plan port
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.connect((TCP_IP, PLAN_PORT))
print 'Connected to send port:', addr

while 1:

    message = "do nothing"

    # read in current policy
    policy = open("policy.txt")
    data = policy.read().split();
    pages_per_spider = int(data[0])
    min_spiders = int(data[1])
    max_spiders = int(data[2])
    policy.close()

    data = conn.recv(BUFFER_SIZE)
    print "received data:", data

    if data:
        data = data.split(",")
        numb_pages = float(data[0])
        numb_spiders = float(data[1])

        spiders_needed = int(math.ceil(numb_pages/pages_per_spider))
        print "spiders needed: " + str(spiders_needed) + ", max: " + str(max_spiders) + ", min: " + str(min_spiders)

        # check for max number of spiders in policy
        if (numb_spiders > max_spiders):
            message = "too many spiders"
        # check for min number of spiders in policy
        elif (numb_spiders < min_spiders):
            message = "not enough spiders"
        # kill all spiders
        elif (max_spiders == 0) and (min_spiders == 0):
            message = "too many spiders"
        # check if we need to increase spiders
        elif spiders_needed > numb_spiders:
            if (numb_spiders < max_spiders):
                message = "not enough spiders"
        # check if we need to decrease spiders
        elif spiders_needed < numb_spiders:
            if (numb_spiders > min_spiders):
                message = "too many spiders"


        # send request
        p.send(message)
        print "sent data:", message

conn.close()
p.close()