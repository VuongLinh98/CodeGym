def count_chars(txt) :
    result = 0
    for i in txt:
        result += 1
    return result

input_str = input("Your string: ")
print("Độ dài chuỗi của bạn: ", count_chars(input_str))