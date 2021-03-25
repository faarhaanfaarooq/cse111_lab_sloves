class Patient:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age
        self.symptoms = None
    def add_Symptom(self,*sym):
        self.symptoms = sym
    def printPatientDetail(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Symptoms: ",end="")
        print(*self.symptoms,sep=",")
        
# Write your code here.
p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
print("=========================")