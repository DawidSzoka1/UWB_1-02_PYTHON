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
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

name = ['d', 'a', 'w', 'i', 'd']
join_lambda = lambda name: ''.join(name)
