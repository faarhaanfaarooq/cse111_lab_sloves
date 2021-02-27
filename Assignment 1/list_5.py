s = input()
lst1= []
lst2= []
lst3= []
lst4= []
for char in s:
    if (ord(char)>=65 and ord(char)<=90):
        lst1.append(char)

    elif (ord(char)>=97 and ord(char)<=122):
        lst2.append(char)

    elif (ord(char)>=48 and ord(char)<=57):
        print(char)
        if(int(char)%2==0):
            lst3.append(char)
        else: 
            lst4.append(char)
lst1.sort()
lst2.sort()
lst3.sort()
lst4.sort()
result = ""

for item in lst2:
    result+=item
for item in lst1:
    result+=item
for item in lst4:
    result+=item
for item in lst3:
    result+=item

print(result)
