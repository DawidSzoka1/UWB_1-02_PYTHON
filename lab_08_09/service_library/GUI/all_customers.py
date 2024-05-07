import tkinter as tk


class Customers(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_frame = self
        self.main_frame.grid(row=0, column=0)
        self.main_frame.columnconfigure(0, weight=1)

