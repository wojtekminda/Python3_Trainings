import tkinter as tk
import tkinter.messagebox as tkmb

root = tk.Tk()
root.title('Messagebox')

answer = tkmb.askquestion('Question', 'Do you like me?')

if answer == 'yes':
    tkmb.showinfo('Answer', 'It is very nice :]')
else:
    tkmb.showinfo('Answer', 'Why?')

root.mainloop()
