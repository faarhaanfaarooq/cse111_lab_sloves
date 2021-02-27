s = input()
up = 0
low = 0
i=0
while i < len(s):
    if s[i].isupper():
        up+=1
        i+=1
    else:
        low+=1
        i+=1

if up>low:
    print(s.upper())

else:
    print(s.lower())
