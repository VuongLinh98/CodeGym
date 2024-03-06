gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

#tạo 2 list
text = []
numbers = []
for i in gadgets :
    if isinstance(i, str):
        text.append(i)
    else:
        numbers.append(i)
print("List chứa chuỗi: ", text)
print("List chứa số: ", numbers)

#Sắp xếp list chứa chuỗi
text.sort()
print("List text theo thứ tự tăng dần: ", text)
text.sort(reverse=True)
print("List text theo thứ tự giảm dần: ", text)

#Sắp xếp list số
numbers.sort()
print("List numbers theo thứ tự tăng dần: ", numbers)
numbers.sort(reverse=True)
print("List numbers theo thứ tự giảm dần: ", numbers)