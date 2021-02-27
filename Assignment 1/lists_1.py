list1=[]
list2=[]

while True:
    i = input()
    if i != "STOP":
        list1.append(int(i))
    else:
        break
        
while i < len(list1):
    if list1[i] not in list2:
        list2.append(int(i))
print(list1)
print(list2)