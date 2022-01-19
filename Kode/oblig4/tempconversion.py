#Et GUI program der brukeren kan gi en temperatur i celsius som input og få 
#den tilsvarende temperaturen returnert i fahrenheit 

import tkinter as tk

class Window:
    def __init__(self):
        
        root=tk.Tk()

        entry_label = tk.Label(root,text="Celcius temperature: ")
        entry_label.pack(side = tk.TOP)

        button_convert = tk.Button(root, 
                                   text = "Convert", 
                                   command = self.celsius_to_fahrenheit)
        button_convert.pack(side = tk.RIGHT)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

        root.mainloop()

    def celsius_to_fahrenheit(self):
        celsius = float(self.entry.get())
        fahrenheit = celsius * (9 / 5) + 32
        self.output_label.configure(text = (f"{fahrenheit} fahrenheit") )

Window()