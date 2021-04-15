class Laptop:
    laptopCount = 0
    def __init__(self, name, number):
        self.name = name
        self.count = number
        Laptop.laptopCount += number
    @staticmethod
    def advantage():
        s1 = "Laptops are portable"
        return s1
    @classmethod
    def resetCount(cls):
        Laptop.laptopCount = 0


lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)