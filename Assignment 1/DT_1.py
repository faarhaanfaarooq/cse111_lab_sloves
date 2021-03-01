n = []
n.append(input())
n.append(input())
output = {}
unique = []

for num in n:
    for i in num.split(","):
        i = i.split(":")
        key = i[0].strip()
        value = i[1].strip()

        if key in output:
            output[key].append(value)
        else:
            output[key] = [value]
            
for k, v in output.items():
    sum = 0
    for x in v:
        x = int(x)
        if not x in unique:
            unique.append(x)
        sum += x
    output[k] = sum

map(int, unique)
unique.sort()
print(output)
print(tuple(unique))
