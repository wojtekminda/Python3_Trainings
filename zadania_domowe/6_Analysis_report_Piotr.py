'''
Write a script which:
1. asks the user for a path to an input file,
2. reads data from this file into memory,
3. in a loop, asks the user for a word until he or she provides an empty string,
•every time the user provides a non-empty word, the percentage of lines of the input file containing this word is printed
4. finally, if at least one non-empty word was provided, asks the user for a path of an output file to write the report to:
•if the provided path is a non-empty string, write to the file,
so that every line contains one of the provided words followed by the calculated percentage.
'''

#input_path = input('Provide a path to an input file: ')
input_path = '.\\6_Analysis_report_FILES\\twinkle.txt'

list_of_words_to_find = []
list_of_percentages = []

word_to_find = input('Provide a word (or hit ENTER to finish): ')
list_of_words_to_find.append(word_to_find)

# PC: Kolejne dwie linijki sprawdzaja dokladnie to samo, co jest podejrzane.
#     Ten if jest tu tylko po to, zeby pokryc jeden przypadek: uzytkownik nie
#     podal zadnego slowa i nie chcemy pytac o sciezke. Wystarczyloby jednak
#     zapewnic, ze list_of_words_to_find zawiera rzeczywiscie slowa, a nie
#     pusty napis, tj.:
#         word_to_find = input()
#         while word_to_find:
#             list_of_words_to_find.append(word_to_find)
#             word_to_find = input()
#     To jest w pelni analogicznie do innych zadan, ktore robilismy z taka
#     petla: uzywamy wyniku input() dopiero w srodku w while i skladniowo w
#     jednym miejscu (podczas gdy input() jest skladniowo w dwoch miejscach).
#     W tym wariancie wystarczy pozniej sprawdzic, czy list_of_words_to_find
#     jest pusta i nie pytac o sciezke. Jedno wciecie mniej.
if word_to_find:
    while word_to_find:
        # PC: Zgodnie z trescia zadania mozna bylo wczytac plik do pamieci raz,
        #     np. do listy stringow albo listy list stringow. Ty robisz to
        #     za kazdym razem, gdy uzytkownik poda slowo. Wady Twojego
        #     rozwiazania:
        #     1) Dodatkowe przetwarzanie (split/strip) wykonywane jest
        #        wielokrotnie, choc spodziewamy sie ze efekt bedzie raczej ten
        #        sam.
        #     2) Jezeli efekt nie bedzie ten sam (plik zmienil sie w czasie
        #        gdy uzytkownik myslal nad kolejnym slowem), to statystyki
        #        bede malo spojne -- jedno slowo bedzie odnosic sie do innej
        #        wersji pliku niz drugie.
        #     Zaleta Twojego rozwiazania ujawnia sie oczywiscie przy bardzo
        #     duzych plikach -- choc i w takim wypadku moglibysmy przechowac
        #     w pamieci dane wystarczajace do statystyk, a nie bedace calym
        #     plikiem ;)
        with open(input_path, 'r', encoding='utf-8') as f:
            lines_counter = 0
            contain_counter = 0
            for line in f:
                line = line.split()
                for word in line:
                    word = word.strip(',' '.' '!')
                    if word == word_to_find:
                        contain_counter = contain_counter + 1
                        break
                lines_counter = lines_counter + 1
            percentage = str(contain_counter/lines_counter*100)
            list_of_percentages.append(percentage)
            print(percentage + '% of lines contain this word')
        word_to_find = input('Provide a word (or hit ENTER to finish): ')
        list_of_words_to_find.append(word_to_find)

    #output_path = input('Provide a path to an output file: ')
    output_path = '.\\6_Analysis_report_FILES\\twinkle_info.txt'
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            # PC: Tej zmiennej moglibysmy uniknac, gdybysmy mieli
            #     np. liste list [[slowo, procent], [slowo, procent], ...].
            #     Albo gdybysmy uzyli zip(). Juz chyba o to pytales kiedys.
            counter = 0
            for word in list_of_words_to_find:
                # PC: Acha! Ten if nie bedzie potrzebny jezeli wezmiesz
                #     moj pierwszy dlugi komentarz pod uwage. Ogolnie, warto
                #     dbac o "czystosc" danych. Ten if dowodzi, ze
                #     list_of_words_to_find zawiera niepoprawne wartosci
                #     wynikajace z takiego a nie innego ukladu instrukcji
                #     sterujacych (while, if), ktore generuja te liste i teraz
                #     inne czesci kodu musza brac te wartosci pod uwage.
                if word:
                    f.write(word)
                    f.write(" ")
                    f.write(list_of_percentages[counter])
                    f.write("\n")
                    counter = counter + 1
