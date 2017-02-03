import socket
from time import time
from cfg import *
from buddies import *

def sendMessage(sock, message):
    sock.send(bytes("PRIVMSG #" + CHANNEL + " :" + message + "\r\n", "UTF-8"))
    
def respondToCommand(sock, message, username, start):
    if "@kocchibot" in message.lower():
        sendMessage(sock, randomizePhrase())
        
    elif message == "!commands":
        sendMessage(sock, "Avaliable commands: !rank, !playlist, !author, !command, !k00pa, !uptime")
        
    elif message == "!rank":
        sendMessage(sock, "Current rank: Diamond III")
        
    elif message == "!playlist":
        sendMessage(sock, "Current playlist: Pandora doesn't work")
        
    elif message == "!author":
        sendMessage(sock, "KocchiBot is a bot mady by Komor. It's written in Python 3.5, you can check commands by typing \"!commands\"")
        
    elif message == "!uptime":
        sendMessage(sock, getUpTime(start))
        
    elif message == "!k00pa":
        sendMessage(sock, "Nothing here yet :^)")

def readMessage(sock, message, username, start):
    if lookForCapsLock(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't abuse CapsLock! (timeout for 60 seconds)".format(username))
        
    elif lookForSwears(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't curse that much! (timeout for 60 seconds)".format(username))
        
    elif lookForLongMsg(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't put walls of text! (timeout for 60 seconds)".format(username))
        
    else:
        if time() - timePassed > RATE:
            respondToCommand(sock, message, username, start)