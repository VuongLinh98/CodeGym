numbers = [1, 34, 25, 67, 24, 20, 49, 28, 0, 3, 4, 27, 100, 728, 35]

def remove_largest_number(numbers) :
    largest = 0
    for number in numbers :
        if number > largest : 
            largest = number 
    print(largest)
    numbers.remove(largest)

remove_largest_number(numbers)
print(numbers)
    