list = [1,2,3,4,5]
list_1 = list.copy()
if len(list) == 0:
    print(list_1,"=>",list)
else:
    b = list[-1]
    del(list[-1])
    list.insert(0,b)
    print(list_1,"=>",list)


