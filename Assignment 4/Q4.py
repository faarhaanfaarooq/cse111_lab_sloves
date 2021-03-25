class Cat:
    def __init__(self, cat_color = "White", cat_action = "sitting"):
        if cat_color!= None and cat_action != None:
            self.color = cat_color
            self.action = cat_action
        elif  cat_color != None:
            self.color = cat_color
    def printCat(self):
        print("{} cat is {}".format(self.color,self.action))
    def changeColor(self,color):
        self.color = color

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()