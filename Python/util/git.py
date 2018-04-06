# -*- coding: utf-8 -*-
import os
import sys

strRepositoryName = sys.argv[1].replace("/", "")
strCommand = sys.argv[2]

strPath = os.getcwd() + "/" + strRepositoryName
strGitPath = strPath+"/.git"

def check() :
    IsMoreThan100MB = False

    for root, dirs, files in os.walk(strPath+'/'):
        if (root.find(".git") != -1) :
            continue
        for fname in files:
            full_fname = os.path.join(root, fname)
            size = os.path.getsize(full_fname)
            if (size >= 104857600) :
                print(full_fname)
                IsMoreThan100MB = True

    if (IsMoreThan100MB) :
        print("directory has some files more than 100MB")
        sys.exit()

def sendMaster() :
    os.system(getMyCmd("add ."))
    os.system(getMyCmd("commit"))
    os.system(getMyCmd("push"))
    print("finish push")

def showStatus() :
    os.system(getMyCmd("status"))

def showLog() :
    os.system(getMyCmd("log"))

def getMyCmd(strCmd) :
    return "git --git-dir=%s --work-tree=%s %s;"%(strGitPath, strPath, strCmd)

def runCommand(strCommand) :
    if strCommand == "send" :
        check()
        sendMaster()
    elif strCommand == "status" :
        showStatus()
    elif strCommand == "log" :
        showLog()

runCommand(strCommand)
