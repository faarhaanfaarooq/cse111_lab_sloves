list1=[]
list2=[]

while True:
    i = input()
    if i != "STOP":
        list1.append(int(i))
    else:
        break

x=0
while x < len(list1):
    if list1[x] not in list2:
        list2.append(list1[x])
    x+=1


y=0
while y < len(list2):
    c = list1.count(list2[y])
    print(list2[y], "-", c, "times")
    y+=1





