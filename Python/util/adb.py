import datetime
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os

def touch(x, y) :
    os.system("adb shell input tap %s %s" % (x, y))

def touchBack() :
    os.system("adb shell input keyevent 4")

def sleep(time=1) :
    os.system("sleep %s" % time);

# device = MonkeyRunner.waitForConnection()
# MonkeyRunner.sleep(1)

os.system("adb shell am start -a android.intent.action.MAIN -n skim.dev.kr.settingapplication/skim.dev.kr.settingapplication.MainActivity;")

touch(407, 910)
sleep();
touch(535, 131)
sleep();
touch(394, 701)
sleep();
touch(554, 999)
sleep();
touch(396, 625)
sleep();
touch(810, 1105)
sleep();
touchBack()

# MonkeyRunner.sleep(1)
# device.press(102, 'DOWN_AND_UP');
