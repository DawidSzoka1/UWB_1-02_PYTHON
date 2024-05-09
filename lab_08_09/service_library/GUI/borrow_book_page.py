import tkinter as tk

from lab_08_09.service_library.GUI.usefullfun import back_to_home_page


class BorrowBookPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.frame_label = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1000,
            height=150
        )
        self.frame_label.grid(row=0, column=0, sticky='nsew')
        self.frame_label.grid_propagate(False)

        self.send_frame = tk.Frame(
            self,
            bg=self.parent.bg_color_2,
            width=500,
            height=1000
        )
        self.send_frame.grid(row=0, column=1, sticky='nsew', rowspan=2)

        self.entry_frame = tk.Frame(
            self,
            bg=self.parent.bg_color_1,
            width=1000,
            height=900
        )
        self.entry_frame.grid(row=1, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.load_widgets()

    def load_widgets(self):
        back_to_home_page(self.frame_label, self.parent.show_frame, self.parent.font_color_1)
        self.create_label()
        self.create_send_button()
        self.create_entry()

    def create_label(self):
        pass

    def create_send_button(self):
        pass

    def create_entry(self):
        pass
