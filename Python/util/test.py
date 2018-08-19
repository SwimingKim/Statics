# from multiprocessing import Process, Lock

# def f(l, i):
#     l.acquire()
#     print('hello world', i)
#     l.release()

# # if __name__ == '__main__':
# lock = Lock()

# for num in range(10):
#     Process(target=f, args=(lock, num)).start()

# def nextImage():

#     global canvas
#     global item

#     canvas.delete(item)

#     im = Image.open("screen1.png")
#     photo = ImageTk.PhotoImage(im)
#     item = canvas.create_image(10,10,anchor=NW, image=photo)


import time
import shutil
import itertools
import os
import threading
import tkinter as tk
from tkinter import *
# import PIL
# import Image from pillow
from PIL import ImageTk, Image 

def update_image_file(dst):
    TEST_IMAGES = 'screen1.png', 'screen.png'
    # for src in itertools.cycle(TEST_IMAGES):
    #     shutil.copy(src, dst)
    #     time.sleep(.5)  # pause between updates

def refresh_image(canvas, img, image_path, image_id):
    # showShot()
    try:
        pil_img = Image.open(image_path).resize((800, 1000), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except IOError:  # missing or corrupt image file
        img = None
    # repeat every half sec
    canvas.after(50, refresh_image, canvas, img, image_path, image_id)  

image_path = 'screen.png'

# th = threading.Thread(target=update_image_file, args=(image_path,))
# th.daemon = True  # terminates whenever main thread does
# th.start()
# while not os.path.exists(image_path):  # let it run until image file exists
#     time.sleep(.1)


# tkinter init
root = tk.Tk()
root.title("Android Devices")
root.geometry("{}x{}".format(800, 1000))
root.resizable(True, True)

left = tk.Frame(root)
left.pack(side="left")

canvas= tk.Canvas(left, width=800, height=1000)
img = None  # initially only need a canvas image place-holder
image_id = canvas.create_image(0, 0, image=img, anchor='nw')
canvas.pack()
# canvas.focus_set()


threading.Thread(target=refresh_image, args=(canvas, img, image_path, image_id,)).start()
# refresh_image(canvas, img, image_path, image_id)
root.mainloop()