class Account:
    def __init__(self, name = "Default Account", bal = 0):
        self.name = name
        self.bal = bal
        self.rem = 0
    def details(self):
        print(self.name)
        print(self.bal)
    def withdraw(self,taka):
        self.rem = self.bal-taka
        if self.rem<0:
            print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
        elif self.rem>0:
            print("Withdraw successful! New balance is: {}".format(rem))

# Write your code here
a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930);
print("------------------------")
a2.withdraw(600);
print("------------------------")
a1.withdraw(6929)