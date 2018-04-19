import tkinter as tk

def doNothing():
    print('OK, nothing happened...')

root = tk.Tk()

root.title('Drop down menu')

mainMenu = tk.Menu(root)
root.config(menu=mainMenu)

fileMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Open', command=doNothing)
fileMenu.add_command(label='Save', command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)

editMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)
editMenu.add_command(label='Paste', command=doNothing)

root.mainloop()
