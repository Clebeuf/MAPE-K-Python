#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
ANALYZE_PORT = 6002
PLAN_PORT = 6003
BUFFER_SIZE = 1024
message = "do nothing"


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

    # read in current policy
    policy = open("policy.txt")
    data = policy.read().split();
    min_spiders = int(data[0])
    pages_per_spider = int(data[1])
    policy.close()

    data = conn.recv(BUFFER_SIZE)
    print "received data:", data

    if not data: 
        pass
    else:
        data = data.split(",")
        numb_pages = int(data[0])
        numb_spiders = int(data[1])

        if (numb_pages/numb_spiders) > pages_per_spider:
            message = "not enough spiders"
        elif (numb_pages/numb_spiders) < pages_per_spider:
                message = "too many spiders"

        p.send(message)
        print "sent data:", message


conn.close()
p.close()