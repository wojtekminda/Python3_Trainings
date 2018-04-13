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
file_merged = 'merged_2.txt'

# Lista
line_list = list()

# Uzupelnienie listy -> file1
with open(directory + file1, 'r') as f:
    for line in f:
        line = line.strip()
        line_list.append(line)

# Uzupelnienie listy -> file2
with open(directory + file2, 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i < len(line_list):
            line_list[i] = line_list[i] + " " + line
        else:
            line_list.append(line)

# Zapis do pliku
with open(directory + file_merged, 'w') as f:
    for line in line_list:
        f.write(line)
        f.write('\n')
