def main():
    message = input("whats your message - ")
    print(convert(message))

def convert(phrase):
    emoji2 = phrase.replace(":)", "🙂").replace(":(", "🙁").replace(":(","🙁")
    return emoji2

main()
