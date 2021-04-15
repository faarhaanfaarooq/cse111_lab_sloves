class Student:
    Id = 0
    def __init__(self, name, dep, age, cgpa):
        self.name = name
        self.dep = dep
        self.age = age
        self.cgpa = cgpa
    def get_details(self):
        Student.Id+=1
        print("ID: {}".format(Student.Id))
        print("Name: {}".format(self.name))
        print("Department: {}".format(self.dep))
        print("Age: {}".format(self.age))
        print("CGPA: {}".format(self.cgpa))

    @classmethod

    def from_String(cls, strr):
        name, dep, age, cgpa = strr.split("-")
        student = cls(name, dep, age, cgpa)
        return student

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()