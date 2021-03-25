class Student:
    def __init__(self,student_name = "default name"):
        self.avg=0
        if student_name != None:
            self.name = student_name
    def quizcalc(self, *numbers):
        sum=0
        for i in numbers:
            sum+=i
        self.avg = sum/3
    def printdetail(self):
        print("Hello {}".format(self.name))
        print("Your average quiz score is {}".format(self.avg))

# Write your code here
s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()