import tkinter as tk

root = tk.Tk()

root.title('Layout example - pack')

frameTop = tk.Frame(root)
frameBottom = tk.Frame(root)

frameTop.pack(side='top')
frameBottom.pack(side='bottom')

button1 = tk.Button(frameTop, text='Button 1', fg='red')
button2 = tk.Button(frameTop, text='Button 2', fg='green')
button3 = tk.Button(frameTop, text='Button 3', fg='blue')
button4 = tk.Button(frameBottom, text='Button 4', fg='purple')

button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack()

root.mainloop()
