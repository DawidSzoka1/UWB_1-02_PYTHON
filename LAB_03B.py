## Zadanie 1
# # Utwórz 1 funkcje wielu-zmiennych wejściowych, która obliczy wartość wyrażenia
# ## dla dowolnego jednego argumentu wejściowego, x^x
# ## dla dowolnych dwóch argumentów wejściowych  x^x,
# dla pozostałych przypadków wyświetli komunikat, że jest błąd.

# def power(*args):
#     if len(args) > 2:
#         print("za duzo zmiennych")
#         return 0
#     for num in args:
#         print(num ** num)
######### Zadanie 2
## Wczytaj poniższy fragment tekstu opisujący komputer
## Napisz funkcję która ustali liczbę występujących w tym tekście wyrazów wskazanych przez użytkownika
## ciąg nazw i liczba wyszukiwanych wyrazów podanych przez użytkownika jest dowolna,
## niemniej w tekście są wyrazy o nazwach kluczowych i potencjalnie zawsze ważnych
### dla innych użytkowników np. komputera, skaner, uwzględnij je w wyszukiwaniu.

# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest '   \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
#
# def Intext(text, *args):
#     for word in args:
#         print(f"wyrazu {word} w teksie jest {text.count(word)}")
#
# Intext(text, 'komputer', 'a')


############ Zadanie 3 #################
## Utwórz funkcję o nazwie "SredniaLiczb.py", która wczyta N dowolnych liczb
## i obliczy średnią z w/w liczb, podane przez użytkownika liczby przypisz do listy

# def SredniaLiczba(*N):
#     return sum(N)/len(N)

############ Zadanie ##################
## Utwórz funkcję o nazwie "ZdanieRozdziel.py", która wczyta od użytkownika pewien dowolny tekst,'
## a następnie podzieli go na zdania (zakładamy, że jednoznacznie kropka rozdziela zdania)'
## funkcja w zależności od ustawionych kolejnych parametrów wejściowych funkcji
## (ustaw domyślnie argumenty wejściowe: True),
## może ale nie musi wyświetlić następujące informacje:
## ile w każdym zdaniu jest fragmentów rozdzielonych przez określony znak np. ',', ';'
# (domyślnie argument wejściowy to przecinek: ',')
## ile w każdym zdaniu jest wyrazów (zakładamy, że spacja oddziela wyrazy w zdaniu)
## użyj odpowiednich metod dla zmiennych typu string np. split do rozdzielenia elementów: x = ‘blue,red,green’,   x.split(“,”)

# def ZdanieRodziel(text, sep=',',separator=True , space=True):
#     words = text.split('.')
#     if separator:
#         for word in words:
#             length = len(word.split(sep))
#             print(f"W zdaniu '{word}' separator {sep} rozdziela {length if length > 1 else 0} slow")
#     if space:
#         for word in words:
#             print(f"W zdaniu '{word}' jest {word.count(' ')} wyrazow")
#
#
# ZdanieROdziel('tesdt, gfd', sep='.')

########### Zadanie 6  ########################
## Zdefiniuj funkcję "CiagGometryczny.py", która dla podanych trzech parametrów:
## n=numer elementu ciągu, a1=wartość pierwszego elementu ciągu (domyślnie: 1),
## q=wartość iloczynu ciągu geometrycznego (domyślnie: 2)
## zwróci w zależności od ustawianych parametrów funkcji
## a) wartość n-tego elementu ciągu geometrycznego
## b) sumę elementów ciągu geometrycznego

# def CiagGeometryczny(n, a1=1, q=2, sum=False):
#     if q == 1:
#         return a1 * n
#     if sum:
#         return a1 * ((1 - q ** n) / (1 - q))
#     return a1 * (q ** (n - 1))

# ########################## Zadanie 7
## Zaprojektuj program służący do obsługi prostej bazy danych dla sklepu z
## dowolnej branży o różnej liczbie pracowników. Program zapisuje do kolejnych list
## liczby produktów dostarczonych w danym dniu (nazwa listy odpowiada nazwie towaru)
## liczba towarów powinna być zapamiętana


# def Shop(id_sklep=0, liczba_pracownikow=5, **kwargs):
#     shop = {'id_sklep': id_sklep, 'liczba_pracownikow': liczba_pracownikow, 'produkty': kwargs}
#     print("Sklep zostal stworzony")
#     return shop
#
#
# def delivery(shop, **kwargs):
#     print(f"Stan magazynu:")
#     for product, amount in kwargs.items():
#         if product in shop['produkty']:
#             shop['produkty'][product] += amount
#         else:
#             shop['produkty'][product] = amount
#     for product, amount in shop['produkty'].items():
#         print(f"Produktu {product} mamy: {amount}")
#
#
# def shop_info(shop:dict):
#     print(f"W sklepie {shop['id_sklep']} pracuje {shop['liczba_pracownikow']} pracownikow")
#     delivery(shop)
#
#
# shop = Shop(2, liczba_pracownikow=15, drabina=500, cement=200)
# delivery(shop, drabina=50, cement=200, jabłka = 200)
#
# shop_info(shop)

# ########################## Zadanie 8
## W module pole_prostokata.py
## Zdefiniuj funkcję która obliczy pole powierzchni prostokąta
## W module pole_trojkata.py
## Zdefiniuj funkcję która obliczy pole powierzchni trójkąta
# W module pola.py
## Korzystając z modułów pole_prostokata i pole_trojkata
## napisz funkcję która ma możliwość obliczenia pola prostokąta, trójkąta i kwadratu
## Użyj zmiennych globals, utwórz moduł globals.py w którym będą przechowywane
## domyślne wartości dla boków prostokąta, trójkąta, kwadratu (równe 1)


# rozwiazanie w module pole.py

# ########################## Zadanie 9
## Zdefiniuj funkcję wyższego rzędu która ma możliwość obliczenia
## pole powierzchni prostokąta i pola powierzchni trójkąta
## Nie modyfikując zawartości w/w funkcji, użyj dekoratora i dodaj możliwość
## obliczenia pola kwadratu


