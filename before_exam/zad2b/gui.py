import tkinter as tk
import pandas as pd


def opertation(buget):
    movies = pd.read_csv('movies.csv')
    movies = movies[movies['budget'] < buget.get()]


def gui(root):
    root.geometry('400x400')
    buget = tk.Entry(root)
    buget.grid(row=1, column=0)
    tk.Label(root, text='Budzet filmu: ').grid(row=0, column=0)
    button = tk.Button(root, text='OK', command=lambda: opertation(buget))
    button.grid(row=1, column=1)
    text = tk.Label(root, text='')
    text.grid(row=2, column=0)
    return root
