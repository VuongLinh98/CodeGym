numbers = input("Nhập số cần in sang chữ: ")

text = ("không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chán")
for num in numbers :
    print(text[int(num)], end=' ')