#Khai báo lớp HCN
class HCN :
    #Khai báo thuộc tính chiều dài:
    chieu_dai = 0
    #Khai báo thuộc tính chiều rộng:
    chieu_rong = 0
    #Khai báo phương thức tính diện tích:
    def tinh_dien_tich(self) :
        return self.chieu_dai * self.chieu_rong
    
    #khai báo phương thức tính chu vi
    def tinh_chu_vi(self) :
        return 2 * (self.chieu_dai + self.chieu_rong)
    
hcn_1 = HCN()
hcn_1.chieu_dai = 4
hcn_1.chieu_rong = 5
#tính diện tích, chu vi hcn_1
dien_tich = hcn_1.tinh_dien_tich()
chu_vi = hcn_1.tinh_chu_vi()
print("Diện tích hcn1: ", dien_tich)
print("Chu vi hcn1: ", chu_vi)

hcn_2 = HCN()
hcn_2.chieu_dai = 6
hcn_2.chieu_rong = 8
#tính diện tích, chu vi hcn_2
dien_tich = hcn_2.tinh_dien_tich()
chu_vi = hcn_2.tinh_chu_vi()
print("Diện tích hcn2: ", dien_tich)
print("Chu vi hcn2: ", chu_vi)