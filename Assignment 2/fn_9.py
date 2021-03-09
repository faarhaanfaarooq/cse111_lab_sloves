def capital_checker(string):
    items = string.split(" ")
    if items[0][0].islower():
        items[0] = items[0].capitalize()
        for i in range(1,len(items)-1):
            if items[i].endswith((".","!","?")) and items[i+1][0].islower():
                items[i+1]=items[i+1].capitalize()
            if items[i] == "i":
                items[i] = items[i].capitalize()
        outpur_string = " ".join(items)
        return outpur_string
    
print(capital_checker("my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily.do you know my pet dog’s name? i love my pet very much."))
