#!/usr/bin/env python

import socket
import time
import requests
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 6001
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while :
	MESSAGE = raw_input("please enter the #pages,#spiders: ")
	# time.sleep(1)
	s.send(MESSAGE)

# data = s.recv(BUFFER_SIZE)
s.close()

print "closed"