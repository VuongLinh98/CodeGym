str = input("Nhap 2 gia tri ngan cach bang dau space: ")
str = str.split(" ")
firstNumber = int(str[0])
secondNumber = int(str[1])
print(firstNumber)
print(secondNumber)

for i in range(firstNumber,secondNumber+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else :
        print(i)