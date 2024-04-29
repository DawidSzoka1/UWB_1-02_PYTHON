from customerservice import *
from rejestbook import *
import tkinter as tk

root = tk.Tk()
root.title("Service Library")
root.geometry("1000x500")
root.configure(background="black")
label = tk.Label(root, text="Hello, World!", fg="white", bg='black')
label.pack()


def main():
    pass


if __name__ == '__main__':
    root.mainloop()
    main()
