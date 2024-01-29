Tien_da_chi = int(input("Nhập số tiền khách hàng đã chi: "))
if Tien_da_chi >= 150 : 
    print("Số tiền thanh toán là: ", Tien_da_chi - 50)
elif 150 > Tien_da_chi >= 100 :
    print("Số tiền thanh toán là: ", Tien_da_chi - 25)
elif 100 > Tien_da_chi >= 75 :
    print("Số tiền thanh toán là: ", Tien_da_chi - 15)
else :
    print("Số tiền thanh toán là: ", Tien_da_chi)
