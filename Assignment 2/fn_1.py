def division(num1,num2):
    if num2 == 0:
        return 0
    else:
        div = num1/num2
        if div == 0:
            return 0
        else:
            div = div-int(div)
            return div

print(division(5,2))
print(division(5,0))
print(division(0,5))