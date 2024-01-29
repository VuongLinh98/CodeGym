Chieu_cao = float(input("Nhập chiều cao: "))
Can_nang = float(input("Nhập cân nặng: "))
BMI = Can_nang/(Chieu_cao**2)

if BMI > 40 :
    print("Béo phì cấp độ 3")
elif 35 <= BMI < 40 :
    print("Béo phì cấp độ 2")
elif 30 <= BMI < 35 :
    print("Béo phì cấp độ 1")
elif 25 <= BMI < 30 :
    print("Thừa cân")
elif 18.5 <= BMI < 25 :
    print("Bình thường")
elif 17 <= BMI < 18.5 :
    print("Gầy cấp độ 1")
elif 16 <= BMI < 17 :
    print("Gầy cấp độ 2")
else :
    print("Gầy cấp độ 3")