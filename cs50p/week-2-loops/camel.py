char = input("writeCamelCase: ")

snake = ""
for i in char:
    if i.isupper():
        snake = snake + "_" + i.lower()
    else:
        snake = snake + i

print(snake)
