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
        try :
            text = subprocess.check_output(cmd , shell=True)
            return text
        except :
            return "none"
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
        sendMessage(deviceId, "shell screencap -p /sdcard/screen.png")
        sendMessage(deviceId, "pull /sdcard/screen.png")
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
    # return int(value * scale)
    return int(value * 1/scale)

# device list
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
        device = device.replace(" ", "")
        device = device.replace("'", "")
        device = device.replace("\\tdevice", "")
        if len(device) >= 16:
            renewDevices.add(device)
    if len(checkDiff(conectedDevices, renewDevices)) > 0 or len(checkDiff(renewDevices, conectedDevices)) > 0 :
        conectedDevices = renewDevices
        selectedDevice = list(conectedDevices)[0]
        if __name__ == "__main" :
            updatelist()
    t = threading.Timer(3, checkDevices)
    t.daemon = True
    t.start()

checkDevices()

wmSize = sendMessage(selectedDevice, "shell wm size", True)
wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
wmSize = wmSize.replace("'", "")
wmSize = wmSize.replace("\\r", "")
rowWidth = int(wmSize.split("x")[0])
rowHeight = int(wmSize.split("x")[1])
w = int(rowWidth * scale)
h = int(rowHeight * scale)

# click event
def clickUnlock() :
    if __name__ == "__main__" :
        for device in conectedDevices :
            cmd = "shell dumpsys display {}".format(findString("mScreenState"))
            screenState = sendMessage(device, cmd, True)
            screenState = str(screenState).split("=")[1]
            screenState = screenState.replace("\\r", "")
            screenState = screenState.replace("\\n", "")
            screenState = screenState.replace("'", "")
            isOff = screenState!="ON"
            print(screenState, isOff)
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
        for device in conectedDevices :
            result = sendMessage(device, "shell pm list package -f {}".format(findString("com.imfine.galaxymediafacade")), True)
            if result == "none" :
                sendMessage(device, "-d install 0_app-release.apk")
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
        for device in conectedDevices :
            result = sendMessage(device, "shell pm list package -f {}".format(findString("skim.dev.kr.settingapplication")), True)
            if result == "none" :
                sendMessage(device, "-d install adb.apk")
        startActivity("skim.dev.kr.settingapplication/.MainActivity")

def clickShell() :
    if __name__ == "__main__" :
        shell = open("shell.txt", "r")
        shell = str(shell.read(),)
        for device in conectedDevices :
            if not shell.__contains__("//") :
                text = sendMessage(device, shell, True)
                print(text)

def clickDeleteCustom() :
    if __name__ == "__main__" :
        sendAllMessage("shell am force-stop skim.dev.kr.settingapplication")
        sendAllMessage("uninstall skim.dev.kr.settingapplication")


def clickDeleteGalaxy() :
    if __name__ == "__main__" :
        sendAllMessage("shell am force-stopcom.imfine.galaxymediafacade")
        sendAllMessage("com.imfine.galaxymediafacade")


# canvas event
def pressScrollUpKey():
    sendAllMessage("shell input touchscreen swipe 300 300 500 1000 100")

def pressScrollDownKey():
    sendAllMessage("shell input touchscreen swipe 300 1000 500 300 100")

def pressKey(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
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
    # else :
    #     sendAllMessage("shell input keyevent {}".format(keyValue))
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
    try:
        showShot()
        pil_img = Image.open(image_path).resize((w, h), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except:  # missing or corrupt image file
        img = None
    canvas.after(50, refresh_image, canvas, img, image_path, image_id)  

# tkinter init
root = tk.Tk()
root.title("Android Devices")
root.geometry("{}x{}".format(w+600, h))
root.resizable(True, True)
root.bind("<Key>", pressKey)
# root.bind('<Control-U>', pressScrollUpKey)
# root.bind('<Control-D>', pressScrollDownKey)

left = tk.Frame(root)
left.pack(side="left")

canvas= tk.Canvas(left, width=w, height=h)
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
    screenshot(picked)
    selectedIndex = picked
    print(picked)

center = tk.Frame(root)
center.pack(side="left")

# device list
menuFont = font.Font(size=26)
listbox = tk.Listbox(center, width=20, height=int(h), font=menuFont)
listbox.bind('<<ListboxSelect>>',selectItem)
for device in conectedDevices:
    listbox.insert(0, device)
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
    listbox.after(1000, updatelist)  

buttons = tk.Frame(root, width=5, padx=5)
buttons.pack()

def showShot():
    screenshot(selectedDevice)


clickUnlock()
# sendAllMessage("shell netcfg")
# os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
# os.system("adb shell rm -rf %s" % path)
# os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")

def addButton(buttonName, onClick) :
    button = tk.Button(buttons, height=1, width=80, text=buttonName, command=onClick, font=menuFont)
    button.pack()

addButton("unlock", clickUnlock)
addButton("custom", clickCustom)
addButton("galaxy", clickGalaxy)
addButton("quit alls", clickQuit)
addButton("home", clickHome)
addButton("file", clickFile)
addButton("settings", clickSetting)
addButton("activity", clickActivity)
addButton("Shell", clickShell)
addButton("delete galaxy", clickDeleteGalaxy)
addButton("delete custom", clickDeleteCustom)

if __name__ == "__main__" :
    image_path = 'screen.png'
    threading.Thread(target=refresh_image, args=(canvas, img, image_path, image_id,)).start()
    threading.Thread(target=updatelist).start()
    # Process(target=refresh_image, args=(canvas, img, image_path, image_id,)).start()

    root.mainloop()
