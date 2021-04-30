class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(Football):

    def __init__(self, team_name, name, role, total_goals, total_played):
        super.__init__(team_name,name,role)
        self.total_goals = total_goals
        self.total_played = total_played
        self.ratio = 0
        
    def calculate_ratio(self):
        self.ratio = self.total_goals/self.total_played

    def print_details(self):
        self.earning_per_match = (self.total_goals*1000)+(self.total_played*10)
        print("Name: ",self._name, ", Team Name: "+ self._team)
        print("Team Role: ",self._role)
        print("Team Goal: ",self.total_goals,", Total Played: ",self.total_played)
        print("Goal Ratio: ", self.ratio)
        print("Match Earning: ",self.earning_per_match, "K")

class Manager(Football):
    def __init__(self, team_name, name, role, total_wins):
        super.__init__(team_name,name,role)
        self.total_wins = total_wins

    def print_details(self):
        self.earning_per_match = self.total_wins * 1000
        print("Name: ",self._name, ", Team Name: "+self._team)
        print("Team Role: ", self.role)
        print("Total Win: ",self.total_wins)
        print("Match Earning: ",self.earning_per_match)
player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()