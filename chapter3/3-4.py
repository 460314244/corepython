t=1
while t:
    a=float(raw_input('Please input a number btween 1 and 100...'))
    if 1<a<100:
        print 'Your have input a number between 1 and 100..'
        t=0
    else :
        print 'Are you a big SB...'

def displayNumType(num):
    print num,"is",
    if type(num)==type(0):
        print 'an integer'
    elif type(num)==type(OL):
        print 'a long '
    elif type(num) ==type(0.0):
        print 'a complex number'
    else:
        print 'not a number at all'




