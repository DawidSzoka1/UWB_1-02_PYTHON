# # ################################ Task 1
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
# x = int(input("Enter a number x: "))
# y = int(input("Enter a number y: "))
# while x and y:
#     print(x*y)
#     x = int(input("Enter a number x: "))
#     y = int(input("Enter a number y: "))

## # ################################ Task 2
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)
# password = ('Tajne haslo', '1234')
# check = input("Enter a passowrd: ")
# if check in password:
#     print('DS')
# else:
#     print("wrong password")

################################## Task 3
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.
# import random
#
# numbers = random.sample(range(100000), 100)
# odd_numbers = sorted(list(filter(lambda n: n % 2 != 0, numbers)))

############### Task 4
## Uprość kod z Zadania 2 korzystając w w/w struktur
## Simplify the code from Task 2 using a one line if/else statement
# password = ('Tajne haslo', '1234')
# check = input("Enter a passowrd: ")
# print("ds") if check in password else print("Wrong password")


#################### Task 5
## Write a function that calculates the quotient of 3 even numbers
## Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"

# quotient = lambda x, y, z: x/y/z

# ########################## Task 6
# # Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# # z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

# name = ['d', 'a', 'w', 'i', 'd']
# join_lambda = lambda name: ''.join(name)

# ########################## Task  7
# # Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# # z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# # użyj funkcji list i metody split - dla zmiennych typu string

# full_name = 'Tomasz Kowalski'
# separate = lambda name: list(name.replace(" ", ''))
# print(separate(full_name))


# ########################## Task 8
# # Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# # znajdzie dowolną literę (2 argument funkcji)
## użyj lammbda()

# find_in_text = lambda text, word: text.find(word)

# ########################## Task 9
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).

# logins = []
# passwords = []
# while True:
#     login = input("Enter a login: ")
#     password = input("Enter a password: ")
#     if login.lower() == 'stop' or password.lower() == 'stop':
#         break
#     if login in logins:
#         continue
#     if password in passwords:
#         continue
#     logins.append(login)
#     passwords.append(password)
# dict_log_pass = dict(zip(logins, passwords))
#
# ########################## Task 10  - Module in Python
# # #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # #Utwórz funkcje Pion: która rysuje gwiazdeki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # obie funkcje są z modułu o nazwie stars
# # Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L
# from stars import Pion, Poziom
#
# Poziom(3)
# Pion(2)
# Poziom(3)
# Pion(2)
# Poziom(3)
# print("\n")
# Pion(6)
# Poziom(3)


# ########################## Task 11
# # utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)
# from sil import silnia
#
# number_1 = float(input("Enter a number: "))
# number_2 = float(input("Enter a number: "))
# print(f"{number_1}!  = {silnia(number_1)}\n")
# print(f"{number_2}!  = {silnia(number_2)}\n")
# ########################## Task 12
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# numbers = [x for x in range(1, 100)]
# numbers_filter = list(filter(lambda x: True if x % 2 == 0 else False, numbers))
# print(numbers_filter)

# ########################## Task 13
#### Write a script, using reduce(), which will multiply elements in range (1, 100)
# import functools
#
# number = functools.reduce(lambda x, y: x * y, [x for x in range(1, 100)])
# ########################## Task 14
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)

# numbers_filtered = list(filter(lambda number: True if number % 7 == 0 and number % 5 != 0 else False, [x for x in range(2000, 3201)]))
# print(numbers_filtered)
