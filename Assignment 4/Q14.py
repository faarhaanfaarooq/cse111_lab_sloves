class EPL_Team:
    def __init__(self, name, song="No Slogan"):
        self.name = name
        self.song = song
        self.title = 0
    def increaseTitle(self):
        self.title = self.title + 1
        return self.title
    def showClubInfo(self):
        print("Name: ",self.name)
        print("Song: ",self.song)
        print("Total No of Title: ",self.title)
    def changeSong(self, slogan):
        self.song = slogan

# Write your code here
manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())