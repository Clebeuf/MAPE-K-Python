#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
MONITOR_PORT = 5001
ANALYZE_PORT = 5002
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


# monitor component

while 1:

    # listen at the monitor port
    m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    m.bind((TCP_IP, MONITOR_PORT))
    m.listen(1)
    conn, addr = m.accept()
    print 'Connection address:', addr
    data = conn.recv(BUFFER_SIZE)
    print "received data:", data
    conn.close()

    # send message to the analysis port
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.connect((TCP_IP, ANALYZE_PORT))
    a.send(data)
    a.close()
    print "sent data:", data