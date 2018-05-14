import tkinter as tk

root = tk.Tk()
root.title('Images and Icons')

photo = tk.PhotoImage(file='logo.png')
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
