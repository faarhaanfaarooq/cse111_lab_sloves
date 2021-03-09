def palindrome_checker(string1):
    string2 = "".join(reversed(string1))
    if string1==string2:
        return "Palindrome"
    else:
        return "Not a palindrome"
    
print(palindrome_checker("madam"))
            