Dictionary = {
    "Hello" : "Xin Chào",
    "hello" : "Xin chào",
    "Bye" : "Tạm biệt",
    "Green" : "Màu xanh lá cây",
    "Red" : "Màu đỏ",
    "Yellow" : "Màu vàng"
}

def translate_word(word):
    if word in Dictionary:
        print("Nghĩa của từ này là: ", Dictionary[word])
    else:
        print("giá trị không hợp lệ!") 

word = str(input("Nhập từ cần dịch: "))
translate_word(word)