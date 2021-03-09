def div(min, max, div):
    sum = 0
    for i in range(min, max):
        if i%div == 0:
            sum = sum+i

    return sum

print(div(0,10,2))
print(div(3,16,3))
