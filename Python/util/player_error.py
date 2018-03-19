from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import Scrollbar
import os
import csv

def clickFind() :
    list = filedialog.askopenfilenames(initialdir =os.getcwd(),title = "choose your file")
    for item in list :
        idx = 0
        while( idx < listbox.size() ) :
            if item == listbox.get(idx) :
                item = item.replace( "csv", "" )
                idx = listbox.size()
            else :
                idx += 1
        if item.split(".")[-1] == "csv" :
            listbox.insert(END, item)
def clickClear() :
    listbox.delete(0, END) 

def clickShow() :
    idx = 0
    while( idx < listbox.size() ) :
        show( listbox.get(idx) )
        idx += 1
    listbox.delete(0, END) 

def clickResult() :
    arrError = []
    arrCount = []

    idx = 0
    while( idx < listbox.size() ) :
        arrError, arrCount = result( listbox.get(idx), arrError, arrCount )
        idx += 1

    str = ""
    if listbox.size()==1:
        fileName = listbox.get(0).split("/")[-1].replace(".csv", "")
    else :
        fileName = listbox.get(0).split("/")[-1].replace(".csv", "") + "외" + (listbox.size()-1).__str__()
    file = open('result_'+fileName+'.txt', 'w', encoding='cp949')
    idx = 0
    for i in arrError :
        str += arrCount[ idx ].__str__() + "\t" + arrError[ idx ] + "\n"
        idx += 1
    
    file.write(str)
    file.close()
    listbox.delete(0, END) 

def show( strFile ) :
    fileName = strFile.split("/")[ -1 ]
    filePath = strFile.replace( fileName, "" )
    
    f = open(strFile, 'r', encoding='cp949')
    rdr = csv.reader(f)
    text = ""
    fileName = ""

    for line in rdr:
        str = line[4]
        if str.find( "Mcode : " ) == -1 :
            text += str
        else :
            text = str
            fileName = line[0]

        while( text.find( "\n\n" ) != -1 ) :
            text = text.replace("\n\n", "")

        files = strFile.replace( ".csv", "" )
        if not os.path.isdir( files+'/' ):
            os.mkdir( files+'/' )

        file = open(files+'/'+fileName.split( "." )[ 0 ]+'.txt', 'w', encoding='utf-8')
        text = text.replace("[ 2018", "\n[ 2018")
        if len( text.split(" ") ) > 1 :
            text = text.replace( text.split( " " )[5], text.split( " " )[5]+"\n" )

        file.write(text)
        file.close()

    f.close() 
    print(strFile)

def result( strFile, arrError, arrCount ) :
    print(len(arrError))
    
    f = open(strFile, 'r', encoding='cp949')
    rdr = csv.reader(f)
    for line in rdr:
        text = line[4]
        while( text.find( "\n\n" ) != -1 ) :
            text = text.replace("\n\n", "")

        if len( text.split(" ") ) > 1 and text.find( "Mcode : " ) != -1 :
            index = text.find( text.split( " " )[6] )
            end = text.find( "[ 2018" )
            text = text[ index : end ]

            if text in arrError :
                i = arrError.index( text )
                arrCount[ i ] += 1 
            else :
                arrError.append( text )
                arrCount.append( 1 )
    f.close() 
    return arrError, arrCount

root = Tk()
root.title("플레이어 로그분석")
root.geometry("300x280")

top = Frame(root)
top.pack(pady=5)

lbl = Label(top, text="분석 파일", width=10)
lbl.pack(side="left")

btnFind = Button(top, text="불러오기", width=10, command=clickFind)
btnFind.pack(padx=5, side="left")

btnClear = Button(top, text="지우기", width=10, command=clickClear)
btnClear.pack(padx=5, side="left")

btn = Frame(root)
btn.pack(pady=5)

listbox = Listbox(btn, width = 40)
listbox.pack()
s = Scrollbar(btn, orient=HORIZONTAL)
s.pack(side="bottom", fill=X)
s.config(command=listbox.xview)

btn1 = Frame(root)
btn1.pack(pady=5)

btnBuild = Button(btn1, text="개별 분석", width=15, command=clickShow)
btnBuild.pack(padx=5, side="left")

btnPublish = Button(btn1, text="전체 결과", width=15, command=clickResult)
btnPublish.pack(padx=5, side="right")

root.mainloop()
