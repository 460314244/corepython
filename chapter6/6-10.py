input1=raw_input('Please input a string:')
output=''
for i in input1:
    if i==i.upper():
        output=output +i.lower()
    else:
        output=output+ i.upper()
print output
  
