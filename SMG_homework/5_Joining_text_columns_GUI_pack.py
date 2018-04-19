'''
Write a script which reads two files and writes their contents to the screen.
Corresponding lines from the files are printed on the same line, separated by a space character.
If one of the files is longer, its remaining lines are printed on their own.
Both file paths may be fixed and hard-coded in the script.
'''

from tkinter import *

#Sciezka wzgledna
directory = '.\\5_Joining_text_columns_FILES\\'

# Pliki
file1 = 'column1.txt'
file2 = 'column2.txt'
file_merged = 'merged_GUI_pack.txt'

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
    for i, line in enumerate(line_list):
        f.write(line)
        if i < len(line_list)-1:
            f.write('\n')

### GUI ###
with open(directory + file1, 'r') as f:
    data1 = f.read()

with open(directory + file2, 'r') as f:
    data2 = f.read()

with open(directory + file_merged, 'r') as f:
    data3 = f.read()

root = Tk()
root.title("Merger")

left_frame = Frame(root)
center_frame = Frame(root)
right_frame = Frame(root)

w1 = Label(left_frame, text = "Column 1", fg = "red")
w2 = Label(left_frame, text = data1)

w3 = Label(center_frame, text = "Column 2", fg = "red")
w4 = Label(center_frame, text = data2)

w5 = Label(right_frame, text = "Merged columns", fg = "red")
w6 = Label(right_frame, text = data3)

left_frame.pack(side=LEFT)
center_frame.pack(side=LEFT)
right_frame.pack(side=LEFT)

w1.pack()
w2.pack()
w3.pack()
w4.pack()
w5.pack()
w6.pack()

root.mainloop()
