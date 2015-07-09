#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
MONITOR_PORT = 6001
ANALYZE_PORT = 6002
BUFFER_SIZE = 1024


# MONITOR COMPONENT:
# it communicates with the sensors to determine the 
# current number of crawlers and number of pages then 
# passes this information to the analyzer

# listen at the monitor port
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.bind((TCP_IP, MONITOR_PORT))
m.listen(1)
conn, addr = m.accept()
print 'Connected to listener port:', addr

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((TCP_IP, ANALYZE_PORT))
print 'Connected to send port:', addr

while 1:

    data = conn.recv(BUFFER_SIZE)

    if not data: 
        pass
    else:
        print "received data:", data
        a.send(data)
        print "sent data:", data


conn.close()
a.close()