#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
PLAN_PORT = 5003
EXECUTE_PORT = 5004
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


# analyze component

while 1:

    # listen at the analyze port
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p.bind((TCP_IP, PLAN_PORT))
    p.listen(1)
    conn, addr = p.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "received data:", data
    conn.close()

    # send message to the plan port
    e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    e.connect((TCP_IP, EXECUTE_PORT))
    e.send(data)
    e.close()
    print "sent data:", data