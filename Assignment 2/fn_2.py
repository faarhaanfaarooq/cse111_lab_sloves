def bmi(height, weight):
    height = height/100
    B = weight/(height*height)
    print(round(B,1))

bmi(175, 96)
