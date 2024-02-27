def get_min_number(numbers) :
    result = numbers[0]
    for num in numbers :
        if num < result :
            result = num
    return result

numbers = [10, 38, 20, 50,62,18, 39, 29]
print("Min Number: ", get_min_number(numbers))