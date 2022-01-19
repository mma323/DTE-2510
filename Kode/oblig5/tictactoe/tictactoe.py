#Enkelt TicTacToe GUI-program

import tkinter as tk

class Cell(tk.Label):
    def __init__(self, container):
        tk.Label.__init__(self, container, image = image_empty)
        self.bind("<Button-1>", self.turn)
        self.token = " "
      
    def turn(self, event):
        global current_token
        if self.token == " " and current_token != "Over":
            if current_token == "X":
                current_token = "O"
                self["image"] = image_x   
                self.token = "X"
            else:   
                current_token = "X"
                self["image"] = image_o   
                self.token = "O"
                
        check_status(self.token)

def check_status(token):
    global current_token
    if is_won(token):
        status_label["text"] = token + " won! The game is over"
        current_token = "Over"
    elif is_full():
        status_label["text"] = "Draw! The game is over"
        current_token = "Over"
        
def is_full():
    for i in range(3):
        for j in range(3):
            if cells[i][j].token == ' ':
                return False
    return True

def is_won(token):
    for i in range(AMOUNT_OF_ROWS):
        if cells[i][0].token == token and cells[i][1].token == token \
            and cells[i][2].token == token:
            return True

    for i in range(AMOUNT_OF_COLUMNS):
      if cells[0][i].token == token and cells[1][i].token == token \
          and cells[2][i].token == token:
        return True

    if cells[0][0].token == token and cells[1][1].token == token \
        and cells[2][2].token == token:
      return True

    if cells[0][2].token == token and cells[1][1].token == token \
        and cells[2][0].token == token:
      return True

    return False

window = tk.Tk() # Create a window
window.title("TicTacToe") # Set title
image_x = tk.PhotoImage(file = "x.gif")
image_o = tk.PhotoImage(file = "o.gif")
image_empty = tk.PhotoImage(file = "empty.gif")
current_token = "X"
    
frame = tk.Frame(window)
frame.pack()

cells = []
AMOUNT_OF_ROWS    = 3
AMOUNT_OF_COLUMNS = 3
for i in range(AMOUNT_OF_ROWS):     
    cells.append([])
    for j in range(AMOUNT_OF_COLUMNS):
        cells[i].append(Cell(frame))
        cells[i][j].grid(row = i, column = j)

status_label = tk.Label(window, text = " ")
status_label.pack()
window.mainloop() 