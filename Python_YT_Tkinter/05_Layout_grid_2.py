import tkinter as tk

root = tk.Tk()

root.title('Layout example - grid')

label1 = tk.Label(root, text='Name')
label2 = tk.Label(root, text='Password')
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
checkbox = tk.Checkbutton(root, text='Keep me logged in')

label1.grid(row=0, column=0, sticky='e')
label2.grid(row=1, column=0, sticky='e')
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
checkbox.grid(columnspan=2)

root.mainloop()
