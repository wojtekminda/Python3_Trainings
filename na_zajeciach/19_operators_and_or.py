mail1 = input("Podaj adres e-mail: ")
mail2 = input("Ponownie podaj adres e-mail: ")

D1 = "@samsung.com"
D2 = "@partner.samsung.com"

if mail1 == mail2:
    if mail1.endswith(D1) or mail1.endswith(D2):
        if (mail1 != D1) and (mail1 != D2):
            print("Twoj email to:", mail1)
        else:
            print("Pusta nazwa uzytkownika...")
    else:
        print("Zla domena...")
else:
    print("Podales rozne adresy...")
