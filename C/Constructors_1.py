class Car :
    Name = ""
    Model = ""
    Weight = 0
    Color = ""

    #khởi tạo hàm mặc định
    def __init__(self, Name, Model, Weight, Color):
        self.Name = Name
        self.Model = Model
        self.Weight = Weight
        self.Color = Color
    def start(self) :
        pass
    def dive(self) :
        pass
    def stop(self) :
        pass
    def brake(self) :
        pass
    def toString(selft) :
        pass

car = Car("A","B",99,"D")
car.show()
