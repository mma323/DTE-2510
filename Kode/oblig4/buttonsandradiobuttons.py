#Programmet bruker buttons og radio buttons til å endre bakgrunnsfarge for 
#tekst i en GUI, samt flytte teksten til venstre og til høyre

import tkinter as tk

class Window:
    def __init__(self):
        self.colors = ["red", "yellow", "white", "gray", "green"]
        self.start_color = self.colors[0]
        self.color = self.start_color

        self.start_x_value = 30          #x-verdi kan endres av bruker
        self.x_value = self.start_x_value
        self.y_value = 25

        window = tk.Tk()

        frame = tk.Frame()
        frame.pack(side = tk.TOP)

        self.radio_button_control = tk.StringVar()
        self.radio_button_control.set(self.start_color)

        for color in self.colors:
            radio_button = tk.Radiobutton(frame, 
                            text = color,
                            variable = self.radio_button_control,
                            value = color,
                            command = lambda : self.change_color(color))
            radio_button.pack(side = tk.LEFT)
        
        self.canvas_width = 250
        self.canvas_height = 50
        self.canvas = tk.Canvas(window,
                                width  = self.canvas_width, 
                                height = self.canvas_height, 
                                bg     = self.color         )
        self.add_text()
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()

        button_right = tk.Button(frame, text="<=", command=self.move_left)
        button_right.grid(row=1, column=1)

        button_left = tk.Button(frame, text="=>", command=self.move_right)
        button_left.grid(row=1, column=2)

        window.mainloop()

    def change_color(self, color):
        self.canvas.delete("all")
        color = self.radio_button_control.get()
        self.color = color
        self.canvas.configure(bg = self.color)
        self.add_text()

    def move_right(self):
        max_x_value = self.canvas_width - self.text_width * (2 / 3)
        if self.x_value < max_x_value:
            self.canvas.delete("all")
            self.x_value += 2
            self.add_text()

    def move_left(self):
        if self.x_value > self.start_x_value:
            self.canvas.delete("all")
            self.x_value -= 2
            self.add_text()

    def add_text(self):
        self.text = self.canvas.create_text(self.x_value, 
                                            self.y_value, 
                                            text = "Welcome")
        self.text_coordinates = self.canvas.bbox(self.text)

        #canvas.bbox(self.text) returnerer koordinater på formen 
        #(start_x, start_y, slutt_x, slutt_y)
        self.text_width = self.text_coordinates[2] - self.text_coordinates[0]

Window()