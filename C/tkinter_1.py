#khai báo module tkinter
from tkinter import *
from tkinter import ttk

#tạo cửa sổ chính cho giao diện
root = Tk()
#Thiết lập độ rộng cho giao diện
root.geometry("400x250")
#Đặt tiêu đề cho cửa sổ chính
root.title("First_Program")

#==== BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH

#Tạo text “Hello World !” , đây là kết quả sẽ in ra
Label(root, text ="Hello World !").pack()
#tạo nút nhấn
Button(root, text="Cộng").pack()
#Select box
ttk.Combobox(root, values=["Mùa xuân", "Mùa hạ", "Mùa thu", "Mùa đông"]).pack()
#Check box
ttk.Checkbutton(root, text="Chọn").pack()
#Ô nhập dữ liệu
ttk.Entry(root).pack()
#Thanh kéo
ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL).pack()
#Ô nhập số
ttk.Spinbox(root, from_=0, to=100).pack()
#Ô nhập nhiều text
Text(root).pack()

#======= KẾT THÚC PHẦN THÂN CHƯƠNG TRÌNH
  
# Sử dụng phương thức để cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()