#Khai báo module tkinter
from tkinter import *
#phần mở rộng của thư viện tkinter
from tkinter import ttk
# Tạo cửa sổ chính cho giao diện
root = Tk()
# Thiết lập độ rộng cho giao diện
root.geometry("400x250")
# Đặt tiêu đề cho cửa sổ chính 
root.title("Bố cục với Grid")

#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH

Label(root, text = "Tài khoản").grid(row = 0, column = 0)
Entry(root).grid(row = 0, column = 1)
Label(root, text = "Mật khẩu").grid(row = 1, column = 0)
Entry(root).grid(row = 1, column = 1)
Button(root, text = "Đăng nhập").grid(row = 2, column = 0)

#======= KẾT THÚC PHẦN THÂN CHƯƠNG TRÌNH

root.mainloop()