list = [1,0,2,0,30]
list_1 = [x for x in list if x != 0]
list_0 = len(list) - len(list_1)
list_1.extend( [0] * list_0 )
print(list,"->",list_1)