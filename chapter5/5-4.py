while True:
    j=float(raw_input("you must input number that it<1..."))
    if 0<j<1:
        i=j*100
        n25=int(i/25)
        n10=int(i/10)
        n5=int(i/5)
        a25=i%25
        a10=i%10
        a5=i%5
        m25=n25
        m10=int(a25/10)
        m5=int((a25%10)/5)
        m1=int((a25%10)%5)
        print m25,'*25 and' ,m10,'*10 and' , m5,'*5 and', m1,'*1'
    else:
        print 'Please input agin ....'
        continue        
        

