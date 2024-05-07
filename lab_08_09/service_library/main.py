from GUI import main_app
import tkinter as tk


def main():
    root = tk.Tk()
    root.geometry('1500x1000')
    app = main_app.Application(root)
    return app


if __name__ == '__main__':
    app = main()
    app.mainloop()
