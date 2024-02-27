def sort_numbers(num1, num2, num3) :
    temp = 0
    if num2 < num1 and num2 < num3 : 
        temp = num1
        num1 = num2
        num2 = num1
    elif num3 < num1 and num3 < num2 :
        temp = num1
        num1 = num3
        num3 = temp
    elif num2 > num3 :
        temp = num2
        num2 = num3
        num3 = temp
    else:
        print("error value!")
    return(num1, num2, num3)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Original numbers: ", x, y, z)
print("Sorted numbers: ", sort_numbers(x, y, z))
