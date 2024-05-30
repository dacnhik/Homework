list=[]
if len(list) % 2 == 0:
    i = len(list) // 2
    list_1 = list[:i]
    list_2 = list[i:]
    list = [list_1,list_2]
    print (list)
elif len(list) == 0:
    list_1 = []
    list_2 = []
    list = [list_1,list_2]

else:
    i=len(list) // 2 + 1
    list_1 = list[:i]
    list_2 = list[i:]
    list = [list_1, list_2]
    print (list)