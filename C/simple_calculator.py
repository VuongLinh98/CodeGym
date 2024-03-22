from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x320")
root.title("Simple Calculator")

#tạo ô input
nhapSo = Entry(root, width=50)
nhapSo.grid(row= 0, columnspan=4, pady=10, padx=50)

# Hàm xử lý khi nhấn vào các phím 0,1,2,3,4,5,6,7,8,9,+,-,*,/, dấu chấm
def onPress(number):
    # Thêm dữ liệu vào phía sau ô input
    nhapSo.insert('end',number)
# Hàm xử lý khi nhấn phím =
def onEqual():
    #lay gia tri trong o input
    value = nhapSo.get()
    # Xu ly bieu thuc
    result = eval(value)
    # xoa du lieu trong o va dua vao noi dung moi
    nhapSo.delete(0, 'end')
    nhapSo.insert('end',result)
# Hàm xử lý khi nhấn phím Clear
def onClear():
    # Xoa toan bo ô input
    nhapSo.delete(0, 'end') 

#tạo phím ấn
Button(root,width=4,height=2, text="1",command=lambda: onPress('1')).grid( row=1,column=0,pady=2 )
Button(root,width=4,height=2, text="2", command= lambda: onPress('2')).grid( row=1,column=1, pady= 2 )
Button(root,width=4,height=2, text="3", command=lambda: onPress('3') ).grid( row=1,column=2,pady=2 )
Button(root,width=4,height=2, text="+", command=lambda:onPress('+')).grid( row=1,column=3, pady=2 )

Button(root,width=4,height=2, text="4", command=lambda:onPress('4')).grid( row=2,column=0,pady=2 )
Button(root,width=4,height=2, text="5", command=lambda:onPress('5')).grid( row=2,column=1,pady=2 )
Button(root,width=4,height=2, text="6", command=lambda:onPress('6')).grid( row=2,column=2, pady=2 )
Button(root,width=4,height=2, text="-", command=lambda:onPress('-')).grid( row=2,column=3, pady=2 )

Button(root,width=4,height=2, text="7", command=lambda:onPress('7')).grid( row=3,column=0, pady=2 )
Button(root,width=4,height=2, text="8", command=lambda:onPress('8')).grid( row=3,column=1, pady=2 )
Button(root,width=4,height=2, text="9", command=lambda:onPress('9')).grid( row=3,column=2, pady=2 )
Button(root,width=4,height=2, text="*", command=lambda:onPress('*')).grid( row=3,column=3, pady=2 )

Button(root,width=4,height=2, text="0", command=lambda:onPress('0')).grid( row=4,column=0, pady=2 )
Button(root,width=4,height=2, text="Clear", command=onClear).grid( row=4,column=1 )
Button(root,width=4,height=2, text="=", command=onEqual).grid( row=4,column=2 )
Button(root,width=4,height=2, text="/", command=lambda:onPress('/')).grid( row=4,column=3, pady=2 )

Button(root,width=4,height=2, text=".", command=lambda:onPress('.')).grid( row=5,column=0, pady=2 )


root.mainloop()