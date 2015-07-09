#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
EXECUTE_PORT = 6004
MONITOR_PORT = 6001
BUFFER_SIZE = 1024

# analyze component

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
        print "received data:", data

conn.close()

    # send message to managed element
    # m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # m.connect((TCP_IP, MONITOR_PORT))
    # m.send(data)
    # m.close()
    # print "sent data:", data