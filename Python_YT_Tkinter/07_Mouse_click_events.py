import tkinter as tk

def leftClick(event):
    print('LEFT!')

def middleClick(event):
    print('MIDDLE!')

def rightClick(event):
    print('RIGHT!')

root = tk.Tk()

root.title('Mouse click events')

frame = tk.Frame(root, width=300, height=300, bg='green')
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
