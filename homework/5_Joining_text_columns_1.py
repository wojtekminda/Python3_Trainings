'''
Write a script which reads two files and writes their contents to the screen.
Corresponding lines from the files are printed on the same line, separated by a space character.
If one of the files is longer, its remaining lines are printed on their own.
Both file paths may be fixed and hard-coded in the script.
'''

import os.path

#Sciezka bezwzgledna
directory = 'E:\\Programowanie\\Python_szkolenie_2\\zadania_domowe\\5_Joining_text_columns_FILES\\'

# Pliki
file1 = 'column1.txt'
file2 = 'column2.txt'
file_merged = 'merged_1.txt'

# Listy
f1_list = list()
f2_list = list()
final_list = list()

# Pliki -> Listy
with open(directory + file1, 'r') as f1:
    for line in f1:
        line = line.strip()
        f1_list.append(line)
with open(directory + file2, 'r') as f2:
    for line in f2:
        line = line.strip()
        f2_list.append(line)

# Ustalenie dlugosci list
len1 = len(f1_list)
len2 = len(f2_list)
length = max(len1,len2)

# Utworzenie finalnej listy o odpowiednij dlugosci
i = 0
while i < length:
    final_list.append("")
    i = i + 1

# Odpowiednie uzupelnienie listy
i = 0
while i < len(final_list):
    if i < len1:
        final_list[i] = final_list[i] + f1_list[i] + " "
    if i < len2:
        final_list[i] = final_list[i] + f2_list[i]
    i = i + 1

# Zapis do pliku
with open(directory + file_merged, 'w') as fw:
    i = 0
    while i < len(final_list):
        fw.write(final_list[i])
        fw.write('\n')
        i = i + 1
