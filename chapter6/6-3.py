aList=raw_input('Please input numbers,separated by space:')
bList=[]
aList = aList.split(' ')
for i in aList:
    if not i == '':
        bList.append(int(i))
    else:
        continue
bList.sort()
print bList
