'''
A collaborative software distributed individual pages of a book among various volunteers to work on.
Now all the pages are ready and need to be assembled into a final book.
Every page is a textual file named pageN, where N is the page number.
If a page starts with [skip] marker, it should not be included in the final book.
There is also pagesCount file, which stores the total number of pages to be included in the book.
All these files are place in a single directory.
Write a script which assembles a book and prints it to the screen.
You may fix the directory and encoding of your choice.
'''

import os.path

#Sciezka wzgledna
directory = '.\\4_Stitching_a_book_FILES\\'

file = "pages_count.txt"
f = open(directory + file)
data = f.read()
f.close()

pages_count = int(data)

page_number = 1
while page_number <= pages_count:

    file = "page" + str(page_number) + ".txt"

    if os.path.isfile(directory + file):
        f = open(directory + file)
        data = f.read()
        f.close()

        if not data.startswith("[skip]"):
            print(data)

        page_number = page_number + 1
        
    else:
        print("!!!\nNie ma tylu stron do zlaczenia, ile podanych zostalo w pliku 'pages_count.txt'\n!!!")
        break
