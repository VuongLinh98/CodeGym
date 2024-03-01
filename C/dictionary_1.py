tu_dien = {
    "ten" : "Vương Huyền Linh",
    "tuoi" : 26,
    "can_nang" : 43
}

#1. lấy phần tử trong từ điển
print(tu_dien["ten"])
#2. lấy phần tử trong từ điển cách 2
print(tu_dien.get("tuoi"))
#3. thêm phần tử vào từ điểm
tu_dien.update({"so_thich" : "xem phim"})
#4. xóa phần tử
tu_dien.pop("so_thich")
#5. thay đổi giá trị
tu_dien["can_nang"] = 50
#6. xóa phần tử
tu_dien.pop("can_nang")
#7. xóa toàn bộ
tu_dien.clear()
