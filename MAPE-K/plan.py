#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
PLAN_PORT = 6003
EXECUTE_PORT = 6004
BUFFER_SIZE = 1024

# PLAN COMPONENT
# receives the request for the change and formulates a plan

# listen at the plan port
p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.bind((TCP_IP, PLAN_PORT))
p.listen(1)
conn, addr = p.accept()
print 'Connected to listener port:', addr

# send message to the execute port
e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
e.connect((TCP_IP, EXECUTE_PORT))
print 'Connected to send port:', addr

while 1:
    message = "do nothing"
    
    data = conn.recv(BUFFER_SIZE)

    if not data: 
        pass
    else:
        print "received data:", data
        if data == "not enough spiders":
            message = "increase spiders"
        elif data == "too many spiders":
            message = "decrease spiders"

        e.send(message)
        print "sent data:", message


conn.close()
e.close()