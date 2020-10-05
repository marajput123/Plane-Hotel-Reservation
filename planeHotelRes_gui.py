import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
two = ""
def addApp():
  two= "Two"
  label = tk.Label(frame, text=two)

# def showTwo():
#   label

canvas = tk.Canvas(root, height=500, width=700, bg="#333")
canvas.pack()

frame = tk.Frame(root, bg="#e76f51")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

getTwo = tk.Button(root, text="add two", padx=10, pady=5, fg='white', bg="grey", command=addApp)
getTwo.place(relwidth=0.4, relheight=0.1, relx=0.1, rely=.9)

showTwo = tk.Button(frame, text="show two", padx=10, pady=5, fg='white', bg="grey", command=addApp)
showTwo = tk.Button(frame, text="show two", padx=10, pady=5, fg='white', bg="grey", command=addApp)
root.mainloop()

