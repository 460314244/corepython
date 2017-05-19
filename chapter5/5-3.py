while True:
    i=int(raw_input("Please input number that it 100..."))
    if 90<=i<=100:
        print "A"
        break
    elif 80<=i<=89:
        print "B"
        break
    elif 70<i<=79:
        print "C"
        break
    elif 60<=i<=69:
        print "D"
        break
    elif i<60:
        print "F"
        break
    else:
        print "the number is too big"
        continue

