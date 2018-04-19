import tkinter as tk

root = tk.Tk()

root.title('Layout example - pack')

label1 = tk.Label(root, text='Label 1', fg='red', bg='yellow')
label2 = tk.Label(root, text='Label 2', fg='green', bg='black')
label3 = tk.Label(root, text='Label 3', fg='blue', bg='white')

label1.pack()
label2.pack(fill='x')
label3.pack(side='left', fill='y')

root.mainloop()
