from time import time
from random import randint
import string

def getUpTime(start):
    seconds = int(time()) - start
    minutes = int(seconds/60)
    hours   = int(minutes/60)
    seconds = seconds - hours*3600 - minutes*60
    return "Stream has been live for {} hours {} minutes {} seconds.".format(hours, minutes, seconds)

def randomizePhrase():
    phrases = [
        "I'm engaged",
        "I'm not attracted to 3D men",
        "I've run out of ideas"
    ]
    
    return phrases[randint(0, 2)]

def lookForCapsLock(message):
    capsCounter = 0;
    
    if(len(message) > 10):
        for char in message:
            if char == char.upper():
                capsCounter += 1
        if float(capsCounter)/float(len(message)) > 0.6:
            return True
        else:
            return False
    else:
        return False

def lookForSwears(message):
    swearsCounter = 0
    swears = [
        "kurwa",
        "chuj"
    ]
    
    for element in message.split():
        for swear in swears:
            if element.lower() == swear:
                swearsCounter += 1
    if swearsCounter > 5:
        return True
    else:
        return False
    
def lookForLongMsg(message):
    if(len(message) > 480):
        return True
    else:
        return False