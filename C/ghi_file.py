# Mở file và ghi thêm nội dung
file = open("list/data.txt", "a+")
file.write( "\nPython")
file.close()
#Mở file và đọc file
file = open("list/data.txt", "r")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print ('Dòng 1: ', line1)
print ('Dòng 2: ', line2)
print ('Dòng 3: ', line3)