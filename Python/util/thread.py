# #!/usr/bin/python3

# import thread
# import time
import subprocess
import os
# import threading
from multiprocessing import Process, Lock

# lock = Lock()

# def sendAllSync(message, result=False):
#     for device in conectedDevices:
#         Process(target=sendMessage, args=(device, message, result,)).start()
#     # threads = []
#     # try:
#     #     for device in conectedDevices:
#     #         t = threading.Thread(target=sendMessage, args=(device, message, result,))
#     #         threads.append(t)
#     #     print(threading.activeCount())
#     #     for t in threads:
#     #         t.start()
#     #         t.join()
#     #     print ("Exiting Main Thread")
#     # except:
#     #     print("thread error")

def sendMessage(deviceId, message, result=False):
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        text = subprocess.check_output(cmd , shell=True)
        return text
    else :
        os.system(cmd)
        return "no text"

def adbPath() :
    return "C:\\Users\\imfine\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb"

cmd = '{} devices'.format(adbPath())
devices = subprocess.check_output(cmd, shell=True)
conectedDevices = list()

devicelist = str(devices).split('\\n')
del devicelist[0]
for device in devicelist:
    device = device.replace("\\r", "")
    device = device.replace(" ", "")
    device = device.replace("'", "")
    device = device.replace("\\tdevice", "")
    if len(device) >= 16:
        conectedDevices.append(device)

def sendAllMessage(message, result=False):
    idx = 0
    for device in conectedDevices:
        sendMessage(device, message, result)
        print(device+"!!", idx)
        idx = idx + 1

if __name__ == "__main__" :
    sendAllMessage("shell input keyevent 26")

# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # Create two threads as follows
# # try:
# #    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
# #    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# # except:
# #    print ("Error: unable to start thread")
# def test(device) :
#     print(device)
#     print("!!")
# # threading.Thread(target=test).start()

# sendAllSync("shell input keyevent 26")
# sendAllSync("shell input keyevent 82")


# while 1:
#    pass

# import os
# from multiprocessing import Process

def doubler(number) :
    result = number * 2
    proc = os.getpid()
    print("{} doubled to {} by process id : {}".format(number, result, proc))

if __name__ == "__main__" :
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers) :
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs :
        proc.join()