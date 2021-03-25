class ParcelKoro:
    def __init__(self, cname="No name set" ,pweight=0):
        self.customer_name = cname
        self.product_weight = pweight
        self.fee = 0
        self.area = ""
    def calculateFee(self,area=None):
        self.area = area
        if self.product_weight == 0:
            self.fee = 0
        elif self.area == None:
            self.fee = (self.product_weight*20)+50
        else:
            self.fee = (self.product_weight*20)+100
    def printDetails(self):
        print("Customer Name: ",self.customer_name)
        print("Product Weight: ",self.product_weight)
        print("Total fee: ",self.fee)
print("**********************")
p1 = ParcelKoro()
p1.calculateFee()
p1.printDetails()
print("**********************")
p2 = ParcelKoro('Bob The Builder')
p2.calculateFee()
p2.printDetails()
print("----------------------------")
p2.product_weight = 15
p2.calculateFee()
p2.printDetails()
print("**********************")
p3 = ParcelKoro('Dora The Explorer', 10)
p3.calculateFee('Dhanmondi')
p3.printDetails()