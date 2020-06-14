from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import csv

root = tk.Tk()
root.title("State Facts")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=390, padx=330)

# Create a Tkinter variable
tkvar = StringVar(root)

# List for Drop Down
States = []
with open("./list_files/states.txt") as file:
    for line in file:
        line = line.strip()  # used for each line of the file to remove \n newline character that each line might have
        States.append(line)  # storing everything in memory

# Dictionaries with Data
# Import ratification file to dictionary
a = open('./list_files/ratification.csv', 'r')
reader = csv.reader(a)
Ratification = {}
for row in reader:
    Ratification[row[0]] = {row[1]}

# Import capitals file to dictionary
b = open('./list_files/capitals.csv', 'r')
reader = csv.reader(b)
Capital = {}
for row in reader:
    Capital[row[0]] = {row[1]}

# Import flag file to dictionary to set flag image
c = open('./list_files/flag.csv', 'r')
reader = csv.reader(c)
Flag = {}
for row in reader:
    Flag[row[0]] = {row[1]}

# Import nickname file to dictionary
d = open('./list_files/nickname.csv', 'r')
reader = csv.reader(d)
Nickname = {}
for row in reader:
    Nickname[row[0]] = {row[1]}

# Import state bird file to dictionary
e = open('./list_files/bird.csv', 'r')
reader = csv.reader(e)
Bird = {}
for row in reader:
    Bird[row[0]] = {row[1]}

# Import state flower file to dictionary
f = open('./list_files/flower.csv', 'r')
reader = csv.reader(f)
Flower = {}
for row in reader:
    Flower[row[0]] = {row[1]}

# Import state tree file to dictionary
g = open('./list_files/tree.csv', 'r')
reader = csv.reader(g)
Tree = {}
for row in reader:
    Tree[row[0]] = {row[1]}

# Import abbreviation file to dictionary
h = open('./list_files/abbreviation.csv', 'r')
reader = csv.reader(h)
Abbreviation = {}
for row in reader:
    Abbreviation[row[0]] = {row[1]}

tkvar.set("Choose State")  # set the default option
T = Text(root, height=10, width=60)  # Creation of textbox for facts
T.place(x=140, y=210)  # Position of textbox (Do not need to use .pack since it is placed)

# Setting initial flag image
result = (tkvar.get())
img = ImageTk.PhotoImage(Image.open("./images/usa.gif"))
imagebox = tk.Label(root, image=img)
imagebox.place(x=240, y=10)  # Position of textbox (Do not need to use .pack since it is placed)

# Setting of initial choice of drop down menu
popupMenu = OptionMenu(mainframe, tkvar, *States)
Label(mainframe, text="Choose a State").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


# function to clear contents of textbox
def clear_textbox():
    T.delete('1.0', END)


# function to change image when state is changed
def callback():
    result = (tkvar.get())
    img2 = ImageTk.PhotoImage(Image.open("./images/" + (str(Flag[result]).replace("{'", "").replace("'}", "")) + ".gif"))
    imagebox.configure(image=img2)
    imagebox.image = img2


# function to change data when state is changed
def change_dropdown(*args):
    clear_textbox()
    result = (tkvar.get())
    callback()
    T.insert(END,
             (str(Ratification[result]).replace("{'", "").replace("'}", ""))+"\n"
             + (str(Abbreviation[result]).replace("{'", "Abbreviation: ").replace("'}", "")) + "\n"
             +(str(Capital[result]).replace("{'", "Capital: ").replace("'}", ""))+"\n"
             +(str(Nickname[result]).replace("{'", "Nickname(s): ").replace("'}", ""))+"\n"
             + (str(Bird[result]).replace("{'", "State Bird: ").replace("'}", "")) + "\n"
             + (str(Flower[result]).replace("{'", "State Flower: ").replace("'}", "")) + "\n"
             + (str(Tree[result]).replace("{'", "State Tree: ").replace("'}", "")) + "\n"
             )


# link function to change dropdown
tkvar.trace('w', change_dropdown)
root.mainloop()