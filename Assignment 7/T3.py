class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
#write your code here
class Cricket_Tournament(Tournament):
    def __init__(self,name='Default',team=0,tp="no type"):
        self.t = "Cricket Tournament"
        self.team = team
        self.tp = tp
        super().__init__(name)
    
    def detail(self):
        print(self.t,"name: ",self.get_name())
        print("number of teams: ",self.team)
        return "team type: "+self.tp
    
class Tennis_Tournament(Tournament):
    def __init__(self,name,team):
        self.t = "Tennis Tournament"
        self.team = team
        super().__init__(name)
    
    def detail(self):
        print(self.t,"name: ",self.get_name())
        return "number of teams: "+ str(self.team)
        

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())