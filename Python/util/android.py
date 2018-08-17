import subprocess
import os
from tkinter import *
import os

def sendMessage(deviceId, message, result=False):
    if result :
        text = subprocess.check_output("adb -s %s %s" % (deviceId, message) , shell=True)
        return text
    else :
        os.system("adb -s %s %s" % (deviceId, message))
        return "no text"

def screenshot() :
    sendMessage(conectedDevices[0], "shell screencap -p /sdcard/screen.png")
    sendMessage(conectedDevices[0], "pull /sdcard/screen.png")

devices = subprocess.check_output('adb devices', shell=True)
conectedDevices = list()

devicelist = str(devices).split('\\r\\n')
del devicelist[0]
for device in devicelist:
    device = device.replace(" ", "")
    device = device.replace("'", "")
    device = device.replace("\\tdevice", "")
    if len(device) >= 16:
        conectedDevices.append(device)

print(conectedDevices)
wmSize = sendMessage(conectedDevices[0], "shell wm size", True)
wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
wmSize = wmSize.replace("'", "")
wmSize = wmSize.replace("\\r", "")
w = wmSize.split("x")[0]
h = wmSize.split("x")[1]

screenshot()

# for device in conectedDevices:
#     sendMessage(device, "shell input keyevent 26")
    # sendMessage(device, "input keyevent 3")
    # sendMessage(device, "input swipe 100 500 100 1450 100")
    # sendMessage(device, "wm size", True)
    # sendMessage(device, "screencap -p /sdcard/screen.png")
    # sendMessage(device, "rm /sdcard/screen.png")
    # sendMessage(device, "rm /sdcard/sc.png")

root = Tk()
root.title("Android Devices")
root.geometry(wmSize)
bg = PhotoImage(file = "screen.png")
# wall_label = Label(image = wall)
# wall_label.place(x = -2,y = -2)

canvas= Canvas(root, width=w, height=h)
    
def key(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
    if keyValue == str(1):
        keyValue = 26
    if keyValue == "s":
        screenshot()
        global canvas
        global bgImg
        bg = PhotoImage(file = "screen.png")
        canvas.itemconfig(bgImg, image=bg)
        canvas.update_idletasks()
    for device in conectedDevices:
        sendMessage(device, "shell input keyevent {}".format(keyValue))
    print("pressed", keyValue)

def callback(event):
    for device in conectedDevices:
        sendMessage(device, "shell input tap {} {}".format(event.x, event.y))
    print("clicked at", event.x, event.y)

# root = Tk()
# root.title("Android Devices")
# root.geometry(wmSize)
# bg = PhotoImage(file = "screen.png")
# wall_label = Label(image = wall)
# wall_label.place(x = -2,y = -2)

# canvas= Canvas(root, width=w, height=h)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
bgImg = canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.focus_set()
canvas.pack()

root.mainloop()


