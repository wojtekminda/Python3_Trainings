'''
Write a script which reads two files and writes their contents to the screen.
Corresponding lines from the files are printed on the same line, separated by a space character.
If one of the files is longer, its remaining lines are printed on their own.
Both file paths may be fixed and hard-coded in the script.
'''

# Modules
from tkinter import *
from tkinter import messagebox

# Path
directory = '.\\5_Joining_text_columns_FILES\\'

# Files
file1 = 'column1.txt'
file2 = 'column2.txt'
file_merged = 'merged_GUI_grid.txt'

# After "Merge!" button click
def ButtonMerge():
    # List
    line_list = list()

    # Filling the list -> file1
    with open(directory + file1, 'r') as f:
        for line in f:
            line = line.strip()
            line_list.append(line)

    # Filling the list -> file2
    with open(directory + file2, 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i < len(line_list):
                line_list[i] = line_list[i] + " " + line
            else:
                line_list.append(line)

    # Writing to a file
    with open(directory + file_merged, 'w') as f:
        for i, line in enumerate(line_list):
            f.write(line)
            if i < len(line_list)-1:
                f.write('\n')

    with open(directory + file_merged, 'r') as f:
        data3 = f.read()

    w6 = Label(root, text = "Merged columns", fg = "red")
    w7 = Label(root, text = data3)

    w6.grid(row=0, column = 2)
    w7.grid(row=1, column = 2, sticky=N)

    messagebox.showinfo('Info', 'Created file -> \'merged_GUI_grid.txt\'')

### GUI ###
with open(directory + file1, 'r') as f:
    data1 = f.read()

with open(directory + file2, 'r') as f:
    data2 = f.read()

root = Tk()
root.title("Merger")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.destroy)

w1 = Label(root, text="Column 1", fg = "red")
w2 = Label(root, text=data1)

w3 = Label(root, text="Column 2", fg = "red")
w4 = Label(root, text=data2)

w5 = Button(root, text="Merge!", width=35, command=ButtonMerge)

w1.grid(row=0, column=0)
w3.grid(row=0, column=1)

w2.grid(row=1, column=0, sticky=N)
w4.grid(row=1, column=1, sticky=N)

w5.grid(row=3, columnspan=2)

root.mainloop()
