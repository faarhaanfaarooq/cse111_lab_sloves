def bmi(height, weight):
    height = height/100
    B = weight/(height**2)
    if B < 18.5:
        return "Socre is {:.1f}. You are Underweight".format(B)
    elif B >= 18.5 and B <= 24.9:
        return "Socre is {:.1f}. You are Normal".format(B)
    elif B >= 25 and B <= 30:
        return "Socre is {:.1f}. You are Overweight".format(B)
    else:
        return "Socre is {:.1f}. You are Obese".format(B)

print(bmi(175,96))
print(bmi(152,48))
