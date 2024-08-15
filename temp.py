import pandas as pd
import csv
import tkinter
#import random
window = tkinter.Tk()

df=pd.read_csv('C:/Users/ddd/Desktop/supplier_dataaa.csv' ,  encoding = 'CP949')
df1=df.iloc[0:4]
File = open('C:/Users/ddd/Desktop/supplier_dataaa.csv')
Reader = csv.reader(File)
Data = list(Reader)
list_of_entries = []
for x in list(range(0,len(Data))):
   list_of_entries.append(Data[x][1])
  
frame1=tkinter.Frame(window, relief="solid", bd=1,)
frame2=tkinter.Frame(window, relief="solid", bd=1,)
frame3=tkinter.Frame(window, relief="solid", bd=1,)
frame4=tkinter.Frame(window, relief="solid", bd=1,)
frame5=tkinter.Frame(window, relief="solid", bd=1,)
window.title("☆☆☆ 어!느새부터여행은어려워 ☆☆☆")
window.geometry("1100x1500+100+100")
window.resizable(True,True)

story1 = tkinter.Label(frame4, text= "여행지 정보\n", font = "Verdana 10 bold", width = 15)
story2 = tkinter.Label(frame2, text="반복되는 일상!\n 지겹지 않으신가요? ♡ 지금 당장 떠납시다!! ♡\n", font = "Verdana 15 bold", fg="white", bg="skyblue")
story3 = tkinter.Label(frame1, text= "지역(1개 이상)   테마(1개 이상)", font = "Verdana 10 bold")
story5 = tkinter.Label(frame5, text= "여행지 저장하기!", font = "Verdana 14 bold", fg="white", bg="skyblue", width = 14)
lb = tkinter.Label(frame4)     
lb2 = tkinter.Label(frame5)
lb3 = tkinter.Label(frame5)
lb4 = tkinter.Label(frame5)

a = []

def btnpress():                 
    if CheckVar1.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='서울특별시') & (df['테마'] =='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar1.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='서울특별시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar1.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='서울특별시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar1.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='서울특별시') &(df['테마']=='힐링')])     
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar2.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='부산광역시') &(df['테마']=='문화/예술')])   
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar2.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='부산광역시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar2.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='부산광역시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar2.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='부산광역시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar3.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='대구광역시') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar3.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='대구광역시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar3.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='대구광역시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar3.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='대구광역시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar4.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='인천광역시') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar4.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='인천광역시') &(df['테마']=='역사/유적')]) 
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar4.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='인천광역시') &(df['테마']=='축제/체험')])   
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar4.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='인천광역시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar5.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='광주광역시') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar5.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='광주광역시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar5.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='광주광역시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar5.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='광주광역시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar6.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='대전광역시') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar6.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='대전광역시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar6.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='대전광역시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar6.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='대전광역시') &(df['테마']=='힐링')]) 
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar7.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='울산광역시') &(df['테마']=='문화/예술')])     
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar7.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='울산광역시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar7.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='울산광역시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar7.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='울산광역시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar8.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='세종시') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar8.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='세종시') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar8.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='세종시') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar8.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='세종시') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar9.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='경기도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar9.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='경기도') &(df['테마']=='역사/유적')]) 
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar9.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='경기도') &(df['테마']=='축제/체험')])  
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar9.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='경기도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar10.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='강원도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar10.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='강원도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar10.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='강원도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar10.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='강원도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar11.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청남도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar11.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청남도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar11.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청남도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar11.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청남도') &(df['테마']=='힐링')]) 
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar12.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청북도') &(df['테마']=='문화/예술')])     
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar12.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청북도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar12.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청북도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar12.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='충청북도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar13.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라남도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar13.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라남도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar13.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라남도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar13.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라남도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar14.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라북도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar14.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라북도') &(df['테마']=='역사/유적')]) 
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar14.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라북도') &(df['테마']=='축제/체험')])    
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar14.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='전라북도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar15.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상남도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar15.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상남도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar15.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상남도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar15.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상남도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar16.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상북도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar16.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상북도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar16.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상북도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar16.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='경상북도') &(df['테마']=='힐링')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar17.get() == 1 & CheckVar18.get() == 1 :        
        a.append(df.loc[(df['지역']=='제주특별자치도') &(df['테마']=='문화/예술')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar17.get() == 1 & CheckVar19.get() == 1 :        
        a.append(df.loc[(df['지역']=='제주특별자치도') &(df['테마']=='역사/유적')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar17.get() == 1 & CheckVar20.get() == 1 :        
        a.append(df.loc[(df['지역']=='제주특별자치도') &(df['테마']=='축제/체험')])
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    if CheckVar17.get() == 1 & CheckVar21.get() == 1 :        
        a.append(df.loc[(df['지역']=='제주특별자치도') &(df['테마']=='힐링')])      
        a.append("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")
    lb.config(text=a, font = "Verdana 10 bold") 
    
    
def btnpress2():
    lb2.config(text=a, font = "Verdana   5 bold")
    
    
def btnpress3():
    a.clear()
    lb.config(text=a, font = "Verdana 10 bold")
    
listbox1 = tkinter.Listbox(frame5, font = "Verdana 10 bold", width = 20, height = 11) 
b = []
def result(n):
    listbox1.insert(0,ent1.get())
    listbox.delete(0,)
ent1 = tkinter.Entry(frame5, bd = 2, width = 26) 
ent1.bind("<Return>", result)

CheckVar1=tkinter.IntVar()
CheckVar2=tkinter.IntVar()
CheckVar3=tkinter.IntVar()
CheckVar4=tkinter.IntVar()
CheckVar5=tkinter.IntVar()
CheckVar6=tkinter.IntVar()
CheckVar7=tkinter.IntVar()
CheckVar8=tkinter.IntVar()
CheckVar9=tkinter.IntVar()
CheckVar10=tkinter.IntVar()
CheckVar11=tkinter.IntVar()
CheckVar12=tkinter.IntVar()
CheckVar13=tkinter.IntVar()
CheckVar14=tkinter.IntVar()
CheckVar15=tkinter.IntVar()
CheckVar16=tkinter.IntVar()
CheckVar17=tkinter.IntVar()
CheckVar18=tkinter.IntVar()
CheckVar19=tkinter.IntVar()
CheckVar20=tkinter.IntVar()
CheckVar21=tkinter.IntVar()
c1=tkinter.Checkbutton(frame1,text="서울특별시",variable=CheckVar1, font = "Verdana 10 bold")
c2=tkinter.Checkbutton(frame1,text="부산광역시",variable=CheckVar2, font = "Verdana 10 bold")
c3=tkinter.Checkbutton(frame1,text="대구광역시",variable=CheckVar3, font = "Verdana 10 bold")
c4=tkinter.Checkbutton(frame1,text="인천광역시",variable=CheckVar4, font = "Verdana 10 bold")
c5=tkinter.Checkbutton(frame1,text="광주광역시",variable=CheckVar5, font = "Verdana 10 bold")
c6=tkinter.Checkbutton(frame1,text="대전광역시",variable=CheckVar6, font = "Verdana 10 bold")
c7=tkinter.Checkbutton(frame1,text="울산광역시",variable=CheckVar7, font = "Verdana 10 bold")
c8=tkinter.Checkbutton(frame1,text="세종시",variable=CheckVar8, font = "Verdana 10 bold")
c9=tkinter.Checkbutton(frame1,text="경기도",variable=CheckVar9, font = "Verdana 10 bold")
c10=tkinter.Checkbutton(frame1,text="강원도",variable=CheckVar10, font = "Verdana 10 bold")
c11=tkinter.Checkbutton(frame1,text="충청남도",variable=CheckVar11, font = "Verdana 10 bold")
c12=tkinter.Checkbutton(frame1,text="충청북도",variable=CheckVar12, font = "Verdana 10 bold")
c13=tkinter.Checkbutton(frame1,text="전라남도",variable=CheckVar13, font = "Verdana 10 bold")
c14=tkinter.Checkbutton(frame1,text="전라북도",variable=CheckVar14, font = "Verdana 10 bold")
c15=tkinter.Checkbutton(frame1,text="경상남도",variable=CheckVar15, font = "Verdana 10 bold")
c16=tkinter.Checkbutton(frame1,text="경상북도",variable=CheckVar16, font = "Verdana 10 bold")
c17=tkinter.Checkbutton(frame1,text="제주특별자치도",variable=CheckVar17, font = "Verdana 10 bold")
c18=tkinter.Checkbutton(frame1,text="문화/예술",variable=CheckVar18, font = "Verdana 10 bold")
c19=tkinter.Checkbutton(frame1,text="역사/유적",variable=CheckVar19, font = "Verdana 10 bold")
c20=tkinter.Checkbutton(frame1,text="축제/체험",variable=CheckVar20, font = "Verdana 10 bold")
c21=tkinter.Checkbutton(frame1,text="힐링",variable=CheckVar21, font = "Verdana 10 bold")
button1 = tkinter.Button(frame1, text = "지역 및 테마 선택하기!",command = btnpress, font = "Verdana 10 bold", bd= 2, fg="white", bg="skyblue")
button2 = tkinter.Button(frame4, text = "여행을 떠나보세요",command =btnpress2, font = "Verdana 13 bold", bd= 1, fg="white", bg="skyblue")
button3 = tkinter.Button(frame1, text = "초기화", command = btnpress3, font = "Verdana 10 bold", bd = 2, fg="skyblue", bg ='white')
story6 = tkinter.Label(frame5, text = " ", font ="Verdana 13 bold")
story1.grid(row=2, column=1, sticky = 'w', ipadx = 117)
story2.grid(row=1, column=0,ipadx = 250, sticky = 'w')
story3.grid(row=2, column = 0)
story5.grid(row=19, column=2, sticky = 'e')
story6.grid(row=19, column=1, sticky = 'e')
listbox1.grid(row=21, column=2, sticky = 'e')
c1.grid(row = 3, column=0, sticky ='w')
c2.grid(row = 4, column=0, sticky ='w')
c3.grid(row = 5, column=0,sticky ='w')
c4.grid(row = 6, column=0, sticky ='w')
c5.grid(row = 7, column=0,sticky ='w')
c6.grid(row = 8, column=0,sticky ='w')
c7.grid(row = 9, column=0,sticky ='w')
c8.grid(row = 10, column=0,sticky ='w')
c9.grid(row = 11, column=0,sticky ='w')
c10.grid(row = 12, column=0,sticky ='w')
c11.grid(row = 13, column=0,sticky ='w')
c12.grid(row = 14, column=0,sticky ='w')
c13.grid(row = 15, column=0,sticky ='w')
c14.grid(row = 16, column=0,sticky ='w')
c15.grid(row = 17, column=0,sticky ='w')
c16.grid(row = 18, column=0,sticky ='w')
c17.grid(row = 19, column=0,sticky ='w')
c18.grid(row = 3, column=0,sticky ='e')
c19.grid(row = 4, column=0, sticky ='e')
c20.grid(row = 5, column=0, sticky ='e')
c21.grid(row = 6, column=0,sticky ='e')
button1.grid(row =22, column=0,columnspan = 2, sticky = 'w')
button3.grid(row =22, column=0, sticky = 'e')
button2.grid(row =23, column=0,columnspan = 4)
lb.grid(row = 22, column=1)
lb2.grid(row = 20, column=0, sticky = 'n')
ent1.grid(row = 20, column = 2, sticky = 'e')
frame1.grid(row = 2, column=0, sticky = 'nw', ipadx=22, ipady = 3)
frame2.grid(row = 0, column=0, sticky = 'w' )
frame3.grid(row = 21,column=0,sticky = 'nw' )
frame4.grid(row = 2,column=0,ipady = 3, sticky = 'n',ipadx = 40)
frame5.grid(row = 2,column=0, sticky = 'ne',ipadx=20)
window.mainloop()