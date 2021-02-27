s = input()
up = -1
low = -1
i=0
for char in s:
    if char.isupper():
        if(up==-1):
            up=i
        else:
            low=i
    i+=1

if low-up > 1:
    print(s[up+1:low])

else:
    print("BLANK")
