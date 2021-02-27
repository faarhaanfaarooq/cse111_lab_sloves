list1 = [int(i) for i in input().split()]
list2 = [int(i) for i in input().split()]
list3 = []

for i in list1:
    for j in list2:
        pro = i*j
        list3.append(pro)

print(list3)
