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
    for x in range(len(my_list)) :
        if my_list[x] > max :
            max_2 = max
            max = my_list[x]
    return max_2
print("max_2 :", get_max_2(my_list))

print("max number: ", get_max(my_list))
print("min number: ", get_min(my_list))

def get_2_max(my_list) :
    max1 = 0
    max2 = 0
    for b in range(len(my_list)) :
        if my_list[b] > max1 :
            max2 = max1
            max1 = my_list[b]
    return max1, max2
print("2 max number: ", get_2_max(my_list))