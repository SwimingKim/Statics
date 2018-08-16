import subprocess
import os
from tkinter import *
from PIL import Image
from PIL import ImageTk

scale = 0.5

def sendMessage(deviceId, message, result=False):
    cmd = "%s -s %s %s" % (adbPath(), deviceId, message)
    if result :
        text = subprocess.check_output(cmd , shell=True)
        return text
    else :
        os.system(cmd)
        return "no text"

def screenshot() :
    sendMessage(conectedDevices[0], "shell screencap -p /sdcard/screen.jpg")
    sendMessage(conectedDevices[0], "pull /sdcard/screen.jpg")

def adbPath() :
    return "/Users/suyoung/Library/Android/sdk/platform-tools/adb"

cmd = '{} devices'.format(adbPath())
devices = subprocess.check_output(cmd, shell=True)
conectedDevices = list()

devicelist = str(devices).split('\\n')
for device in devicelist:
    if len(device) != 28:
        continue
    device = device.replace("\\tdevice", "")
    conectedDevices.append(device)

wmSize = sendMessage(conectedDevices[0], "shell wm size", True)
wmSize = list(str(wmSize).split("\\nOverride size: "))[-1].replace("\\n", "")
wmSize = wmSize.replace("'", "")
w = int(int(wmSize.split("x")[0]) * scale)
h = int(int(wmSize.split("x")[1]) * scale)
wmSize = str(w)+"x"+str(h)

# # for device in conectedDevices:
# #     sendMessage(device, "shell input keyevent 26")
#     # sendMessage(device, "input keyevent 3")
#     # sendMessage(device, "input swipe 100 500 100 1450 100")
#     # sendMessage(device, "wm size", True)
#     # sendMessage(device, "screencap -p /sdcard/screen.png")
#     # sendMessage(device, "rm /sdcard/screen.png")
#     # sendMessage(device, "rm /sdcard/sc.png")

    
def key(event):
    value = repr(event.char)
    keyValue = str(value).replace("'", "")
    if keyValue == str(1):
        keyValue = 26
    elif keyValue == "s":
        screenshot()
        changeImage()
        return
    for device in conectedDevices:
        sendMessage(device, "shell input keyevent {}".format(keyValue))
    print("pressed", keyValue)

def callback(event):
    for device in conectedDevices:
        sendMessage(device, "shell input tap {} {}".format(event.x * int(1/scale), event.y * int(1/scale)))
    print("clicked at", event.x, event.y)



def init() :
    root = Tk()
    root.title("Android Devices")
    root.geometry(wmSize)

    canvas= Canvas(root, width=w, height=h)
    canvas.bind("<Key>", key)
    canvas.bind("<Button-1>", callback)
    settingCanvas(canvas)

    screenshot()
    image = Image.open("screen.jpg")
    image = image.resize((w, h), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(image)
    bgImgae = canvas.create_image(0, 0, image=bg, anchor='nw')

    canvas.focus_set()
    canvas.pack()
    root.mainloop()

def changeImage() :
    canvas = Canvas(getCanvae())
    # canvas.delete(bgImgae)
    # canvas.delete('all')
    img = Image.open("screen.jpg")
    img = img.resize((w, h), Image.ANTIALIAS)
    bgImg = ImageTk.PhotoImage(img)
    bgImgae = canvas.create_image(0, 0, image=bgImg, anchor='nw')
    # canvas.itemconfig(bgImgae, image =bgImg)
    # canvas.update()
    # canvas.pack()
    

# screenshot()
# changeImage()

# image = Image.open("screen.jpg")
# bg = ImageTk.PhotoImage(image)
# label = Label(root, image=bg)
# label.image = bg 

def Image2():
    canvas.delete("all")
    # # image1 = PhotoImage(file = "image2.png")
    # # canvas.create_image(0,0,anchor='nw',image=image1)
    # canvas.image = image1


# stopbutton = Button(root, text='Stop',width=5,fg="red",command = Image2)
# stopbutton.pack(side = RIGHT)

def settingCanvas(canvas) :
    can = canvas

def getCanvae() :
    return can

init()