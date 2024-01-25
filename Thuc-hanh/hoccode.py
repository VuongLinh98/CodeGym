string = "Python programming language"
string2 = "   Python programming language   "
# Hàm len: Lấy độ dài của chuỗi
print("Độ dài của chuỗi là: ", len(string))

#Hàm count - trả về số lần chuỗi con có mặt trong chuỗi
print("Số lần từ 'language' có mặt trong chuỗi là: ", string.count('language'))

#Hàm lower - chuyển chuỗi về dạng in thường
print("Chuỗi in thường là: ", string.lower())

#Hàm upper - chuyển chuỗi về dạng in hoa
print("Chuỗi in hoa là: ", string.upper())

#Hàm lstrip - loại bỏ các ký tự khoảng trắng ở đầu chuỗi
print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu là: ", string2.lstrip())