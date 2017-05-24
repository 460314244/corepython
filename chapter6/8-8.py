def factorial(number):
    k=1
    for i in range(1,number+1):
        k=k*i
    return k
number=int(raw_input('Please input a number ; '))
print factorial(number)

