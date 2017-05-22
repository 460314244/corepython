import random
while True:
    dict1={'scissons':2,'fist':3,'colth':1}
    for i in dict1:
        print  i,dict1[i]
    people1=int(raw_input('Please input a number between 1-3:'))
    people2=random.randint(1,3)
    print 'PC input a number between 1-3 : ',people2
    iswin=people1-people2
    if iswin==1 or iswin==-1:
        a=max(people1,people2)
        if people1==a:
            print 'You Win!!!'
        else:
            print 'You are SB!!'
    elif iswin==0:
        print 'You are double SB!!!'
    else :
        a=min(people1,people2)
        if people1==a:
            print 'You Win!!'
        else:
            print 'You are SB!!'
    print '----------------------------------------------------------'         
