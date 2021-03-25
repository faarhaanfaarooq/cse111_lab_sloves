class Wadiya():
    def __init__(self):
        self.name = None#"Aladeen"
        self.designation = None#"President Prime Minister Admiral General"
        self.num_of_wife = None#100
        self.dictator = None#True

wadiya = Wadiya()
wadiya.name = "Aladeen"
wadiya.designation = "President Prime Minister Admiral General"
wadiya.num_of_wife = 100
wadiya.dictator = "True"


print("Part 1:")
print("Name of President: ",wadiya.name)
print("Designation: ",wadiya.designation)
print("Number of Wife: ",wadiya.num_of_wife)
print("Is he/she a dictator: ",wadiya.dictator)

print("Part 2:")
wadiya.name = "Donald Trump"
wadiya.designation = "President"
wadiya.num_of_wife = 1
wadiya.dictator = "False"
print("Name of President: ",wadiya.name)
print("Designation: ",wadiya.designation)
print("Number of Wife: ",wadiya.num_of_wife)
print("Is he/she a dictator: ",wadiya.dictator)
print('=====================')
print("previous information lost")
