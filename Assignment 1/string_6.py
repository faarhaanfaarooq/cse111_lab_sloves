s = input()
up = False
low = False
digit = False
special_char = False
str1 = "Special missing"
str2 = "Digit missing"
str3 = "Lowercase character missing"
str4 = "Uppercase character missing"

for i in s:
    if i.isupper():
        up = True

    if i.islower():
        low = True

    if i.isdigit():
        digit = True

    if i=='_' or i=='#' or i=='@' or i=='$':
        special_char = True

if up==True and low==True and digit==True and special_char==True:
    print("OK")
elif up==True and low==True and digit==True and special_char==False:
    print(str1)
elif up==True and low==True and digit==False and special_char==True:
    print(str2)
elif up==True and low==False and digit==True and special_char==True:
    print(str3)
elif up==False and low==True and digit==True and special_char==True:
    print(str4)
elif up==True and low==False and digit==False and special_char==False:
    print(str1+", "+str2+", "+str3)
elif up==False and low==True and digit==False and special_char==False:
    print(str1+", "+str2+", "+str4)
elif up==False and low==False and digit==True and special_char==False:
    print(str1+", "+str3+", "+str4)
elif up==False and low==False and digit==False and special_char==True:
    print(str2+", "+str3+", "+str4)
elif up==True and low==True and digit==False and special_char==False:
    print(str1+", "+str2)
elif up==True and low==False and digit==True and special_char==False:
    print(str1+", "+str3)
elif up==False and low==True and digit==True and special_char==False:
    print(str1+", "+str4)
elif up==True and low==False and digit==False and special_char==True:
    print(str2+", "+str3)
elif up==False and low==True and digit==False and special_char==True:
    print(str2+", "+str4)
elif up==False and low==False and digit==True and special_char==True:
    print(str3+", "+str4)