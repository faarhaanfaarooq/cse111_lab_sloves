class Calculator:
    def __init__(self,first_value,second_value,operator):
        self.num1 = first_value
        self.num2 = second_value
        self.operator = operator

    def add(self):
        print("Result: ",num1+num2)
    def subtract(self):
        print("Result: ",num1-num2)
    def multiply(self):
        print("Result: ", num1*num2)
    def divide(self):
        print("Result: ", num1/num2)

num1 = int(input())
operator = input()
num2 = int(input())
print("Let’s Calculate!")
print("Value 1: ",num1)
print("Operator: ",operator)
print("Vaue 2: ",num2)

calculate = Calculator(num1,num2,operator)
if operator == "+":
    calculate.add()
elif operator == "-":
    calculate.subtract()
elif operator == "*":
    calculate.multiply()
else:
    calculate.divide()
