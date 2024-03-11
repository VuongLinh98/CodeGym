class Student :
    #Khai báo thuộc tính lưu trữ danh sách
    danh_sach = []

    #Thêm sinh viên
    def themSinhVien( self, sinh_vien ):
        self.danh_sach.append( sinh_vien )
    
    #xem danh sách sinh viên
    def xemDanhSachSinhVien( self ):
        for sinh_vien in self.danh_sach:
            print( "sinh vien: ", sinh_vien)
    
    #Cập nhật thông tin của sinh viên trong danh mục
    def capnhatThongTin( self, vitri, giatri ):
        self.danh_sach[vitri] = giatri

    #xóa thông tin sinh viên
    def xoaSinhVien(self, vitri):
        del self.danh_sach[vitri]

    #tìm kiếm thông tin sinh viên trong danh mục theo từ khóa
    def timkiemSinhVien(self, vitri):
        return self.danh_sach[vitri]

    #sắp xếp danh sách sinh viên
    def sapxepDanhSach(self):
        self.danh_sach.sort()

SV = Student()

SV.themSinhVien({ 
    "msv" : "001",
    "ten" : "Vuong Linh"
})
SV.themSinhVien({
    "msv" : "002",
    "ten" : "Ba Tong"
})
SV.themSinhVien({
    "msv" : "003",
    "ten" : "Bich Ly"
})
SV.themSinhVien({
    "msv" : "004",
    "ten" : "Ngoc Anh"
})

SV.capnhatThongTin(0,{
    "msv" : "011",
    "ten" : "Xuan Phuong"
})

SV.xoaSinhVien(2)

SV.xemDanhSachSinhVien()

print(SV.timkiemSinhVien(1))
print("======Sap xep=======")
