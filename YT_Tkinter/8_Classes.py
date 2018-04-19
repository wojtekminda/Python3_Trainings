import tkinter as tk

class MyButtons:

    def __init__(self, master):

        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text='Print message', command=self.printMessage)
        self.printButton.pack()

        self.quitButton = tk.Button(frame, text='Quit', command=master.quit)
        self.quitButton.pack()

    def printMessage(self):
        print('WOW! It worked!')

root = tk.Tk()
root.title('Classes')
b = MyButtons(root)
root.mainloop()
