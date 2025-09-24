import random
from tkinter import *


window=Tk()

lebal=Label(window,text='I gona fuck you!')

lebal.pack()
entry=Entry(window)
window.mainloop()

user=input('Wellcome to my game plz choice the level :  easy , mediume , hard\n \a')
if user =='easy' :
    c=30
elif user=='mediume' :
    c=60
else :
    c=100
b=1
i=random.randint(b,c)
a=0
counter=5

user=''
    
while user!='yes' :
    while counter>0:
     a=int(input('Enter your number :'))
     if a==i :
            print('you win !')
            break
     elif a>i :
            print('too high')
     elif a<i :
            print('too low')
     else :
        print('you lose!')
          
     counter-=1
    
     print('you have %s chance'%(counter))
    if a==i :
        print('you are so clever tanks for using my app \a ')
    else :
        print('Hi loser ! \n fucking  your mind ! \a Ha Ha')
    user=input('Do you want to stop :\a')      
     
    
    
      
        
