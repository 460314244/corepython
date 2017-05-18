#Using while loop
i=0
total=0
a=[1,2,3,4,5]
while i<5:
    print 'Please input number',i+1
    a[i]=float(raw_input())
    total=total+a[i]
    i+=1
print 'The total is',total

#Using for loop
total=0
a=[1,2,3,4,5]
for i in range(0,5):
    print 'Please input number',i+1
    a[i]=float(raw_input())
    total=total+a[i]
print 'The total is',total
