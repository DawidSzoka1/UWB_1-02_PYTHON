import tkinter as tk


class AvailableBooks(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_frame = self
        self.main_frame.grid(row=0, column=0)
        self.main_frame.columnconfigure(0, weight=1)
        self.load_page()
        self.back_main_frame(parent)

    def back_main_frame(self, parent):
        self.button_back = tk.Button(self, text="Back", command=lambda: parent.show_frame(page=0))
        self.button_back.grid(row=1, column=1)

    def load_page(self):
        self.text_label = tk.Label(
            self.main_frame,
            bg="#08172B",
            text="TEST",
            fg="#CFCFA7",
            font=("Georgia pro", 80)
        )
        self.text_label.grid(row=0, column=0, padx=(0, 250), pady=(50, 0), columnspan=4)

