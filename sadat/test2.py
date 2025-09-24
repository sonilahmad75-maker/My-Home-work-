
user=''
while user!='yes':
    try :
        
        a =int(input('plz enter your number 1 :'))
        b =int(input('plz enter your number 2 :'))
        
    except :
        print('invaled inpute !')

    c =input('plz enter your operator :')
    
    if c=='+' :
        print(a+b)
    elif c=='-' :
        print(a-b)
    elif c=='*' :
        print(a*b)
    elif c=='/' :
        if b!=0 :
            print(a/b)
        elif b==0 :
            print('that is imposible !')
    else :
        print('invalide charactor !')
    user = input("do you want to stop ? (yes/no)")
print('thank you for use our app !')
            
    
        
        
        
  