# jos saa, keskimmäinen ruutu pitää olla vaikea
import json
import random
from random import randrange, seed
import time
from tkinter import *

# Open and read the JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
options = data['options']

seed(time.time())

# Create a 5x5 table filled with zeros
table = [[0 for _ in range(5)] for _ in range(5)]

# create root window
root = Tk()
# root window title and dimension
root.title("R6S Bingo Randomizer")
# Set geometry (widthxheight)
root.geometry('1080x850')
# all widgets will be here

# adding a label to the root window
lbl = Label(root, text = "Create your bingo board")
lbl.grid()

# function to display text when
# button is clicked
def clicked():
    createBingoBoard()

# button widget with red color text
# inside
btn = Button(root, text = "Randomize" ,
             fg = "black", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

def createBingoBoard():
    # Shuffle the options list to randomize the order
    shuffled_options = options.copy()  # Make a copy to avoid modifying the original list
    random.shuffle(shuffled_options)
    
    # Add data to table and place in the grid
    option_index = 0  # Index to keep track of where in the shuffled options list we are

    # Add data to table
    for i in range(5):
        for j in range(5):
            table[i][j] = shuffled_options[option_index]  # Get the next unique option
            option_index += 1
            # Create a label for each grid cell and place it with the grid method
            board = Label(root, text=table[i][j], borderwidth=1, relief="solid", width=30, height=10)
            board.grid(row=i + 1, column=j)  # Start from row=1 to avoid overlapping the button/label at (0, 0)

    # Print the table
    for row in table:
        print(row)


# Execute Tkinter
root.mainloop()