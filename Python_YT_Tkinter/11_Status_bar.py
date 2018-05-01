import tkinter as tk

# --- Example function --- #
def doNothing():
    print('OK, nothing happened...')

# --- Main window --- #
root = tk.Tk()
root.title('Drop down menu')

# --- Drop down menu --- #
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

# --- Toolbar --- #
toolbar = tk.Frame(root, bg='blue')
toolbar.pack(side='top', fill='x')

insertButton = tk.Button(toolbar, text='Insert', command=doNothing)
insertButton.pack(side='left', padx=5, pady=5)
printButton = tk.Button(toolbar, text='Print', command=doNothing)
printButton.pack(side='left', padx=5, pady=5)

# --- Status bar --- #
statusBar = tk.Label(root, text='Preparing to do nothing...', bd=1, relief='sunken', anchor='w')
statusBar.pack(side='bottom', fill='x')

# --- Mainloop function --- #
root.mainloop()
