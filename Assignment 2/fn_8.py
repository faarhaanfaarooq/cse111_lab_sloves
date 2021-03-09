def counter(days):
    years = int(days/365)
    days = days%365
    months = int(days/30)
    day = int(days%30)

    return years, months, day

result = counter(4000)
print(str(result[0])+ " years, "+ str(result[1])+ " months and "+ str(result[2])+ " days")
