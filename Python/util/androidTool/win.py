#-*-coding:utf-8

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
import itertools
import os
import shutil
import time
import subprocess
import threading
from multiprocessing import Process, Lock
import platform
from pathlib import Path
import json
from pprint import pprint

# OS function
def isWindowOS() :
    return platform.system() == "Windows"

def resourcePath() :
    home = str(Path.home())
    if isWindowOS() :
        return home+"\\Desktop\\androidtool\\resources\\"
    else :
        return home+"/Desktop/androidtool/resources/"

def adbPath() :
    try :
        setting = open("{}setting.json".format(resourcePath()), "r").read()
        data = json.loads(setting)
        return data["adb"]
    except :
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
    if deviceId.__contains__(checkState) :
        return None
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        try :
            text = subprocess.check_output(cmd , shell=True)
            return text
        except :
            return None
    else :
        try :
            os.system(cmd)
            return "no text"
        except :
            pass

def sendSyncMessage(deviceId, message, result=False) :
    Process(target=sendMessage, args=(deviceId, message, result,)).start()

# adb function
conectedDevices = set()
selectedDevice = None
def screenshot(deviceId) :
    try : 
        imagePath = "/sdcard/screen.png"
        sendMessage(deviceId, "shell screencap -p {}".format(imagePath))
        sendMessage(deviceId, "pull {}".format(imagePath))
        # sendMessage(deviceId, "shell rm -rf {}".format(imagePath))
    except :
        pass

def sendAllMessage(message, result=False):
    for device in conectedDevices:
        Process(target=sendMessage, args=(device, message, result,)).start()

def startActivity(package):
    sendAllMessage("shell am start -a android.intent.action.MAIN -n {}".format(package))

# screen size
scale = 0.4
def scalePostion(value) :
    return int(value * 1/scale)

def getScreenSize() :
    if selectedDevice == None :
        return (432, 888)
    wmSize = sendMessage(selectedDevice, "shell wm size", True)
    wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
    wmSize = wmSize.replace("'", "")
    wmSize = wmSize.replace("\\r", "")
    rowWidth = int(wmSize.split("x")[0])
    rowHeight = int(wmSize.split("x")[1])
    w = int(rowWidth * scale)
    h = int(rowHeight * scale)
    return (w, h)

# device list
checkState = "*"
def checkDiff(set1, set2) :
    return [x for x in set1 if x not in set2]

def checkDevices():
    global listbox
    global conectedDevices
    global selectedDevice
    renewDevices = set()
    cmd = '{} devices'.format(adbPath())
    devices = subprocess.check_output(cmd, shell=True)
    devicelist = str(devices).split('\\n')
    del devicelist[0]
    for device in devicelist:
        device = device.replace("\\r", "")
        device = device.replace("\\tunauthorized", checkState)
        device = device.replace(" ", "")
        device = device.replace("'", "")
        device = device.replace("\\tdevice", "")
        if len(device) >= 16:
            renewDevices.add(device)
    if len(checkDiff(conectedDevices, renewDevices)) > 0 or len(checkDiff(renewDevices, conectedDevices)) > 0 :
        conectedDevices = renewDevices
        print(conectedDevices, "목록 갱신")
        for device in list(conectedDevices) :
            if not device.__contains__(checkState) :
                selectedDevice = device
                break
        if __name__ == "__main" :
            updatelist()
    t = threading.Timer(3, checkDevices)
    t.daemon = True
    t.start()

# click event
waitTime = 2
def clickUnlock() :
    if __name__ == "__main__" :
        for device in conectedDevices :
            cmd = "shell dumpsys display {}".format(findString("mScreenState"))
            screenState = sendMessage(device, cmd, True)
            if screenState == None :
                continue
            screenState = str(screenState).split("=")[1]
            screenState = screenState.replace("\\r", "")
            screenState = screenState.replace("\\n", "")
            screenState = screenState.replace("'", "")
            isOff = screenState!="ON"
            if isOff :
                sendMessage(device, "shell input keyevent {}".format(26))
                sendMessage(device, "shell input keyevent {}".format(82))
            else :
                sendMessage(device, "shell input keyevent {}".format(82))

def clickHome():
    if __name__ == "__main__" :
        sendAllMessage("shell input keyevent {}".format(3))

def clickFile():
    if __name__ == "__main__" :
        startActivity("com.sec.android.app.myfiles/.common.MainActivity")

def clickSetting():
    if __name__ == "__main__" :
        startActivity("com.android.settings/.Settings")

def clickBack():
    if __name__ == "__main__" :
        sendAllMessage("shell input keyevent 4")

def clickGalaxy():
    if __name__ == "__main__" :
        startActivity("com.imfine.galaxymediafacade/com.imfine.galaxymediafacade.MainActivity")

def closeActivity(device):
    if __name__ == "__main__" :
        value = sendMessage(device, "shell am stack list", True)
        packages = str(value).split(" ")
        for package in packages :
            if not(package.__contains__("/")):
                continue
            package = package.split("/")[0]
            if package.__contains__("{") :
                package = package.split("{")[1]
            sendMessage(device, "shell am force-stop {};".format(package))

def clickQuit():
    if __name__ == "__main__" :
        for device in conectedDevices:
            Process(target=closeActivity, args=(device,)).start()
    # sendAllMessage("shell input tap 150 1440")
    # time.sleep(2)
    # sendAllMessage("shell input tap 350 1350")

def clickActivity():
    if __name__ == "__main__" :
        sendAllMessage("shell am stack list")

def clickCustom():
    if __name__ == "__main__" :
        startActivity("skim.dev.kr.settingapplication/.MainActivity")

def clickShell() :
    if __name__ == "__main__" :
        shell = open("{}shell.txt".format(resourcePath()), "r")
        shell = str(shell.read(),)
        for device in conectedDevices :
            if not shell.__contains__("//") :
                text = sendMessage(device, shell, True)
                print(text)

def clickDeleteCustom() :
    if __name__ == "__main__" :
        # sendAllMessage("shell am force-stop skim.dev.kr.settingapplication")
        sendAllMessage("uninstall skim.dev.kr.settingapplication")

def clickDebug() :
    if __name__ == "__main__" :
        cmd = "{} kill-server".format(adbPath())
        os.system(cmd)
        cmd = "{} start-server".format(adbPath())
        os.system(cmd)

def clickBack() :
    if __name__ == "__main__" :
        sendAllMessage("shell input keyevent {}".format(4))
        # sendSyncMessage("shell input keyevent 4")

def clickUpdate() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 390 258")
        time.sleep(waitTime)
        pressScrollDownKey()
        time.sleep(waitTime)
        sendAllMessage("shell input tap 371 1230")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 580 426")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 580 590")

def clickEdge() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 329 426")
        time.sleep(waitTime)
        # pressScrollDownKey()
        sendAllMessage("shell input touchscreen swipe 300 800 500 550 100")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 400 1292")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 360 603")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 360 710")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 630 681")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 627 808")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 627 953")

def clickNavi() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 360 511")
        time.sleep(waitTime)
        sendAllMessage("shell input touchscreen swipe 300 800 500 550 100")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 340 1135")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 644 224")

def clickNoti() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 540 330")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 558 432")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 629 262")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 647 610")

def clickConnection() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 424 592")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 640 187")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 640 198")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 640 814")

def clickLocation() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 542 682")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 650 166")

def clickScan() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 560 595")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 497 215")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 370 1362")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 644 191")

def clickSound() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 542 860")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 542 194")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 542 361")
        time.sleep(waitTime)
        clickBack()
        time.sleep(waitTime)
        sendAllMessage("shell input tap 542 575")
        time.sleep(waitTime)
        sendAllMessage("shell input touchscreen swipe 263 220 82 220 100")
        time.sleep(waitTime)
        sendAllMessage("shell input touchscreen swipe 333 380 82 380 100")

def clickDisplay() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 590 230")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 877 370")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 960 575")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 585 1567")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 58 575")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 828 156")

def clickGoogle() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 388 1037")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 331 411")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 375 241")

def clickSwipe() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 403 1127")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 373 710")

def clickAutoTime() :
    if __name__ == "__main__" :
        time.sleep(1)
        sendAllMessage("shell input tap 300 946")
        time.sleep(waitTime)
        sendAllMessage("shell input tap 646 219")

def clickNote() :
    if __name__ == "__main__" :
        startActivity("com.samsung.android.app.spage/com.samsung.android.app.spage.main.MainActivity")

def clickInstallCustom() :
    if __name__ == "__main__" :
        sendAllMessage("-d install {}custom.apk".format(resourcePath()))

def clickInstallGalaxy() :
    if __name__ == "__main__" :
        sendAllMessage("-d install {}galaxy.apk".format(resourcePath()))

# canvas event
def pressScrollUpKey():
    sendAllMessage("shell input touchscreen swipe 300 400 500 800 100")

def pressScrollDownKey():
    sendAllMessage("shell input touchscreen swipe 300 800 500 400 100")

def pressKey(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "").lower()
    if keyValue == "u" :
        pressScrollUpKey()
    elif keyValue == "d" :
        pressScrollDownKey()
    elif keyValue == "h" :
        clickHome()
    elif keyValue == "f" :
        clickFile()
    elif keyValue == "s" :
        clickSetting()
    elif keyValue == "q" :
        clickQuit()
    elif keyValue == "c" :
        clickCustom()
    elif keyValue == "g" :
        clickGalaxy()
    elif keyValue == "b" :
        clickBack()
    elif keyValue == "l" :
        clickUnlock()
    print("pressed", keyValue)

# mouse event
clickTime = 0
clickSplit = 2
lastX = None
lastY = None

def mouseDown(event):
    global clickTime
    clickTime = 0
    global lastX
    global lastY
    lastX = event.x
    lastY = event.y

def mouseMove(event):
    global clickTime
    clickTime += 1
    global lastX
    global lastY
    sendAllMessage("shell input touchscreen swipe {} {} {} {} 100".format(scalePostion(lastX), scalePostion(lastY), scalePostion(event.x), scalePostion(event.y)))
    print("move", scalePostion(lastX), scalePostion(lastY), scalePostion(event.x), scalePostion(event.y))
    if clickTime / clickSplit == 0 :
        lastX = event.x
        lastY = event.y

def mouseUp(event):
    global clickTime
    if clickTime < clickSplit:
        sendAllMessage("shell input tap {} {}".format(scalePostion(event.x), scalePostion(event.y)))
        print("up", scalePostion(event.x), scalePostion(event.y))
    clickTime = 0

# image reload
def refresh_image(canvas, img, image_path, image_id):
    idx = 0
    try:
        if idx % 3 == 0 :
            showShot()
        global conectedDevices
        if selectedDevice != None :
            pil_img = Image.open(image_path).resize((w, h), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(pil_img)
            canvas.itemconfigure(image_id, image=img)
    except:  # missing or corrupt image file
        img = None
    t = threading.Timer(1, refresh_image, args=(canvas, img, image_path, image_id))
    t.start()
    idx += 1

# get device list
checkDevices()
clickUnlock()

# tkinter init
root = tk.Tk()
root.title("Android Devices")
(w, h) = getScreenSize()
root.geometry("{}x{}".format(w+800, h))
root.resizable(True, True)
root.bind("<Key>", pressKey)
# root.bind('<Control-U>', pressScrollUpKey)
# root.bind('<Control-D>', pressScrollDownKey)

left = tk.Frame(root)
left.pack(side="left")

canvas= tk.Canvas(left, width=w, height=h)
canvas.configure(background="black")
canvas.bind("<ButtonPress-1>", mouseDown)
canvas.bind("<B1-Motion>", mouseMove)
canvas.bind("<ButtonRelease-1>", mouseUp)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack()

def selectItem(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    selectedDevice = picked

center = tk.Frame(root)
center.pack(side="left")

# device list
menuFont = font.Font(size=18)
listbox = tk.Listbox(center, width=20, height=int(h), font=menuFont)
listbox.bind('<<ListboxSelect>>',selectItem)
listbox.pack()

def updatelist() :
    global listbox
    global isChangeList
    listValue = set(listbox.get(0, tk.END))
    addItems = checkDiff(conectedDevices, listValue)
    removeItems = checkDiff(listValue, conectedDevices)
    if len(addItems) > 0 or len(removeItems) > 0 :
        listbox.delete(0, tk.END)
        for item in conectedDevices :
            listbox.insert(0, item)
            if item.__contains__(checkState) :
                listbox.itemconfig(0, {"fg": "#f0f0f0", "bg": "#eb9f9f"})
    threading.Timer(1, updatelist).start()

buttons = tk.Frame(root, width=5, padx=5)
buttons.pack(side="left")

def showShot():
    screenshot(selectedDevice)

# os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
# os.system("adb shell rm -rf %s" % path)
# os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")

def addButton(obj, buttonName, onClick) :
    button = tk.Button(obj, height=1, width=20, text=buttonName, command=onClick, font=menuFont)
    button.pack()

addButton(buttons, "usb debugging", clickDebug)
addButton(buttons, "(l) unlock", clickUnlock)
addButton(buttons, "(g) galaxy", clickGalaxy)
addButton(buttons, "(c) custom", clickCustom)
addButton(buttons, "(q) quit alls", clickQuit)
addButton(buttons, "(h) home", clickHome)
addButton(buttons, "(f) file", clickFile)
addButton(buttons, "(s) settings", clickSetting)
addButton(buttons, "(u) scrollUp", pressScrollUpKey)
addButton(buttons, "(d) scrollDown", pressScrollDownKey)
addButton(buttons, "(b) back", clickBack)
addButton(buttons, "activity", clickActivity)
addButton(buttons, "Shell", clickShell)
addButton(buttons, "delete custom", clickDeleteCustom)
# addButton(buttons, "note", clickNote)

customs = tk.Frame(root, width=5, padx=5)
customs.pack(side="left")

addButton(customs, "install custom", clickInstallCustom)
addButton(customs, "display", clickDisplay)
addButton(customs, "update", clickUpdate)
addButton(customs, "notification", clickNoti)
addButton(customs, "time & edge", clickEdge)
addButton(customs, "navi", clickNavi)
addButton(customs, "connection", clickConnection)
addButton(customs, "location", clickLocation)
addButton(customs, "scanning", clickScan)
addButton(customs, "sound", clickSound)
addButton(customs, "auto time", clickAutoTime)
addButton(customs, "ok google", clickGoogle)
addButton(customs, "swipe", clickSwipe)
addButton(customs, "install galaxy", clickInstallGalaxy)

if __name__ == "__main__" :
    image_path = 'screen.png'
    t = threading.Thread(target=refresh_image, args=(canvas, img, image_path, image_id,))
    t.daemon = True
    t.start()
    threading.Thread(target=updatelist).start()
    root.mainloop()
