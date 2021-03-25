class Avengers:
    def __init__(self, name, partner):
        self.name = name
        self.partner = partner
        self.spowers = None
    def super_powers(self,*super_powers):
        self.spowers = super_powers
    def printAvengersDetail(self):
        print("Name: ",self.name)
        print("Partner: ",self.partner)
        print("Super powers: ", end="")
        print(*self.spowers, sep=",")

# Write your code here.
a1 = Avengers('Captain America', 'Bucky Barnes')
a1.super_powers('Stamina', 'Slowed ageing')
a2 = Avengers('Doctor Strange', 'Ancient One')
a2.super_powers('Mastery of magic')
a3 = Avengers('Iron Man', 'War Machine')
a3.super_powers('Genius level intellect', 'Scientist ')
print("=========================")
a1.printAvengersDetail()
print("=========================")
a2.printAvengersDetail()
print("=========================")
a3.printAvengersDetail()
print("=========================")