class Joker:
    def __init__(self,name,power,is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho

#Write your class code here
j1 = Joker("Heath Ledger", "Mind Game", False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker("Joaquin Phoenix", "Laughing out Loud", True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')
#Write your code for 2,3 here
print("=====================")
print("The output of First if/else block is showing different because j1 and j2 are different objects.So, their address will not be same.")
print("The output of Second if/else block is showing same because in 22 line before the if statement we have declared 'j2.name='Heath Ledger'. Here 'Heath' Ledger is the element of j1 object. So, when we are checking in the if statement it is printing same.")