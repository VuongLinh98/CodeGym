my_list = [6,8,2,9,1,7]

def get_max(my_list) :
    max = my_list[0]
    for i in my_list :
        if i > max :
            max = i
    return max

def get_min(my_list) :
    min = my_list[0]
    for a in my_list :
        if a < min :
            min = a
    return min

def get_max_2(my_list) :
    max = 0
    for x in range(1,len(my_list)-1) :
        if my_list[x] > max :
            max_2 = max
            max = my_list[x]
    return max_2
print("max_2 :", get_max_2(my_list))

print("max number: ", get_max(my_list))
print("min number: ", get_min(my_list))