class Student:
    def __init__(self, name, id, dep="CSE"):
        self.name = name
        self.id = id
        self.dep = dep
        self.dailyeffort=0
        if dep != None:
            self.dep = dep
    def dailyEffort(self,hours):
        self.dailyeffort=int(hours)
    def printDetails(self):
        print("Name: ",self.name)
        print("ID: ",self.id)
        print("Department: ",self.dep)
        print("Daily Effort: {} hour(s)".format(self.dailyeffort))
        if self.dailyeffort<=2:
            print("Suggestion: Should give more effort!")
        elif self.dailyeffort<=4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others.")
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()