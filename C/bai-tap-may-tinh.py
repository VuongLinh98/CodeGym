import may_tinh 

a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
phep_tinh = input("Nhập phép tính: ")

if phep_tinh == "+" :
    print(a, "+", b, "=", may_tinh.tong(a,b))
elif phep_tinh == "-" :
    print(a, "-", b, "=", may_tinh.hieu(a,b))
elif phep_tinh == "*" or phep_tinh == "x" :
    print(a, "x", b, "=", may_tinh.tich(a,b))
elif phep_tinh == "/" :
    print(a, "/", b, "=", may_tinh.thuong(a,b))
else :
    print("Giá trị không hợp lệ")