#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
ANALYZE_PORT = 5002
PLAN_PORT = 5003
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


# analyze component

while 1:

    # listen at the analyze port
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.bind((TCP_IP, ANALYZE_PORT))
    a.listen(1)
    conn, addr = a.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "received data:", data
    conn.close()

    # send message to the plan port
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p.connect((TCP_IP, PLAN_PORT))
    p.send(data)
    p.close()
    print "sent data:", data