HOST = "irc.twitch.tv"
PORT = 6667
NICK = "kocchibot"
PASS = "oauth:f0poxer58r8997acjj28e2u0d4l6ac"
CHANNEL = "komornig_g"
RATE = 5
timePassed = 0


import socket
from bot import sendMessage

def initSocket():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send(bytes("PASS "  + PASS    + "\r\n", "UTF-8"))
    sock.send(bytes("NICK "  + NICK    + "\r\n", "UTF-8"))
    sock.send(bytes("JOIN #" + CHANNEL + "\r\n", "UTF-8"))
    sendMessage(sock, "Connected")
    return sock