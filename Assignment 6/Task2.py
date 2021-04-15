class Assassin:
    number = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    def printDetails(self):
        Assassin.number+=1
        print("Name: {}".format(self.name))
        print("Success rate: {}%".format(self.rate))
        print("Total number of Assassin: {}".format(Assassin.number))
    @classmethod
    def failureRate(cls, name, rate):
        rate = 100-rate
        assassin = cls(name, rate)
        return assassin
    @classmethod
    def failurePercentage(cls, name, rate):
        rate = 100-rate
        assassin = cls(name, rate)
        return assassin


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage('Akabane', 10)
akabane.printDetails()