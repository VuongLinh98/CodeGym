tieng_anh = ['hi', 'bye', 'love']
tieng_viet = ['chào', 'tạm biệt', 'yêu']

txt = input("Nhập giá trị tiếng anh: ")
x = tieng_anh.index(txt)
print(txt, "=>", tieng_viet[x])