list = [1]
if len(list) == 0:
    print(list,"->",0)
else:
    new_list = []
    i = 0
    last = list[-1]
    for i in range(0,len(list)):
        if i == 0 or i % 2 == 0 :
            new_list.append(list[i])
            print(new_list)
            i = i + 1
        i = i + 1
    list_sum = sum(new_list) * last
    print(list,"->",new_list,"*",last,"=",list_sum)