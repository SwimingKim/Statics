import sys
import os
import shutil
from tkinter import *
import tkinter.messagebox

def build( strContent ) :
    strFullPath = getPath( strContent )
    folder = os.getcwd()+'\\history\\'
    if not os.path.isdir( folder ):
        os.mkdir( folder )
    jsfl = os.getcwd()+'\\history\\'+strContent+'.jsfl'
    shutil.copy( os.getcwd()+'\\build.jsfl', jsfl )
    os.system('"C:\Program Files\Adobe\Adobe Animate CC 2018\Animate.exe" %s' % jsfl)
    print( strContent +" build")

def publish( strContent ) :
    strFullPath = getPath( strContent )
    if strFullPath == "" :
        return
    try:
        shutil.rmtree(os.getcwd()+'\\publish\\'+strContent)
    except FileNotFoundError:
        pass
    dirname = os.getcwd()+'\\publish\\'+strContent;
    shutil.copytree(strFullPath, dirname)
    contents = os.listdir(dirname)
    for content in contents:
        foldername = os.path.join(dirname, content)
        if os.path.isdir( foldername ) and content.find( strContent ) != -1 :
            folder = os.listdir( foldername )
            for f in folder :
                if f.find(".fla") != -1 or f.find("contents.html") != -1 :
                    os.remove( foldername + '\\' + f )
    print( strContent +" pubish")

def getPath( strContent ) :
    strPath = ""
    if strContent.find("NKKJ1") == 0:
        strPath = "1학년"
    elif strContent.find("NKKJ2") == 0:
        strPath = "2학년"
    else :
        tkinter.messagebox.showwarning("오류발생", "차시명을 잘못 입력했습니다")
        txt.delete(0, END)
        txt.insert(0, "")
        return ""

    strFullPath = os.getcwd().replace("006_tool", "")+'\\003_html\\'+strPath+'\\'+strContent+'\\'
    print(strFullPath)
    if not os.path.isdir( strFullPath ) :
        tkinter.messagebox.showwarning("오류발생", "컨텐츠가 존재하지 않습니다")
        return ""
    return strFullPath

def clickBuild() :
    build( txt.get() )
    txt.delete(0, END)
    print("build")

def clickPublish() :
    publish( txt.get() )
    txt.delete(0, END)
    print("publish")

def clickClearBuild() :
    try:
        shutil.rmtree( os.getcwd() + '\\history' )
    except PermissionError:
        tkinter.messagebox.showwarning('오류 발생', '현재 제작중인 파일이 있어 삭제할 수 없습니다')
        pass
    except FileNotFoundError:
        pass
    print('제작 기록 삭제')

def clickClearPublish() :
    try:
        shutil.rmtree( os.getcwd() + '\\publish' )
    except FileNotFoundError:
        pass
    print('납품용 파일 삭제')


root = Tk()
root.title("Html5 자동화")
root.geometry("250x100")
# root.geometry("250x400")

top = Frame(root)
top.pack(pady=5)

lbl = Label(top, text="차시", width=8)
lbl.pack(side="left")

txt = Entry(top)
txt.pack(side="right")
txt.focus_force()

btn1 = Frame(root)
btn1.pack(pady=5)

btnBuild = Button(btn1, text="제작", width=15, command=clickBuild)
btnBuild.pack(padx=5, side="left")

btnPublish = Button(btn1, text="납품용 파일", width=15, command=clickPublish)
btnPublish.pack(padx=5, side="right")

# labelframe = LabelFrame(root, height=18, text="message", relief="groove")
# labelframe.pack(fill="both", expand="yes")

# msg = Label(labelframe, text="자동화 프로그램")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.configure(text=msg.cget("text")+"\n!\n!\n!")
# msg.pack(padx=5, pady=5, anchor=NW)

btn2 = Frame(root)
btn2.pack(pady=5)

btnClearBuild = Button(btn2, text="제작 기록 삭제", width=15, command=clickClearBuild)
btnClearBuild.pack(padx=5, side="left")

btnClearPublish = Button(btn2, text="납품용 파일 삭제", width=15, command=clickClearPublish)
btnClearPublish.pack(padx=5, side="right")

root.mainloop()
