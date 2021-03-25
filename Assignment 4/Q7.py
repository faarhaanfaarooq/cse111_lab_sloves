class Programmer:
    def __init__(self,c_name,l_name,exp):
        self.coder_name = c_name
        self.lan_name = l_name
        self.exp = exp
        print("Horray! A new programmer is born")

    def printDetails(self):
        print("Name: ",self.coder_name)
        print("Language: ",self.lan_name)
        print("Experience: {} years".format(self.exp))
    
    def addExp(self,yr):
        self.exp+=int(yr)
        print("Updating experience of {}".format(self.coder_name))
# Write your code here.
p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()