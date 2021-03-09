def order(bname, location="Mohakhali"):
    if location != "Mohakhali":
        dcharge = 60
    else:
        dcharge = 40

    if bname == "BBQ Chicken Cheese Burger":
        price = 250
    elif bname == "Beef Burger":
        price = 170
    else:
        price = 200
    
    bill = price+dcharge+(price*0.08)
    return bill

print(order("Beef Burger", "Dhanmondi"))
print(order("Beef Burger"))