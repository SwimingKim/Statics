#-*-coding:utf-8
import os;
import sys;
import shutil;
from pywinauto.application import Application;

strContents = sys.argv[1];
strMode = sys.argv[2];

strPath = os.getcwd() + '\\'
if strContents.find("KKJ") == 0:
    strPath += "001_korean"
elif strContents.find("SSJ") == 0:
    strPath += "002_social"

def searchModule(dirname, list):
    contents = os.listdir(dirname)
    for content in contents:
        filename = os.path.join(dirname, content)
        if os.path.isdir(filename) :
            folder = filename.split('\\')[-1]
            if folder != "images" and folder != "sounds" and folder != "common":
                searchModule(filename, list)
        elif filename.split('\\')[-2].find('scripts') != -1 :
            f = filename.split('\\')[-1]
            if f in list :
                print(filename)
                shutil.copy( os.getcwd() + '\\005_module\\' + f, filename );


def searchCommon(dirname):
    contents = os.listdir(dirname)
    for content in contents:
        filename = os.path.join(dirname, content)
        if os.path.isdir(filename) :
            folder = filename.split('\\')[-1]
            if folder != "images" and folder != "sounds" :
                searchCommon(filename)
        else :
            if filename.find('.fla') != -1 or filename.find('contents.html') != -1 :
                os.remove(filename)

def publish() :
    copyPath = strPath+'\\003_contents\\'+strContents;
    pastePath = strPath+'\\003_contents\\publish\\'+strContents;
    try:
        shutil.rmtree(pastePath)
    except FileNotFoundError:
        pass
    shutil.copytree(copyPath, pastePath);
    searchCommon(pastePath)

    print("복사 완료")


def copyCommon() :
    allCommon = os.getcwd()+'\\003_common'
    contentCommon = strPath+'\\003_contents\\'+strContents+'\\common';
    try:
        shutil.rmtree(contentCommon)
    except FileNotFoundError:
        pass
    shutil.copytree(allCommon, contentCommon)
    print("common update 완료")


def copyModule() :
    modulePath = os.getcwd() + '\\005_module'
    copyPath = strPath + '\\003_contents\\' + strContents + '\\'
    file_list = os.listdir( modulePath )
    searchModule( copyPath, file_list )
    print("module copy 완료")


def push() :
    copyPath = strPath + '\\003_contents\\' + strContents + '\\'
    pastePath = "//sdcard//CJHP_TEST//"+strContents
    os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
    os.system("adb shell rm -rf %s" % pastePath)
    os.system("adb push %s %s" % ( copyPath, pastePath ))
    os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")
    print("adb push")

def build() :
    # app = Application().start("C:\Program Files\Adobe\Adobe Animate CC 2018\Animate.exe")
    # print( app )
    # app.Animate.MenuSelect("파일(F)")
    # app.Notepad.Edit.TypeKeys("Hello World",with_spaces = True)
            
    # 메모장를 띄운다.
    app = Application().start("notepad.exe")
    
    # 메모장에 code를 적는다.
    app.UntitledNotepad.Edit.type_keys("print ('test')", with_spaces = True)
    
    # '파일' > '저장' 메뉴 실행
    app.UntitledNotepad.menu_select("파일(&F)->저장(&S)")
    
    # '다른 이름으로 저장' 창의 속성을 리스트업 한다.
    # app.다른_이름으로_저장.print_control_identifiers()
    
    # 파일 full 경로 입력
    app.다른_이름으로_저장.Edit1.SetEditText("c:\python\code\samplecode.py")
    
    # '파일이름' 콤보박스에서 파일 종류 선택
    app.다른_이름으로_저장.ComboBox2.Select("모든 파일")
    
    # '파일형식' 콤보박스에서 인코딩 선택
    app.다른_이름으로_저장.ComboBox3.Select("UTF-8")
    
    # 바로 저장 버튼을 누르면 미처 콤보 박스가 안 바뀌어 에러가 나서 1초 시간 줌
    import time
    time.sleep(1.0)
    
    # 저장 버튼 누름
    app.다른_이름으로_저장.Button1.click()
    print("build")

def remove() :
    path = "//sdcard//CJHP_TEST//"
    os.system("adb shell am force-stop kr.co.nod.cjhtmlplayer_unlock;")
    os.system("adb shell rm -rf %s" % path)
    os.system("adb shell am start -a android.intent.action.MAIN -n kr.co.nod.cjhtmlplayer_unlock/.display.activity.CJInitActivity")
    print("adb remove")

def setting( mode ) :
    if mode == "publish" :
        publish()
    elif mode == "common" :
        copyCommon()
    elif mode == "module" :
        copyModule()
    elif mode == "update" :
        copyCommon();
        copyModule();
    elif mode == "push" :
        push();
    elif mode == "build" :
        build();
    elif mode == "remove" :
        remove();

setting( strMode )


