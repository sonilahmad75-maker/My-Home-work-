import random

a=random.randint(1,4)
user=0
score=1
while 0<=score<3 :
    user=int(input('\a plz select one of this :\n stone [1] :\n paper [2] :\n secore[3] :\n \a'))

    if user==a :
        score+=1
    else:
        score-=1
    print('your score is %s'%(score))

if score==3 :
    print('you win !')
else:
    print('Fucking your mind !')



