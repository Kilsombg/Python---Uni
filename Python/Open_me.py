def answ():
    k = input("(Y,N) : ")
    k = k.upper()
    return k

k = ''

while k != "Y":
    print(""" Wanna go out? """)
    k = answ()

    if k == 'Y' or k == "YES" or k == "YEAH" or k== "YE" or k == "YEA":
        print("Just send me a picture of that or answer me in messenger.")
        break
    if k == 'N' or k == "NO" or k == "NOT A CHANCE" or k == "NOPE":
        print("""I don't accept 'No' for an answer.
                """)
    if k == "ON A DATE" or k == "ON A DATE?":
        print("If you want to say it like that, sure...")
        print("Just send me a picture of that or answer me in messenger.")
        break

e = input()