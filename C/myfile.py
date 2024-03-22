#mở file ở chế độ đọc và ghi
file = open('data.txt', 'r+')
# print("Tên của file là: ", file.name)
# print("File có đóng hoặc không?: ", file.closed)
# print("Chế độ mở file: ", file.mode)

#đọc file
str = file.read()
# print("Nội dung file: \n", str)

#viết vào file
file.write("\nĐây là dòng viết thêm!")
file.close()

file = open('data.txt', 'r+')
#Đọc từng dòng
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print("Dòng 1: ", line1)
print("Dòng 2: ", line2)
print("Dòng 3: ", line3)

file.close()
