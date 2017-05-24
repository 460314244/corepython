import datetime
input_d1 = raw_input('You should input datetime es: MM/DD/YY:')
input_d2 = raw_input('You should input datetime  :')
d1 = input_d1.split('/')
d2 = input_d2.split('/')
date1 = datetime.datetime(int(d1[2]),int(d1[1]),int(d1[0]))
date2 = datetime.datetime(int(d2[2]),int(d2[1]),int(d2[0]))
print date1,date2
q = date2-date1

print q.days
