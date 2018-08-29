import os


copyPath = os.getcwd() + "/dddd/"
pastePaht = "//sdcard//Downloads"
print(copyPath)
os.system("adb push %s %s" % ( copyPath, pastePaht ))