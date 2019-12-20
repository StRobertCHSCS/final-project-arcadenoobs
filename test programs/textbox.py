import tkinter as tk

root= tk.Tk()

can = tk.Canvas(root, width = 800, height = 600)
can.pack()

entry1 = tk.Entry (root) 
can.create_window(400, 300, window=entry1)

def getSquareRoot ():  
    x1 = entry1.get()
    
    label1 = tk.Label(root, text= float(x1)**0.5)
    can.create_window(400, 250, window=label1)
    
button1 = tk.Button(text='What is your name', command=getSquareRoot)
can.create_window(400, 350, window=button1)

root.mainloop()