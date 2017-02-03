import socket
import string
import time
from cfg import *
from bot import readMessage

sock = initSocket()
start = int(time.time())

while True:
    for line in str(sock.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue
        
        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]
            
        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]
        
        readMessage(sock, message, username, start)
        timePassed = time.time()