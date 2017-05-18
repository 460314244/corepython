a=[1,3,5,6,7]
s=0
i=0
while i<len(a):
    s=s+a[i]
    i+=1
    if i==5:
        b=(float(s))/len(a)
        print b
    
q=raw_input("Please input date...")
while true:
    
    if q <100:
        break
    else:
        q
