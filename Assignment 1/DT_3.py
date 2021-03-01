n = input()
output = {}

for i in n.split(","):
    i = i.split(":")
    key = i[0].strip()
    value = i[1].strip()
    if value in output:
        output[value].append(key)
    else:
        output[value] = [key]
print(output)