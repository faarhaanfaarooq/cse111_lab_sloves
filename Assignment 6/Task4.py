class Travel:
    count = 0
    def __init__(self, src, dest):
        self.source = src
        self.dest = dest
        self.time = None
        Travel.count+=1
    def set_time(self, time):
        self.time = time
    def display_travel_info(self):
        print("Source: {}".format(self.source))
        print("Destination: {}".format(self.dest))
        if self.time != None:
            print("Flight Time: {}".format(self.time))
        else:
            print("Flight Time: 1:00")
        
    def set_destination(self, d):
        self.dest = d
    def set_source(self, s):
        self.source = s

# Write your code here
print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)