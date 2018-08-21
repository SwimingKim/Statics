# -*- coding: utf-8 -*-
import sys
import subprocess

try:
    zipName = sys.argv[1]
    hashName = zipName.replace(".zip", ".hash")

    subprocess.call("/usr/local/share/john/zip2john '%s' > '%s'"%(zipName, hashName), shell=True)
    subprocess.call("john --incremental=digits '%s'"%hashName, shell=True)
   
    password = subprocess.check_output("john --show '%s'" % hashName, shell=True)
    subprocess.call("rm -rf DAY\ 5\ 수업음성\ \(난이도\ 최강\).hash", shell=True)
    password = str(password).split(":")[1]

    newName = zipName.replace(".zip", "_"+password+".zip")
    subprocess.call("mv '%s' '%s'"%(zipName, newName), shell=True)
except Exception:
    print("에러 발생")
