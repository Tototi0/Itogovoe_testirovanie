from tkinter import*
import random
def click():
    a = random.randint(1, 3)
    canvas.delete(ALL)
    if a == 1:
        x1 = random.randint(110, 450)
        y1 = random.randint(110, 450)
        x2 = x1 - 90
        y2 = y1 - 90
        canvas.create_oval(x1, y1, x2, y2, fill = 'blue', outline = 'white')
    elif a == 2:
        x1 = random.randint(110, 450)
        y1 = random.randint(110, 450)
        x2 = x1 - 100
        y2 = y1 - 100
        canvas.create_rectangle(x1, y1, x2, y2, fill = 'purple', outline = 'white')
    else:
        x1 = random.randint(110, 450)
        y1 = random.randint(110, 450)
        x2 = random.randint(110, 450)
        y2 = random.randint(110, 450)
        x3 = random.randint(110, 450)
        y3 = random.randint(110, 450)
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = 'red')
root = Tk()
root.geometry('500x500')
root.resizable(False, False)
canvas = Canvas(root, width = 500, height = 500, bg = 'white')
button = Button(text = 'click', command = click, width = 9)
button.pack()
canvas.pack()
root.mainloop()
