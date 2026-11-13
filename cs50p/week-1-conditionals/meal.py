def main():
    time = input("What time is it? ")
    t = convert(time)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    time = time.strip().lower().replace(".", "").replace(" ", "")

    is_am = time.endswith("am")
    is_pm = time.endswith("pm")
    time = time.removesuffix("am").removesuffix("pm")   # "7:30"

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if is_pm and hours != 12:
        hours += 12        # 6 pm -> 18
    if is_am and hours == 12:
        hours = 0          # 12 am -> 0 (midnight)
    return hours + minutes / 60

if __name__ == "__main__":
    main()
