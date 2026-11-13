charge = 50
while charge > 0:
    insert = int(input("Insert Coin: "))
    if insert not in (5,10,25):
        print("Amount Due:", charge)
    else:
        charge = charge - insert
        if charge > 0:
            print("Amount Due:", charge)
        elif charge <=0:
            print("Change Owed:", charge - charge*2)
