def division(num1,num2):
    #num1 = int(input())
    #num2 = int(input())
    if num2 == 0:
        print(0)
    else:
        div = num1/num2
        div = div-int(div)
    
    print(div)

division(5,0)