import tkinter as tk

root = tk.Tk()
root.title('Shapes and Graphics')

canvas = tk.Canvas(root, width=400, height=400, bg='green')
canvas.pack()

blackLine = canvas.create_line(0, 0, 400, 200)
redLine = canvas.create_line(0, 400, 400, 200, fill='red')
blueBox = canvas.create_rectangle(100, 100, 300, 300, fill='blue')
purpleCircle = canvas.create_oval(100, 100, 300, 300, fill='purple')

canvas.delete(redLine)
#canvas.delete('all')

root.mainloop()
