user_input = input("Input: ")

vowels = "aeiouAEIOU"

output = ""
for i in user_input:
    if i in vowels:
        continue
    else:
        output = output + i

print("Output: " + output)
