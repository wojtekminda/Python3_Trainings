import tkinter as tk

def printName():
    print('Hello Wojtek!')

def printSurname(event):
    print('Hello Minda!')

root = tk.Tk()

root.title('Binding functions to widgets')

button1 = tk.Button(root, text='Print my name', command=printName)
button1.pack()

button2 = tk.Button(root, text='Print my surname')
button2.bind('<Button-1>', printSurname)
button2.pack()

root.mainloop()
