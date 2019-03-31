'''
Write input_int() function which asks the user to provide an integer number
and returns it (as a number, not as a string). It accepts up to 3 arguments:
1. An optional prompt (like input() built-in function).
2. An optional minimum acceptable number (there is no minimum by default).
3. An optional maximum acceptable number (there is no maximum by default).
The function keeps asking the user until she provides a well-formed integer number within range.

Example usage of the function:
a = input_int("Enter an integer: ")
b = input_int("Enter a positive integer: ", 1)
c = input_int("Enter an integer not greater than 8: ", largest=8)
d = input_int("Enter an integer (4..8): ", 4, 8)
print("Provide another integer (4..8):")
e = input_int(smallest=4, largest=8)
print("Your numbers multiplied by 2:", a * 2, b * 2, c * 2, d * 2, e * 2)

Example session with the script:
Enter an integer: cake
Enter an integer: 3.4
Enter an integer: -5
Enter a positive integer: -10
Enter a positive integer: 0
Enter a positive integer: 1000
Enter an integer not greater than 8: 1000
Enter an integer not greater than 8: 7
Enter an integer (4..8): 1
Enter an integer (4..8): 4
Provide another integer (4..8):
9
8
Your numbers multiplied by 2: -10 2000 14 8 16
'''

def input_int(prompt='', smallest=None, largest=None):
    number = input(prompt)
    # PC: W zadaniu byla mowia o funkcji, ktora albo zwraca liczbe,
    #     albo zglasza wyjatek. A ta funkcja czasem zwraca None.
    #     Uzytkownik moze zrezygnowac z wprowadzania liczby podajac
    #     pusty napis. To jest OK, jesli to Twoj swiadomy wybor.
    while number:
        try:
            number = int(number)
            # PC: Tutaj wszystko jest OK, tylko skladnia moze byc
            #     bardziej zwiezla. Np. zeby nie porownywac kilka
            #     razy tego samego do None, mozna zagniezdzic if-y.
            #     Pamietaj tez ze masz do dyspozycji operatory logiczne.
            #     Ja, kiedy nie jestem w stanie w glowie skonstruowac
            #     wyrazenia logicznego, czasem wypisuje najpierw
            #     wszystkie mozliwosci w tabelce. Ponizej komentuje jak
            #     mozna ulepszyc ten kod, ktory juz tu jest.
            if smallest == None and largest == None:
                return number
            # PC: Jezeli w if-ie jest return, to tego elif-a, można
            #     zastąpić kolejnym if-em.
            elif largest == None:
                # PC: Rezygnacja z tej akrobacji jest zdecydowanie w
                #     Twoich mozliwosciach, bo ten kod troche jednak
                #     cuchnie. Jezeli nie masz nic do umieszczenia w
                #     if-ie, a jedynie w else, to trzeba zanegowac
                #     warunek:
                #         if number >= smallest:
                #             return
                #     Ta sama uwaga w dwoch miejscach nizej.
                if number < smallest:
                    pass
                else:
                    return number
            elif smallest == None:
                if number > largest:
                    pass
                else:
                    return number
            # PC: Jezeli else sklada sie wylacznie z kolejnego if-a,
            #     To mozna po prostu napisac "elif number < ...".
            #     Oszczednosc na wcieciach, choc nie zawsze na
            #     czytelnosci -- ale zawsze mozna dodac komentarz.
            else:
                if number < smallest or number > largest:
                    pass
                else:
                    return number
        except ValueError as exc:
            # PC: Jezeli decydujesz sie na drukowanie bledu parsowania,
            #     to sensownie byloby drukowac rowniez bledy zakresu
            #     liczby w tych if-ach powyzej.
            print(exc)
        number = input(prompt)

a = input_int("Enter an integer: ")
print(a)

b = input_int("Enter a positive integer: ", 1)
print(b)

c = input_int("Enter an integer not greater than 8: ", largest=8)
print(c)

d = input_int("Enter an integer (4..8): ", 4, 8)
print(d)

print("Provide another integer (4..8):")
e = input_int(smallest=4, largest=8)

print("Your numbers multiplied by 2:", a * 2, b * 2, c * 2, d * 2, e * 2)
