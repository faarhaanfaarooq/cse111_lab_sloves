i = input()
lst = i.split(" ")
num_list = []
for i in range(int(lst[0])):
    x = int(input())
    num_list.append(x)

x = 5-int(lst[1])
result = ""
for i in range(len(num_list)):
    if int(num_list[i]) <= x:
        result=result+str(num_list[i])

print(len(result)//3)
