
user=''
while user!='yes':
    try :
        
        a =int(input('plz enter your number 1\a :'))
        b =int(input('plz enter your number 2 \a:'))
        
    except :
        print('invaled inpute \a!')

    c =input('plz enter your \aoperator :')
    
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
            print('that is \a\aimposible !')
    else :
        print('invalide charactor \a!')
    user = input("do you want to stop\a ? (yes/no)")
print('thank you for use our app\a ! \u00A9')
            
    
        
        
        
  