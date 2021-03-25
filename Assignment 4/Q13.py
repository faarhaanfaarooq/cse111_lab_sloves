class Batsman:
    def __init__(self, *info):
        if len(info)==3:
            self.name = info[0]
            self.runs = info[1]
            self.balls = info[2]
        else:
            self.name = "New Batsman"
            self.runs = info[0]
            self.balls = info[1]
        
    def printCareerStatistics(self):
        print("Name: ",self.name)
        print("Runs Scored: {}, Balls Faced: {}".format(self.runs, self.balls))
    def battingStrikeRate(self):
        srate = (self.runs/self.balls)*100
        return srate
    def setName(self,name):
        self.name = name


# Write your code here
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())