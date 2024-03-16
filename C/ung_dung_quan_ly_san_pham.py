product = {}


def find_index_product(myListProduct, productID):
    result = -1
    length = len(myListProduct)
    for i in range(length):
        if myListProduct[i][productID] == productID:
            result = i
    return result

#lấy thông tin sản phẩm
def getInfo(myListProduct, productID):
    if productID in myListProduct:
        print(myListProduct[find_index_product(myListProduct, productID)])

# Hiển thị danh sách sản phẩm

#thêm sản phẩm

#sửa tên sản phẩm

#xóa sản phẩm khỏi danh sách
