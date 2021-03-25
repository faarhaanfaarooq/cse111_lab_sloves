class Panda:
    def __init__(self, p_name, p_gender, p_age):
        self.name = p_name
        self.gender = p_gender
        self.age = p_age
    def sleep(self,sleep=None):
        if sleep != None:
            if sleep >= int(3) and sleep <= int(5):
                s1 = self.name + " sleeps " + str(sleep) + " hours daily and should have Mixed Veggies"
                return s1
            elif sleep >= int(6) and sleep <= int(8):
                s2 = self.name + " sleeps " + str(sleep) +" hours daily and should have Eggplant & Tofu"
                return s2
            elif sleep >= int(9) and sleep <= int(11):
                s3 = self.name + " sleeps " + str(sleep) + " hours daily and should have Broccoli Chicken"
                return s3
        else:
            s4 = self.name + " duration is unknown thus should have only bamboo leaves"
            return s4

panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())


