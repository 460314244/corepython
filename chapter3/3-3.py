a=[1,3,5,6,7]
s=0
i=0
while i<len(a):
    s=s+a[i]
    i+=1
    if i==5:
        b=(float(s))/len(a)
        print b
    

while True:
    q=int(raw_input("Please input date..."))
    if q<100:
        print 'ok'
        break
    else:
        print 'Are you a pig..'
        continue

a=[1,2,3,4,5]
s=0
for i in a:
    s=s+i
    print s         
