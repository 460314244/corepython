list_a=[1,2,3,4]
list_b=['a','b','c','d']
list_c=zip(list_a,list_b)
print list_c
dict_a={}
for i in list_c:
    dict_a.update({i[0]:i[1]})
print dict_a
