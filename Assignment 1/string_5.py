s1 = input()
s2 = input()
x = ''
for char in s1:
    if char in s2:
        x+=char   

for char in s2:
    if char in s1:
        x+=char   

if(x==''):
    print("Nothing in common.")
else:
    print(x)