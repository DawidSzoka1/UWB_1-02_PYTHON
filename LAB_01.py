## Język python jest językiem wysokiego poziomu, typowanie danych w Pythonie jest dynamiczne (interpreter sam rozpoznaje typ zmiennej na podstawie jej wartości)
## You should always use camelCase for class names, snake_case for everything else in Python (you could to use UPPER_CASE_SNAKE for constants).
############ Zmienne; typ prosty (klasy): string, integer, float,double, bool ###############
# print('Hello world')

# var_string = 'mercedes'
# print(type(var_string)) # funkcja type sprawdzenie typu zmiennej

# var_bool = True
# print(type(var_bool))

# var_integer = 1
# print(type(var_integer))

# var_float = 2.2324234
# print(type(var_float))

# var_float = 2.2324234
# print(type(var_float))

#### przypisanie wielu wartości do wielu zmiennych
# a, b, c = 1, 2, 1+2
# print(a,b,c)
# print('a = ', a, '; b = ', b, '; c =', c)
# print('a = ' + str(a) + ', b = ' + str(b) + ', c =' + str (c))   # str - konwersja zmiennej na typ string
# print('a = {}; b = {}; c = {}'.format(a,b,c))
# print('zmienna %s \n2 jako float: %f' % ('a', a))  # \n2 - newline
# print('zmienna %s jako int: %i' % ('a', a))
# print('zmienna %s jako float: %.2f' % ('a', a))  # 2f - zaokrąglij do 2 miejsc po przecinku
# print('zmienna %s jako int: %i' % ('a', a))
########################### Importowanie pakietów/bibliotek w Python
# Sposób 1
# import math   # importuje wszystkie funkcje i metody dostępne w bibliotece math
# x = 30*math.pi/180
# print(math.sin(x))

# Sposób 2
# from math import pi, sin
# x = 30*pi/180
# print('30*pi/180 =', sin(x))

############ strukturalny vs funkcyjny
## Oblicz pierwiastek z liczby 4
# p1 = 4**(1/2)  # paradygmat programowania strukturalnego
# print(p1)
#
# # from math import sqrt
# import math
# p2 = math.sqrt(4) # paradygmat programowania funkcyjnego
# print(p2)

## Komunikacja z użytkownikiem, wczytanie danych z konsoli
# name = input('Podaj imię: ')
# print(name)
# age = int(input('Podaj wiek: '))   # int - konwersja typu zmiennej string (str, łańcuch) na integer (int, liczba całkowita)
# print(name + ' ' + str(age))    # str - konwersja typu zmiennej str na int
#
# print("Twoje imię to: {} masz {} lat.".format(name, age))

###### Zmienne; typy złożone
# W Pythonie nie ma tablic
# # ################## Lista  ####################
# Tworzenie listy i odwoływanie się do jej elementów
# list_empty1 = list()  # pusta lista
# list_empty2 = []      # też pusta lista
# list1 = ['Informatyka', 1, True]  # to jest lista o nazwie cars
# print(list1)
# print(list1[0]) # uwaga numeracja wektora/listy itd. jest od 0
# print(list1[2]) # tu element nr 3 listy
########################### metody dla klasy lista ##########################
####### metody (okreslone operacje) wykonujemy na obiektach, obiektem może być np. nasza zmienna
# # # Zapoznaj się z kilkoma poniższymi podstawowymi i użytecznymi metodami dla list
# # # append(x) - Dodaje element do końca listy,
# # # extend(L) rozszerza listę poprzez dołączenie wszystkich elementów podanej listy L,
# # # insert(i, x) - umieszcza element x na podaną pozycję listy i, np. nazwaLista.insert(0,'Ala')
# # # remove(x) - usuwa pierwszy napotkany element z listy, którego wartością jest x.
# # # pop([i]) - usuwa element z podanej pozycji na liście i zwraca go jako wynik.
# # # index(x) - zwraca indeks pierwszego elementu listy, którego wartością jest x, np. cars.index('BMW')
# # # count(x) - zwraca liczbę wystąpień elementu x na liście.
# # # sort() - sortuje elementy na liście, w niej samej
# # # reverse() - odwraca porządek elementów listy.
##########################################################################
# # # Zapoznaj się przykładami zastosowania w/w metod ###############################################
# cars = ['Audi', 'BMW', 'Mercedes','BMW', 'BMW']
# print(cars)
# cars.append('Porsche') # na obiekcie o nazwie cars wywołana została metoda o nazwie append
# print(cars)

#cars = ['Audi', 'BMW', 'Mercedes','BMW']
# print(cars)
# cars.insert(2,'Porsche')
# cars2 = cars
# print(cars2)

#######  Użycie metody index na obiekcie cars, sprawdzamy index elementu listy
# cars = ['Audi', 'BMW', 'Mercedes','BMW']
# print(cars)
# ind = cars.index('BMW') # na obiekcie cars stosujemy metodę index, 1-sza pozycja elementu
# print(ind)
# ind2 = cars.count('BMW') # na obiekcie cars stosujemy metodę count liczba wystąpień elementu
# print(ind2)

# # Usuwanie wybranego elementu z listy
# numbers = [1, 2, 3, 10, 18, 10, 13, 10]
# print(numbers)
# numbers.remove(10)
# print(numbers)

### Łączenie list
# list1 = ["Ala", "Zosia"]
# list2 = ["Janek", "Tomek"]
# merge_list = list1 + list2
# print(merge_list)
#
# #Zadanie 1
# Utwórz listę z imionami (conajmniej 10 imion, część powinna się powtarzać)
# określ indeks (numer wiersza) w której znajduje się imie osoby, nazwę osoby podaje użytkownik
# ile osób o imieniu wskazanym przez użytkownika znajduje się na liście
# dołącz nowe imie do listy do końca listy
# dołącz nowe imię jako 3 pozycję na liście
# posortuj obiekty w liście, usuń ostatni element z listy
# utwórz nową listę z 3 imionami i dołącz do listy


# # ################# Klasa: Krotka (Tuple)
# print('To moja pierwsza krotka')
# cars2 = ('A', 'B')  # krotka = tuple
# print(cars2)
# #cars2.append('aaaaa')   # w krotce nie mogę zmieniać wartości, elementów
# print(cars2, type(cars2))

# ################  Klasa: Słownik
# dict_empty1 = dict()    # pusty słownik
# print(dict_empty1)
# print(type(dict_empty1))

#słownik = {klucz1: wartość klucza1, klucz2: wartość klucza2, itd}
# slownik1 = {'wojenne': 'Medal od honor, Call of Duty',
#            'romans ': 'Romeo i Julia',
#            'komiksy ': 'Kaczor Donald'}
# print(slownik1)

# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }
# print(cars_countries)
#### Przykład: Zwróć uwagę na odwoływanie się do elementów słownika, po nazwie klucza, a
##### następnie po elementach listy (wartość klucza)
# print(cars_countries['Germany'])
# print(cars_countries['Germany'][1])
# print(cars_countries['Asia']['Japan'][0])
# print(cars_countries['Korea'])  # nas slownik nie ma takiego klucza

######################Zadanie 2
# Utwórz słownik zawierający  trzy klucze: imie, nazwisko, wiek
# jako wartości w/w kluczy wpisz listy 3-elementowe zawierające dowolne dane osobowe
# następnie wyświetl kompletne dane osoby o numerze wskazanej przez użytkownika

###Przykład: dodawanie nowego klucza do słownika##########################
# cars_countries['Korea'] = 'Kia' # 1 sposób dodawanie nowego klucza do słownika
# print(cars_countries)
# print(cars_countries['Korea'])

# 2 sposób dodawanie nowego/ch klucza/kluczy do słownika
# cars_countries.update({
#     'France': 'Citroen',
#     'Spain': 'Seat'
#    })
# print(cars_countries)

######################Zadanie 3
# Do poprzednio utworzonego słownika dodaj nowy klucz o nazwie "kierunek_studiów", wartość w/w klucza dowolna
# wskazana przez użytkownika

################# Metody dla klasy słownik:
### var_dict.clear() - usuwa wszystkie klucze ze słownika var_dict
### var_dict.get(klucz) - zwraca wartość dla podanego klucza, gdy klucza nie ma w słowniku zwraca None
### var_dict.has_key(klucz) - zwraca True gdy klucz jest w słowniku, False w przeciwnym razie,
### var_dict.items() - zwraca listę dwuelementowych krotek (klucz, wartość)
### var_dict.keys() - zwraca listę wszystkich kluczy
### var_dict.values() - zwraca listę wszystkich wartości

################# Przykłady
# cars_countries = {
#       'Germany': ['Audi', 'BMW'],
#       'Asia': {'Japan': ['Toyota', 'Honda']}
# }

# del cars_countries['Germany'] # funkcja del usuwa klucz 'Germany' z słownika cars_countries
# print(cars_countries)
# keys = cars_countries.keys()
# print(keys)
# l = len(keys) # funkcja len liczy długość, ilość elementów
# print(l)
# print(len(cars_countries))
######################Zadanie 4
# Wyświetl nazwy kluczy poprzednio utworzonego słownika, oraz ilość jego elementów
# ###########################################

##############  Zadania do wykonania
## 1. Sprawdź wynik działań
# 0 > 1
# 0 <= 1
# 0 >= 1
# 1 == 0
# 1 == 1
# 1 != 0
# 1 != 1
## 2. Oblicz wyrażenie 2x+5y   gdzie: x,y to dowolne dwie liczby które podaje użytkownik (w konsoli)
## 3. Wyświetl zdanie "Jestem a b mam c lat studiuję d",
##  gdzie : a-imie, a-nazwisko, c-liczba, d-kierunek studiów są dowolne zmienne które podaje użytkownik (wczytywane z klawiatury)
## 4. Sprawdź/porównaj czy 1+2+10+20000001+4+347586970885 jest równa 321784560456434534646
## 5. Sprawdź czy suma dowolnych dwóch liczb podanych przez użytkownika jest liczbą parzystą czy nieparzystą wyświetl właściwy komunikat
##   użyj operatora modulo % który zwraca resztę z dzielenia  np. 5%2   czyli 2 reszta 0
## 6. Utwórz prosty kalkulator dla 2 zmiennych podanych przez użytkownika, który obliczy: sumę, różnicę,
## iloczyn, iloraz, potęgę tych liczb, nie zapomnij o stosownych komentarzach informacyjnych dla użytkownika.
## 7. Dla dowolnego x sprawdź wynik działań (x > 1 and x < 13) oraz (x != 5 or x < 0)
# Zadania dodatkowe:
# 1. Wykonaj mini ankietę tj. poproś użytkownika o następujące informacje: imie, nazwisko, wiek, zadaj mu pytania: "Czy zdrowo się odżywiasz?",
# , "Czy lubisz sport?" i dodatkowo 3 inne własne. Po uzyskaniu wszystkich odpowiedzi wyświetl ich podsumowanie.
# 2. Twoim zadaniem jest przygotowanie uniwersalnego i profesjonalnego życiorysu, złożonego z 5-ciu zdań, które wyświetlisz na ekranie
# Użytkownik wpisuje tylko swoje imie, nazwisko, wiek, zawód, miejsce urodzenia, zainteresowania i ... życiorys jest gotowy.
# 3. Przygotuj dla dziecka, które uczy się czytać zestaw sylab do nauki, ale zrób to inteligentnie tj.
# dziecko wpisuje na klawiaturze 1 spółgłoskę a Ty dodajesz do niej odpowiednie samogłoski i wyświetlasz całość na ekranie
# 4. Użytkownik podaje imie, sprawdź czy to imie to Janusz lub Grażyna