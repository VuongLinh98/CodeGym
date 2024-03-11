class Date:
    #Khai báo thuộc tính
    day = 0
    month = 0
    year = 0

    #khai báo phương thức
    def __init__(self, ts_day, ts_month, ts_year):
        #thiết lập giá trị cho các thuộc tính
        #Khai báo các thuộc tính
        self.day = ts_day
        self.month = ts_month
        self.year = ts_year

    #Trả về giá trị thuộc tính day
    def getDay(self):
        return self.day
    #Trả về giá trị thuộc tính month
    def getMonth(self):
        return self.month
    #Trả về giá trị thuộc tính year
    def getYear(self):
        return self.year
    
    #Phương thức thiết lập giá trị thuộc tính day
    def setDay(self, ts_day):
        self.day = ts_day
    #Phương thức thiết lập giá trị thuộc tính month
    def setMonth(self, ts_month):
        self.month = ts_month
    #Phương thức thiết lập giá trị thuộc tính year
    def setYear(self, ts_year):
        self.year = ts_year

    #Phương thức thiết lập giá trị thuộc tính day, month, year
    def setDate(self, ts_day, ts_month, ts_year):
        self.day = ts_day
        self.month = ts_month
        self.year = ts_year

    #phương thức trả về định dạng ngày tháng năm
    def toString(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

hom_nay = Date(8,3,2024)
print(hom_nay.toString())

hom_nay.setDay(9)
hom_nay.setYear(2025)
print(hom_nay.toString())

hom_nay.setDate(30,4,2026)
print(hom_nay.toString())

print("Hôm nay là ngày: ", hom_nay.getDay())