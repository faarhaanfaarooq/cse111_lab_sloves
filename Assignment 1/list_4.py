while True:
    number = input()
    if number == "STOP":
        break
    else:
        number = number.split(" ")
        lst=[]
        for i in range(0,len(number)):
            number[i] = int(number[i])
        for j in range(0,len(number)-1):
            absolute = abs(number[j]-number[j+1])
            lst.append(absolute)
        count = 0
        for k in range(1,len(number)):
            if k in lst:
                count+=1
        if count == len(number)-1:
            print("UB Jumper")
        else:
            print("Not UB Jumper")
