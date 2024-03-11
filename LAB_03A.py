# # ################################ Task 1
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))
while x and y:
    print(x*y)
    x = int(input("Enter a number x: "))
    y = int(input("Enter a number y: "))

## # ################################ Task 2
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)
password = ('Tajne haslo', '1234')
check = input("Enter a passowrd: ")
if check in password:
    print('DS')
else:
    print("zle haslo")
