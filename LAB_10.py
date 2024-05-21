from tkinter import *  # standard Python interface to the Tcl/Tk GUI toolkit
from tkinter.messagebox import showinfo, showerror, showwarning
import requests  # package allows you to send HTTP requests
from PIL import Image, ImageTk

# # ############Zadanie 1 ######################
# # Kalkulator: utwórz 2 kontrolki typu edit tekst, 1 przycisk "ok" i radiobutton
# # po wcisnieciu przycisku program powinien wykonywać 4 dowolne operacje matematyczne na liczbach wpisanych przez użytkownika
# # w kontrolkach edit
# # Obsłuż potencjalne błędy wpisując własny komentarz: np. TypeError
# # Do wyswietlania komunikatów użyj okienek komunikacyjnych
# def operation():
#     try:
#         num1 = float(a.get())
#         num2 = float(b.get())
#         num1 / num2
#     except ValueError:
#         showerror('Wrong input', 'Please enter valid numbers')
#         return 0
#     except ZeroDivisionError:
#         showerror('Wrong input', 'cant divide by 0')
#         return 0
#
#     if var.get() == 1:
#         result_operation = f'{num1 + num2}'
#     elif var.get() == 2:
#         result_operation = f'{num1 - num2}'
#     elif var.get() == 3:
#         result_operation = f'{num1 * num2}'
#     elif var.get() == 4:
#         result_operation = f'{num1 / num2}'
#     else:
#         return 0
#     result.config(text=result_operation)
#
#
# window = Tk()
# window.geometry("500x500")
# a = Entry(window)
# a.grid(row=0, column=0)
# b = Entry(window)
# b.grid(row=1, column=0)
# button = Button(window, text='ok', command=operation)
# button.grid(row=2, column=0)
# var = IntVar()
# Radiobutton(window, text='+', variable=var, value=1).grid(row=0, column=1)
# Radiobutton(window, text='-', variable=var, value=2).grid(row=1, column=1)
# Radiobutton(window, text='*', variable=var, value=3).grid(row=2, column=1)
# Radiobutton(window, text='/', variable=var, value=4).grid(row=3, column=1)
# result = Label(window, text='')
# result.grid(row=3, column=0)
#
# window.mainloop()
# # ########## Zadanie 2
# # Okres świąt to również zwiększony czas brania kredytów przez konsumentów
# # Zaprojektuj prosty interfejs który obliczy ratę kredytu 1000-10000zł zgodnie ze wzorem:
# # rata =(K*q^n*(1-q))/(1-q^n) gdzie: q = 1+p/100
# # K - kwota udzielonego kredytu
# # n - liczba okresów  (n=1,2,3) np. mc
# # p - stopa procentowa (p=const, wpisz jako ułamek)
# # Uwaga jak wiadomo emocje można wyrazić za pomocą kolorów
# # A zatem postaraj się uzależnić kolor wyświetlanej kwoty raty do spłaty od potencjalnych emocji klienta banku na
# # widok ile musi oddać bankowi.
def calculate():
    q = (1+float(p.get())) / 100
    rata = round((float(k.get())*q**int(n.get())*(1-q))/(1-q**int(n.get())), 2)
    result.config(text=f'rata wynosi {rata}')

root = Tk()
root.geometry("500x500")
Label(root, text="Kwoata kredytu").grid(row=0, column=0)
k = Entry(root)
k.grid(row=1, column=0)
Label(root, text="Liczba okresowe").grid(row=2, column=0)
n = Entry(root)
n.grid(row=3, column=0)
Label(root, text="Stopa procentowa").grid(row=4, column=0)
p = Entry(root)
p.grid(row=5, column=0)
Button(root, text='oblicz', command=calculate).grid(row=6, column=0)
result = Label(root, text="")
result.grid(row=7, column=0)
root.mainloop()
#
# # #########Zadanie 3
# # Pewna firma zleciła Ci wykonie badania ankietowego dotyczącego kupowanych przez konsumentów produktów na święta:
# # Do każdego pytania utwórz 2-3 kontrolki wielokrotnego wyboru z następującymi opcjami do wyboru.
# # np. Co najczęściej kupujesz dla rodziny w prezencie?
# # opcja 1: agd
# # opcja 2: kosmetyki
# # opcja 3: odzież