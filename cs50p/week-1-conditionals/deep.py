Q = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
match Q:
    case "42" | "forty-two" | "Forty Two" | "FoRty TwO" | " 42" | "forty two" | "42 " | " 42 ":
        print("Yes")
    case _:
        print("No")
