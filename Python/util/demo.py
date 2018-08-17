from PIL import Image, ImageTk
import tkinter as tk
import itertools
import os
import shutil
import threading
import time
import subprocess


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
    sendMessage(deviceId, "shell screencap -p /sdcard/screen.png")
    # sendMessage(deviceId, "shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png")
    sendMessage(deviceId, "pull /sdcard/screen.png")
    # sendMessage(deviceId, "pull /mnt/sdcard/screen.png")

def adbPath() :
    # return "C:\\Users\\imfine\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb"
    return "/Users/suyoung/Library/Android/sdk/platform-tools/adb"

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

   
def key(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
    # if keyValue == str(1):
    #     keyValue = 26
    # elif keyValue == "s":
    #     screenshot(conectedDevices[0])
    #     return
    for device in conectedDevices:
        sendMessage(device, "shell input keyevent {}".format(keyValue))
    print("pressed", keyValue)

def callback(event):
    global lastX
    global lastY
    lastX = event.x
    lastY = event.y
    for device in conectedDevices:
        sendMessage(device, "shell input tap {} {}".format(event.x * int(1/scale), event.y * int(1/scale)))
    print("clicked at", event.x, event.y)

def swife(event):
    global lastX
    global lastY
    if lastX == event.x and lastY == event.y:
        pass
    for device in conectedDevices:
        sendMessage(device, "shell input swipe {} {} {} {}".format(lastX * int(1/scale), lastY * int(1/scale), event.x * int(1/scale), event.y * int(1/scale)))
    print("swift", event.x, event.y)

def update_image_file(dst):
    """ Overwrite (or create) destination file by copying successive image 
        files to the destination path. Runs indefinitely. 
    """
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
    canvas.after(1000, refresh_image, canvas, img, image_path, image_id)  

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
root.geometry("{}x{}".format(w+200, h))

left = tk.Frame(root)
left.pack(side="left")

canvas= tk.Canvas(left, width=w, height=h)
canvas.bind("<Key>", key)
# screen.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<ButtonPress-1>", callback)
canvas.bind("<ButtonRelease-1>", swife)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack()
# canvas.focus_set()

right = tk.Frame(root)
right.pack(side="right")

def selectItem(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    screenshot(picked)
    selectedIndex = picked
    print(picked)

listbox = tk.Listbox(right, width=20, height=25)
listbox.bind('<<ListboxSelect>>',selectItem)
for device in conectedDevices:
    listbox.insert(0, device)
listbox.pack(side="top")

buttons = tk.Frame(right)
buttons.pack()

def clickPower():
    for device in conectedDevices:
        sendMessage(device, "shell input keyevent {}".format(26))
    print("power")

def clickHome():
    for device in conectedDevices:
        sendMessage(device, "shell input keyevent {}".format(3))
    print("home")

def clickFile():
    # key(3)
    print("file")


def showShot():
    screenshot(selectedDevice)


powerButton = tk.Button(buttons, text="power", anchor="nw", width=150, command=clickPower, pady=5)
powerButton.pack()

homeButton = tk.Button(buttons, width=150, text="home", command=clickHome)
homeButton.pack()

fileButton = tk.Button(buttons, width=150, text="file", command=clickFile)
fileButton.pack()

btn4 = tk.Button(buttons, width=150, text="1")
btn4.pack()

refresh_image(canvas, img, image_path, image_id)
root.mainloop()
