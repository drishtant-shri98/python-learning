x, y, z = input("Expression: ").split()

x = float(x)
z = float(z)

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        if z != 0:
            print(x/z)
        else:
            print("cannot divide by zero")
    case "*":
        print(x*z)
