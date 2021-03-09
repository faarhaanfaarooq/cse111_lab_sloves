def vowel_counter(name):
    vowels = ["a", "e", "i", "o", "u"]
    name_vowles = ""
    counter = 0
    for i in name:
        if i in vowels:
            name_vowles+= i
            counter+=1
    return name_vowles, counter

gg = vowel_counter("Steve Jobs")

if gg[1]==0:
    print("No vowels in the name")

else:
    print("Vowels: "+str(gg[0].split())+". Total number of vowels:"+str(gg[1]))
    
