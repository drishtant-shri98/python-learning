def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
     clean_value = float(d.replace("$",""))
     return clean_value

def percent_to_float(p):
    clean_value = float(p.replace("%",""))
    return clean_value/100

main()
