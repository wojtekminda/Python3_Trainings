print("Masz kota? (TAK/tak/NIE/nie)")
answer = input()

if answer == "tak" or answer == "TAK":
    print("A jak ma na imie?")
    cat_name = input()
    print(cat_name , "to piekne imie :)")

elif answer == "nie" or answer == "NIE":
    print("Szkoda!")

else:
    print("Nie rozumiem...")
