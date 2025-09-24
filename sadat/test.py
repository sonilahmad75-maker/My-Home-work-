import tkinter
from tkinter import *
from tkinter.font import *
from tkinter.font import Font

from my_c import *

def fal(li1,li2,en1) :
    l1=li1.get(ACTIVE)
    l2=li2.get(ACTIVE)
    e=en1.get()
    e=int(e)
    
    
    
    if l1=='Meter' :
        if l2=='Meter' :
            result=e1
        elif l2=='C Meter' :
            result=e1*100
    en2.delete(0,END)
    en2.insert(END,result)

window=Tk()

window.title("sadat")

g=Font(family='f' ,size=45)

f=Font(family='sadat' ,size=20)

fra=tkinter.Frame(window, bg="lightgreen")

lab1=Label(window,text='From',font=f)
lab2=Label(window,text='To',font=f)
lab1.grid(row=0,column=0)
lab2.grid(row=0 ,column=1)


en1=Entry(window,font=f)
en2=Entry(window,font=f)
en1.grid(row=1,column =0,rowspan=2 )
en2.grid(row=1,column=1,rowspan=2)



li1=Listbox(window,font=f ,fg='green' ,exportselection=False)
li2=Listbox(window,font=f ,fg='red' ,exportselection=False)
li1.grid(row=3,column=0)
li2.grid(row=3,column=1)
li1.insert(END,'Meter')
li1.insert(END,'C Meter')
li1.insert(END,'K Meter')
li1.insert(END,'M Meter')
li1.insert(END,'Mile')
li1.insert(END,'Foot')
li2.insert(END,'Meter')
li2.insert(END,'C Meter')
li2.insert(END,'K Meter')
li2.insert(END,'M Meter')
li2.insert(END,'Mile')
li2.insert(END,'Foot')




bot=Button(window ,text='Hesab',font=f ,command=fal(), padx=5, pady=5)
bot.grid(row=4,column=0 ,rowspan=2,columnspan=2 ,sticky=W+E )

window.mainloop()

