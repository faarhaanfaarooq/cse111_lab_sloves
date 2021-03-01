n = {}
while True:
    s = input()
    if s == "STOP":
        break
    elif s in n.keys():
        n[s] += 1
    else:
        n[s] = 1

for x,y in n.items():
    print("{} - {} times".format(x, y))