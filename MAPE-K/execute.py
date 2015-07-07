#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
EXECUTE_PORT = 5004
MONITOR_PORT = 5001
BUFFER_SIZE = 1024

# analyze component

while 1:

    # listen at the analyze port
    e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    e.bind((TCP_IP, EXECUTE_PORT))
    e.listen(1)
    conn, addr = e.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "received data:", data
    conn.close()

    # send message to the plan port
    m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m.connect((TCP_IP, MONITOR_PORT))
    m.send(data)
    m.close()
    print "sent data:", data