# # zad 1
# list_names = ["dawid", "dawid", "dawid", "lukasz", "kuba", "seba", "edek", "ula", "franciszek", 'elzbieta']
# name = input("Enter your name: ")
#
# indeks = list_names.index(name)
# amount = list_names.count(name)
# list_names.append("Mieszko")
# list_names.insert(2, "Marek")
# list_names.sort()
# list_names.pop()
# new_list = ["Mieszko", "Marek", "Pazdan"]
# list_names = list_names + new_list
#
#
# # sprawdzenie
# print(0 > 1)
# print(0 <= 1)
# print(0 >= 1)
# print(1 == 0)
# print(1 == 1)
# print(1 != 0)
# print(1 != 1)

# # zad 2
# x = int(input("Enter a number x: "))
# y = int(input("Enter a number y: "))
# print(f"2x + 5y = {2*x + 5*y}")

# # zad 3
# a = input("Enter your name: ")
# b = input("Enter your last name: ")
# c = input("Enter your age: ")
# d = input("Enter what you are studying: ")
# print(f"Jestem {a} {b} mam {c} lat studiuję {d}")

# # zad 4
# print(
#     f"Czy liczba 1+2+10+20000001+4+347586970885 =  321784560456434534646:"
#     f" {1 + 2 + 10 + 20000001 + 4 + 347586970885 == 3217845604564346}"
# )
# # zad 5
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# print(f"Czy ich suma jest parzysta: {(num1 + num2 )% 2 == 0}")

# # zad 6
# x = int(input("Enter a number: "))
# y = int(input("Enter second number: "))
# print(f"x + y = {x + y}")
# print(f"x - y = {x - y}")
# print(f"x * y = {x * y}")
# print(f"x / y = {x / y}")
# print(f"x^y = {x ** y}")

# # zad 7
# x = int(input("Enter a number: "))
# if 1 < x < 13:
#     print("x miedzy 1 a 13")
# elif x != 5 or x < 0:
#     print("x != od 5 lub mniejszy od 0")

# # zad dodatkowe:
# # zad 1
# name = input("What is your name? ")
# surname = input("What is your surname? ")
# age = input("What is your age? ")
# eat = input("Do you eat well? ")
# sport = input("Do you like sport? ")
# games = input("Do you like games? ")
# books = input("Do you like reading books? ")
# art = input("Do you have an interest in art?: ")
# print("Podsumowanie \n")
# print(f"Imie: {name} \nSurname: {surname} \nWiek: {age} \nDo you eat well: {eat}"
#       f"\nDo you like sport: {sport} \nDo you like games: {games} \nDo you like reading books: {books}"
#       f"\nDo you have an interest in art: {art} ")


# # zad 2
# name = input("What is your name? ")
# surname = input("What is your surname? ")
# age = input("What is your age? ")
# job = input("What is your job? ")
# place_of_birth = input("Where were you born? ")
# hobby = input("What are your hobbies? ")
# print(f"Jestem {name} {surname}, mam {age} lat. Zawodowo pracuję jako {job}.")
# print(f"Urodziłem się w miejscowości {place_of_birth}.")
# print(f"W wolnym czasie lubię {hobby}.")
# print("To jest mój krótki życiorys.")

# zad 3
pary = ["be", "ce", "ći", "de", "ef", "gie", "ha", "jot", "ka", "el", "em", "en", "pe", "er", "es",
        "te", "wu", "y", "zet", "żet", "źet"]
spolgloska = input("Podaj spolgloske: ")
for i in pary:
    if spolgloska in i:
        print(i)

# zad 4
name = input("What is your name? ")
if name == "Janusz":
    print("Janusz")
elif name == "Grazyna":
    print("Grazyna")
else:
    print("ani janusz ani grazyna")
