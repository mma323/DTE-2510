#Et GUI program der brukeren kan flytte en ball ved hjelp av buttons i et panel

import tkinter as tk

class Panel:
    def __init__(self):
        X_1 = 100
        Y_1 = 100
        X_2 = 150
        Y_2 = 150
        window = tk.Tk()
        self.canvas = tk.Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(X_1, Y_1, X_2, Y_2, fill="red")
        frame = tk.Frame(window)

        button_left = tk.Button(frame, text="Left", command=self.move_left)
        button_right = tk.Button(frame, text="Right", command=self.move_right)
        button_up = tk.Button(frame, text="Up", command=self.move_up)
        button_down= tk.Button(frame, text="Down", command=self.move_down)

        button_left.grid(row=1, column=1)
        button_right.grid(row=1, column=2)
        button_up.grid(row=1, column=3)
        button_down.grid(row=1, column=4)

        frame.pack()

        window.mainloop()

    def move_left(self):
        x_1, y_1, x_2, y_2 = self.canvas.coords(self.ball)
        if x_1 > 0:
            self.canvas.move(self.ball, -5, 0)

    def move_right(self):
        x_1, y_1, x_2, y_2 = self.canvas.coords(self.ball)
        if x_1 < 450:
            self.canvas.move(self.ball, 5, 0) 

    def move_up(self):
        x_1, y_1, x_2, y_2 = self.canvas.coords(self.ball)
        if y_1 > 0:
            self.canvas.move(self.ball, 0, -5)

    def move_down(self):
        x_1, y_1, x_2, y_2 = self.canvas.coords(self.ball)
        if y_1 < 450:
            self.canvas.move(self.ball, 0, 5)

Panel()