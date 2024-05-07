import tkinter as tk


class Application(tk.Frame):
    def __init__(self, root):
        self.bg_color_1 = '#08172B'
        self.bg_color_2 = 'black'
        self.font_color_1 = '#CFCFA7'
        self.font_color_2 = 'white'
        self.font_style = "Georgia pro"

        super().__init__(root, bg=self.bg_color_1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_frame_list()
        self.create_pager()

    def create_frame_list(self):
        frame_list = tk.Frame(self.main_frame, background=self.bg_color_1)
        frame_list.columnconfigure(0, weight=1)
        frame_list.rowconfigure(0, weight=1)
        frame_list.grid(row=0, column=0, sticky='nsew')
        text_container = tk.Label(frame_list, text="Hello World!", background=self.font_color_1)
        text_container.grid(row=0, column=0)

    def create_frame_actions(self):
        pass

    def create_pager(self):
        pass


root = tk.Tk()
root.geometry('1500x1000')
app = Application(root)
root.mainloop()
