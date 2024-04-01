# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy

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
# list_names += new_list
# print(list_names)

######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

# dict_zad2 = {"imie": ["Dawid", "Ula", "Edward"], "nazwisko": ['1', '2', '3'], "wiek": [12, 13, 14]}
# number = int(input("Podaj liczba: "))
# print(f"Imie {dict_zad2['imie'][number]}, nazwisko: {dict_zad2['nazwisko'][number]}, wiek: {dict_zad2['wiek'][number]}")

######################Zadanie 3
# Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
# wskazana przez użytkownika

# dict_zad2['kierunek_studiów'] = []
# for i in range(3):
#     kierunek_studiow = input(f"Podaj kierunek studiow {i + 1} osoby: ")
#     dict_zad2['kierunek_studiów'].append(kierunek_studiow)


######################Zadanie 4
# Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów
# ###########################################
# print(f"KLucze {dict_zad2.keys()}\n ilosc elementow:")
# for v in dict_zad2.values():
#     print(f"{len(v)}: {v}")
##############  Zadania do wykonania
## 1. Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
# print(0 > 1)
# print(0 <= 1)
# print(0 >= 1)
# print(1 == 0)
# print(1 == 1)
# print(1 != 0)
# print(1 != 1)

## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)
# x = int(input("Enter a number x: "))
# y = int(input("Enter a number y: "))
# print(f"2x + 5y = {2*x + 5*y}")

## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
# a = input("Enter your name: ")
# b = input("Enter your last name: ")
# c = int(input("Enter your age: "))
# d = input("Enter what you are studying: ")
# print(f"Jestem {a} {b} mam {c} lat studiuję {d}")

## 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646
# print(
#     f"Czy liczba 1+2+10+20000001+4+347586970885 =  321784560456434534646:"
#     f" {1 + 2 + 10 + 20000001 + 4 + 347586970885 == 3217845604564346}"
# )
## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0
# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# print(f"Czy ich suma jest parzysta: {(num1 + num2 )% 2 == 0}")


## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
# x = int(input("Enter a number: "))
# y = int(input("Enter second number: "))
# print(f"x + y = {x + y}")
# print(f"x - y = {x - y}")
# print(f"x * y = {x * y}")
# print(f"x / y = {x / y}")
# print(f"x^y = {x ** y}")

## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
# x = int(input("Enter a number: "))
# if 1 < x < 13 and x != 5 or x < 0:
#     print("x miedzy 1 a 13 lub x != od 5 lub mniejszy od 0")

# Zadania dodatkowe:
# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.

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


# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.

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

# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie
# pary = ["be", "ce", "ći", "de", "ef", "gie", "ha", "jot", "ka", "el", "em", "en", "pe", "er", "es",
#         "te", "wu", "y", "zet", "żet", "źet"]
# spolgloska = input("Podaj spolgloske: ")
# for i in pary:
#     if spolgloska in i:
#         print(i)
#
# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna

# name = input("What is your name? ")
# if name == "Janusz":
#     print("Janusz")
# elif name == "Grazyna":
#     print("Grazyna")
# else:
#     print("ani janusz ani grazyna")
