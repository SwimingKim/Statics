from PIL import Image, ImageTk
import tkinter as tk
import itertools
import os
import shutil
import time
import subprocess
import threading
from multiprocessing import Process, Lock
import platform
from pathlib import Path

# OS function
def isWindowOS() :
    return platform.system() == "Windows"

def adbPath() :
    home = str(Path.home())
    if isWindowOS() :
        return home+"\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb"
    else :
        return home+"/Library/Android/sdk/platform-tools/adb"

def findString(value) :
    if isWindowOS() :
        return "| findstr {}".format(value)
    else :
        return "| grep '{}'".format(value)

# bash function
def sendMessage(deviceId, message, result=False):
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        text = subprocess.check_output(cmd , shell=True)
        return text
    else :
        os.system(cmd)
        return "no text"

# adb function
conectedDevices = list()
def screenshot(deviceId) :
    sendMessage(deviceId, "shell screencap -p /sdcard/screen.png")
    sendMessage(deviceId, "pull /sdcard/screen.png")

def sendAllMessage(message, result=False):
    for device in conectedDevices:
        Process(target=sendMessage, args=(device, message, result,)).start()

def startActivity(package):
    sendAllMessage("shell am start -a android.intent.action.MAIN -n {}".format(package))


# screen size
scale = 0.35
def scalePostion(value) :
    return value * (1/scale)

cmd = '{} devices'.format(adbPath())
devices = subprocess.check_output(cmd, shell=True)

devicelist = str(devices).split('\\n')
del devicelist[0]
for device in devicelist:
    device = device.replace("\\r", "")
    device = device.replace(" ", "")
    device = device.replace("'", "")
    device = device.replace("\\tdevice", "")
    if len(device) >= 16:
        conectedDevices.append(device)
selectedDevice = conectedDevices[0]

wmSize = sendMessage(conectedDevices[0], "shell wm size", True)
wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
wmSize = wmSize.replace("'", "")
wmSize = wmSize.replace("\\r", "")
w = int(int(wmSize.split("x")[0]) * scale)
h = int(int(wmSize.split("x")[1]) * scale)

# canvas event
def pressKey(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
    print(keyValue)
    # sendAllMessage("shell input keyevent {}".format(keyValue))
    # print("pressed", keyValue)

# mouse event
clickTime = 0
lastX = 0
lastY = 0

def mouseDown(event):
    global clickTime
    clickTime = 0
    global lastX
    global lastY
    lastX = scalePostion(event.x)
    lastY = scalePostion(event.y)

def mouseMove(event):
    global clickTime
    clickTime += 1
    print(clickTime)
    global lastX
    global lastY
    print(lastX, lastY)
    print(event.x, event.y)
    sendAllMessage("shell input touchscreen swipe {} {} {} {} 100".format(scalePostion(lastX), scalePostion(lastY), scalePostion(event.x), scalePostion(event.y)))
    lastX = scalePostion(event.x)
    lastY = scalePostion(event.y)
    print("move", lastX, lastY)

def mouseUp(event):
    global clickTime
    if clickTime < 5:
        sendAllMessage("shell input tap {} {}".format(scalePostion(event.x), scalePostion(event.y)))
        print("swift", event.x, event.y)
    clickTime = 0

# image reload
def update_image_file(dst):
    TEST_IMAGES = 'screen.png', 'screen.png'
    for src in itertools.cycle(TEST_IMAGES):
        shutil.copy(src, dst)
        time.sleep(.5)  # pause between updates

def refresh_image(canvas, img, image_path, image_id):
    showShot()
    try:
        pil_img = Image.open(image_path).resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except IOError:  # missing or corrupt image file
        img = None
    # repeat every half sec
    canvas.after(50, refresh_image, canvas, img, image_path, image_id)  

image_path = 'test.png'

th = threading.Thread(target=update_image_file, args=(image_path,))
th.daemon = True  # terminates whenever main thread does
th.start()
while not os.path.exists(image_path):  # let it run until image file exists
    time.sleep(.1)

# tkinter init
root = tk.Tk()
root.title("Android Devices")
root.geometry("{}x{}".format(w+400, h))
root.resizable(False, False)

canvas= tk.Canvas(root)
canvas.bind("<Key>", pressKey)
canvas.bind("<ButtonPress-1>", mouseDown)
canvas.bind("<B1-Motion>", mouseMove)
canvas.bind("<ButtonRelease-1>", mouseUp)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack()
canvas.focus_set()

def selectItem(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    screenshot(picked)
    selectedIndex = picked
    print(picked)

# device list
listbox = tk.Listbox(canvas, width=20, height=int(h))
listbox.bind('<<ListboxSelect>>',selectItem)
for device in conectedDevices:
    listbox.insert(0, device)
listbox.pack(side="left")

# button click event
buttons = tk.Frame(canvas, width=5, padx=5)
buttons.pack(side="right")

def clickUnlock():
    for device in conectedDevices :
        cmd = "shell dumpsys display {}".format(findString("mScreenState"))
        screenState = sendMessage(device, cmd, True)
        screenState = str(screenState).split("=")[1]
        screenState = str(screenState).replace("\\n", "")
        screenState = str(screenState).replace("'", "")
        isOff = screenState!="ON"
        if isOff :
            sendMessage(device, "shell input keyevent {}".format(26))
    sendAllMessage("shell input keyevent {}".format(82))

def clickHome():
    sendAllMessage("shell input keyevent {}".format(3))

def clickFile():
    startActivity("com.sec.android.app.myfiles/.common.MainActivity")

def clickSetting():
    startActivity("com.android.settings/.Settings")

def clickBack():
    sendAllMessage("shell input keyevent 4")

def clickGalaxy():
    startActivity("com.imfine.galaxymediafacade/com.imfine.galaxymediafacade.MainActivity")

def clickApk():
    sendAllMessage("-d install -r 0_app-release.apk")

def clickWifi():
    startActivity("com.android.settings/.wifi.WifiSettings")

def closeActivity(device):
    startActivity("com.android.systemui/com.android.systemui.recents.RecentsActivity")
    # value = sendMessage(device, "shell am stack list", True)
    # packages = str(value).split(" ")
    # for package in packages :
    #     if not(package.__contains__("/")):
    #         continue
    #     package = package.split("/")[0]
    #     if package.__contains__("{") :
    #         package = package.split("{")[1]
    #     sendMessage(device, "shell am force-stop {};".format(package))
    # clickHome()

def clickClose():
    for device in conectedDevices:
        Process(target=closeActivity, args=(device,)).start()
    # sendAllMessage("shell input tap 150 1440")
    # time.sleep(2)
    # sendAllMessage("shell input tap 350 1350")

def clickActivity():
    # adb dumpsys activity
    sendAllMessage("shell am stack list")

def clickADB():
    startActivity("skim.dev.kr.settingapplication/.MainActivity")

def clickUp():
    sendAllMessage("shell input keyevent 20")

def clickDown():
    sendAllMessage("shell input keyevent 19")

def showShot():
    screenshot(selectedDevice)

clickUnlock()
# sendAllMessage("shell netcfg")
# os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
# os.system("adb shell rm -rf %s" % path)
# os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")

unlockButton = tk.Button(buttons, text="unlock", width=80, command=clickUnlock, pady=5)
unlockButton.pack()

homeButton = tk.Button(buttons, width=80, text="home", command=clickHome)
homeButton.pack()

fileButton = tk.Button(buttons, width=80, text="file", command=clickFile)
fileButton.pack()

settingButton = tk.Button(buttons, width=80, text="setting", command=clickSetting)
settingButton.pack()

backButton = tk.Button(buttons, width=80, text="back", command=clickBack)
backButton.pack()

glaxyButton = tk.Button(buttons, width=80, text="galaxy", command=clickGalaxy)
glaxyButton.pack()

apkButton = tk.Button(buttons, width=80, text="apk install", command=clickApk)
apkButton.pack()

wifiButton = tk.Button(buttons, width=80, text="wifi", command=clickWifi)
wifiButton.pack()

closeButton = tk.Button(buttons, width=80, text="close all", command=clickClose)
closeButton.pack()

activityButton = tk.Button(buttons, width=80, text="activity", command=clickActivity)
activityButton.pack()

adbButton = tk.Button(buttons, width=80, text="adb", command=clickADB)
adbButton.pack()

upButton = tk.Button(buttons, width=80, text="Up", command=clickUp)
upButton.pack()

downButton = tk.Button(buttons, width=80, text="Down", command=clickDown)
downButton.pack()

threading.Thread(target=refresh_image, args=(canvas, img, image_path, image_id,)).start()
# refresh_image(canvas, img, image_path, image_id)
root.mainloop()