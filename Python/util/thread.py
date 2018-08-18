#!/usr/bin/python3

import thread
import time
import subprocess
import os
import threading
from multiprocessing import Process, Lock

lock = Lock()

def sendAllSync(message, result=False):
    for device in conectedDevices:
        Process(target=sendMessage, args=(device, message, result,)).start()
    # threads = []
    # try:
    #     for device in conectedDevices:
    #         t = threading.Thread(target=sendMessage, args=(device, message, result,))
    #         threads.append(t)
    #     print(threading.activeCount())
    #     for t in threads:
    #         t.start()
    #         t.join()
    #     print ("Exiting Main Thread")
    # except:
    #     print("thread error")

def sendMessage(deviceId, message, result=False):
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        text = subprocess.check_output(cmd , shell=True)
        return text
    else :
        os.system(cmd)
        return "no text"

def addRootPath() :
    # return "C:\\Users\\imfine\\AppData\\Local\\Android\\Sdk\\platform-tools\\"
    return "/Users/suyoung/Library/Android/sdk/platform-tools/"

def adbPath() :
    return addRootPath()+"adb"

cmd = '{} devices'.format(adbPath())
devices = subprocess.check_output(cmd, shell=True)
conectedDevices = list()

devicelist = str(devices).split('\\n')
del devicelist[0]
for device in devicelist:
    device = device.replace(" ", "")
    device = device.replace("'", "")
    device = device.replace("\\tdevice", "")
    if len(device) >= 16:
        conectedDevices.append(device)

def sendAllMessage(message, result=False):
    for device in conectedDevices:
        sendMessage(device, message, result)


# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: unable to start thread")
def test(device) :
    print(device)
    print("!!")
# threading.Thread(target=test).start()

sendAllSync("shell input keyevent 26")
sendAllSync("shell input keyevent 82")


while 1:
   pass

