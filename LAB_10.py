from tkinter import *  # standard Python interface to the Tcl/Tk GUI toolkit
import requests  # package allows you to send HTTP requests
from PIL import Image, ImageTk

#################################################################################
## Window

# window = Tk()  # create the window
# window.title("GUI")  # tytuł okna
# window.geometry("200x100")  # window size in pixels
# window.mainloop()  # to run the Tkinter event loop

from tkinter.messagebox import showinfo, showerror, showwarning


################# Example - text edit, button, static text, radiobutton
# def callback():  # funkcja uruchamiana po wciśnieciu kontrolki radioButton
#       try:
#           if var.get() == 1:
#             result = int(entry1.get()) + int(entry2.get())
#           if var.get() == 2:
#             result = int(entry1.get()) - int(entry2.get())
#       except ValueError as e:
#           showerror("Box:", e)
#
#       txt = "Result: " + str(result)
#       text3.config(text=txt)  # ustawienie tekstu w kontrolce o nazwie etykieta_text3
#
# window = Tk()
# window.title("Calculator")
# window.geometry("400x200")
#
# # This Label widget implements a display box where you can place text or images.
# Label(window, text="Number x =  ").grid(row=1, column=1)
# Label(window, text="Number y =  ").grid(row=2, column=1)
#
# # The Entry widget is used to accept single-line text strings from a user.
# entry1 = Entry(window, fg='red')
# entry1.grid(row=1, column=2)
#
# entry2 = Entry(window, fg='blue')
# entry2.grid(row=2, column=2)
#
# # Radiobutton widget implements a multiple-choice button, which is a way to offer
# # many possible selections to the user and lets user choose only one of them.
# #
# # When a radiobutton is turned on by the user, its control variable
# # is set to its current value option (IntVar or StringVar).
# var = IntVar()  #
# Radiobutton(window, text=" + ", variable=var, value=1).grid(row=1, column=3)
# Radiobutton(window, text=" - ", variable=var, value=2).grid(row=2, column=3)
#
# text3 = Label(window, text="Result: 0")
# text3.grid(row=3, column=1)
#
# Button(window, text="Enter", command=callback, fg="red").grid(row=4, column=1)
# window.mainloop()
#
# ###################################################################################
# # ################# Example - suwak/slider
# def callfun1():
#   result = var1.get() + var2.get()
#   my_text = "A + B = " + str(result)
#   text3.config(text=my_text)
#
# window = Tk()
# window.geometry("150x400")
#
# Label(window, text="Parameter A", bg="green", fg="white").grid(row=1, column=1)
#
# var1 = IntVar()
# Scale(window, from_=0, to=100, variable=var1).grid(row=2, column=1)
#
# Label(window, text="Parameter B", bg="red", fg="white").grid(row=3, column=1)
#
# var2 = IntVar()
# Scale(window, from_=0, to=50, orient=HORIZONTAL, variable=var2).grid(row=4, column=1)
#
# Button(window, text="A + B", command=callfun1, fg="red").grid(row=5, column=1)
#
# text3 = Label(window, text=" ")
# text3.grid(row=6, column=1)
#
# window.mainloop()

# ############################################
# #### Example - Checkbox
# def callfun2():
#   if var1.get() == 1 and var2.get() == 0:
#     text.config(text="I like to receive gifts")
#
#   if var1.get() == 0 and var2.get() == 1:
#     text.config(text="I like to give gifts")
#
#   if var1.get() == 1 and var2.get() == 1:
#     text.config(text="I like to receive/give gifts")
#
# window = Tk()
# window.geometry("400x400")
#
# var1 = IntVar()
# Checkbutton(window,
#             text="I like to receive gifts",
#             variable=var1,
#             command=callfun2).grid(row=0, sticky=W)
# #  the sticky option specifies which side the widget should stick to and how to distribute any extra space within the cell that is not taken up by the widget at its original size.
# # sticky = W - left-align (wyrównaj do lewej)
#
# # Setting default value of a checkbutton
#
#
# var2 = IntVar()
# Checkbutton(window,
#             text="I like to give gifts",
#             variable=var2,
#             command=callfun2).grid(row=1, sticky=W)
# var2.set(1)
# text = Label(window, text="Result: ")
# text.grid(row=4, column=1)
#
# window.mainloop()
#
# ####################################################################
# ## Zapoznaj się z przykładami tworzenia okienek informacyjnych
# ## How we create a message box
#
# from tkinter.messagebox import showinfo, showerror, showwarning
# # ## Example - showinfo

# window = Tk()
# showinfo("ShowInfo", "Hello World!")
# window.mainloop()
# #
# window = Tk()
# Button(window, text = 'ok', command = lambda :showinfo("Box:", 'info')).grid(row = 1, column = 1)
# window.mainloop()
#
# ## Example - showerror
# # window = Tk()
# # Button(window, text = 'ok', command = lambda :showerror("Box:", 'error')).grid(row = 2, column = 1)
# # window.mainloop()
#
# ## Example - showwarning
# # window = Tk()
# # Button(window, text = 'ok', command = lambda :showwarning("Box:", 'warning')).grid(row = 3, column = 1)
# # window.mainloop()
#
# ###### Placing Widgets in Tk (tkinter)
# ###### Tk provides three methods to position widgets within a window,
# ####### which are represented in code by the grid(), place() and pack() functions.
#
# ## Relative Position (pack)
# ## pack geometry
# # # side − determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.
# window = Tk()
# window.geometry("100x300")
# Label(window, text="pack BOTTOM", bg="red", fg="white").pack(side=BOTTOM)
# Label(window, text="pack TOP", bg="blue", fg="white").pack(side=TOP)
# window.mainloop()
#
# ## ## pack geometry + Frame
# ## The Frame widget is very important for the process of grouping and organizing other widgets.
# ## It works like a container, which is responsible for arranging the position of other widgets.
#
# ## Absolute Position (place)
# ## place geometry
# # window = Tk()
# # Label(window, text="Position : x=10, y=20", bg="red", fg="white").place(x=10, y=20)
# # ## coordinate (x = 10,y = 30) of widget in window
# # mainloop()
#
# # window = Tk()
# # frame1 = Frame(window)
# # frame1.pack(side=TOP)
# # Label(frame1, text="pack 1", bg="red", fg="white").pack(side=LEFT)
# # Label(frame1, text="pack 2", bg="blue", fg="white").pack(side=LEFT)
# #
# # frame2 = Frame(window)
# # frame2.pack(side=TOP)
# # Label(frame2, text="pack3", bg="blue", fg="white").pack(side=TOP)
# # Label(frame2, text="pack4", bg="red", fg="white").pack(side=BOTTOM)
# # Label(frame2, text="pack5", bg="blue", fg="white").pack(side=RIGHT)
# # Label(frame2, text="pack6", bg="red", fg="white").pack(side=RIGHT)
# # window.mainloop()
#
# ################### Menu
# def callfun3():
#   filewin = Toplevel(window)
#   button = Button(filewin, text="Do nothing button")
#   button.pack()
#
# window = Tk()
# menubar = Menu(window)
# my_menu = Menu(menubar, tearoff=0)
#
# my_menu.add_command(label="New", command=callfun3)
# my_menu.add_command(label="Open", command=callfun3)
# my_menu.add_command(label="Save", command=callfun3)
# my_menu.add_separator()
# my_menu.add_command(label="Exit", command=window.quit)
#
# menubar.add_cascade(label="File", menu=my_menu)
# window.config(menu=menubar)
# window.mainloop()
# ##################################################################
# ### padx, ipadx, pady, and ipady, which specify (in pixels) a widget's external and internal margins. For example, in the following code there will be a 10px/20px space between the button and the window (external margin), but a 50px/100px space between the button border and its text (internal margin).
# ## margines zewnętrzny oś x (padx), oś y (pady),
# ## margines wewnetrzny oś x (ipadx), oś y (ipady)
#
# window = Tk()
# t = Label(window, text="Position", bg="red", fg="white")
# t.pack(padx=10, pady=20, ipadx=50, ipady=100, side=LEFT)
# window.mainloop()

## Window - background (tło)

# download example image
# url1 = 'https://www.druk-flag.pl/drukarnia-flag/wp-content/uploads/2019/05/4.jpeg'
# response = requests.get(url1, stream=True)
# if response.status_code == 200:
#     with open("sample.jpg", 'wb') as f:
#         f.write(response.content)
#
# window = Tk()
# window.geometry("500x500")
# canvas = Canvas(window)  # canvas widget to draw graphs or plots
# #  columnnspan - liczba kolumn którą obejmuje kontrolka
# #  How many columns widgetoccupies; default 1
# canvas.grid(columnspan=3)
# image = Image.open('sample.jpg')
# logo1 = ImageTk.PhotoImage(image)
#
# logo2 = Label(image=logo1)
# logo2.image = logo1
# logo2.grid(row=0, column=0, rowspan=100, columnspan=100)
#
# text = Label(window, text="Parameter A = ", fg="black", font='Raleway')
# text.grid(row=1, column=1)
# window.mainloop()

# # ############Zadanie 1 ######################
# # Kalkulator: utwórz 2 kontrolki typu edit tekst, 1 przycisk "ok" i radiobutton
# # po wcisnieciu przycisku program powinien wykonywać 4 dowolne operacje matematyczne na liczbach wpisanych przez użytkownika
# # w kontrolkach edit
# # Obsłuż potencjalne błędy wpisując własny komentarz: np. TypeError
# # Do wyswietlania komunikatów użyj okienek komunikacyjnych
window = Tk()

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
#
# # #########Zadanie 3
# # Pewna firma zleciła Ci wykonie badania ankietowego dotyczącego kupowanych przez konsumentów produktów na święta:
# # Do każdego pytania utwórz 2-3 kontrolki wielokrotnego wyboru z następującymi opcjami do wyboru.
# # np. Co najczęściej kupujesz dla rodziny w prezencie?
# # opcja 1: agd
# # opcja 2: kosmetyki
# # opcja 3: odzież