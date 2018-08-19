from PIL import Image, ImageTk
import tkinter as tk
import itertools
import os
import shutil
import time
import subprocess
import threading
from multiprocessing import Process, Lock

def sendMessage(deviceId, message, result=False):
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        text = subprocess.check_output(cmd , shell=True)
        return text
    else :
        os.system(cmd)
        return "no text"

def screenshot(deviceId) :
    # adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png
    # threading.Thread(target=sendMessage, args=(deviceId, "shell screencap -p /sdcard/screen.png",)).start()
    # threading.Thread(target=sendMessage, args=(deviceId, "pull /sdcard/screen.png",)).start()
    sendMessage(deviceId, "shell screencap -p /sdcard/screen.png")
    # sendMessage(deviceId, "shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png")
    sendMessage(deviceId, "pull /sdcard/screen.png")
    # sendMessage(deviceId, "pull /mnt/sdcard/screen.png")

def addRootPath() :
    # return "C:\\Users\\imfine\\AppData\\Local\\Android\\Sdk\\platform-tools\\"
    return "/Users/suyoung/Library/Android/sdk/platform-tools/"

def adbPath() :
    return addRootPath()+"adb"

def sqlitePath() :
    return addRootPath()+"sqlite3"

lastX = 0
lastY = 0
scale = 0.25

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
selectedDevice = conectedDevices[0]

wmSize = sendMessage(conectedDevices[0], "shell wm size", True)
wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
wmSize = wmSize.replace("'", "")
wmSize = wmSize.replace("\\r", "")
w = int(int(wmSize.split("x")[0]) * scale)
h = int(int(wmSize.split("x")[1]) * scale)
# wmSize = str(w)+"x"+str(h)
# print(wmSize)

def sendAllMessage(message, result=False):
    for device in conectedDevices:
        Process(target=sendMessage, args=(device, message, result,)).start()

def startActivity(package):
    sendAllMessage("shell am start -a android.intent.action.MAIN -n {}".format(package))
   
def key(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
    sendAllMessage("shell input keyevent {}".format(keyValue))
    print("pressed", keyValue)


clickTime = 0
def callback(event):
    global lastX
    global lastY
    lastX = event.x
    lastY = event.y
    sendAllMessage("shell input tap {} {}".format(event.x * int(1/scale), event.y * int(1/scale)))

clickTime
def move(event):
    global clickTime
    clickTime += 1
    print(clickTime)
    if clickTime > 3 :
        global lastX
        global lastY
        if lastX == event.x and lastY == event.y:
            pass
        dx = lastX - event.x
        dy = lastY - event.y
        sendAllMessage("shell input trackball roll {} {}".format(dx, dy))
        # sendAllMessage("shell input swipe {} {} {} {}".format(lastX * int(1/scale), lastY * int(1/scale), event.x * int(1/scale), event.y * int(1/scale)))
        print("swift", event.x, event.y)

def swife(event):
    global clickTime
    global lastX
    global lastY
    if lastX == event.x and lastY == event.y:
        pass
    dx = lastX - event.x
    dy = lastY - event.y
    sendAllMessage("shell input trackball roll {} {}".format(dx, dy))
    # sendAllMessage("shell input swipe {} {} {} {} {}".format(lastX * int(1/scale), lastY * int(1/scale), event.x * int(1/scale), event.y * int(1/scale), clickTime))
    clickTime = 0
    print("swift", event.x, event.y)

def update_image_file(dst):
    TEST_IMAGES = 'screen.png', 'screen.png'
    for src in itertools.cycle(TEST_IMAGES):
        shutil.copy(src, dst)
        time.sleep(.5)  # pause between updates
#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------
# More code to simulate background process periodically updating the image file.
th = threading.Thread(target=update_image_file, args=(image_path,))
th.daemon = True  # terminates whenever main thread does
th.start()
while not os.path.exists(image_path):  # let it run until image file exists
    time.sleep(.1)
#------------------------------------------------------------------------------

root = tk.Tk()
root.title("Android Devices")
root.geometry("{}x{}".format(w+400, h))
root.resizable(False, False)

left = tk.Frame(root)
left.pack(side="left")

canvas= tk.Canvas(left, width=w, height=h)
canvas.bind("<Key>", key)
canvas.bind("<ButtonPress-1>", callback)
# screen.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<B1-Motion>", move)
canvas.bind("<ButtonRelease-1>", swife)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack()
# canvas.focus_set()

center = tk.Frame(root)
center.pack(side="left")

def selectItem(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    screenshot(picked)
    selectedIndex = picked
    print(picked)

listbox = tk.Listbox(center, width=20, height=int(h))
listbox.bind('<<ListboxSelect>>',selectItem)
for device in conectedDevices:
    listbox.insert(0, device)
listbox.pack()


buttons = tk.Frame(root, width=5, padx=5)
buttons.pack()

def clickUnlock():
    for device in conectedDevices :
        screenState = sendMessage(device, "shell dumpsys display | grep 'mScreenState'", True)
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

def clickDisplay():
    startActivity("com.samsung.android.app.spage/com.samsung.android.app.spage.main.MainActivity")

def clickActivity():
    # adb dumpsys activity
    sendAllMessage("shell am stack list")

def clickADB():
    startActivity("skim.dev.kr.settingapplication/.MainActivity")

def clickUp():
    sendAllMessage("shell input keyevent 20")
    print("up")

def clickDown():
    sendAllMessage("shell input keyevent 19")
    print("down")

def clickEdge():
    startActivity("com.samsung.android.app.cocktailbarservice/com.samsung.android.app.cocktailbarservice.settings.EdgePanels")
    print("edge")

def showShot():
    screenshot(selectedDevice)

clickUnlock()
# adb pull /data/misc/wifi/wpa_supplicant.conf
# sendAllMessage("shell netcfg")
# adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings
# adb shell input keyevent 20 & adb shell input keyevent 23
# os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
# os.system("adb shell rm -rf %s" % path)
# os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")

# sendAllMessage("uninstall com.imfine.galaxymediafacade/com.imfine.galaxymediafacade.MainActivity")
# sendAllMessage("shell dumpsys display | grep 'mScreenState'", True)
# sendAllMessage("shell input keyevent 66")
# sendAllMessage("-d install -r 0_app-release.apk")

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