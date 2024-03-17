#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?
import math

# set_gene1 = {'SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#              'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#              'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'}
# set_gene2 = {'SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#              'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#              'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'}
# set_gene3 = {'SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC11',
#              'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#              'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'}
#
# all_three = set_gene1.intersection(set_gene2, set_gene3)
#
# # a)
# print(f"Geny wspolne dla wszystkich pacjentow: {all_three}")
# # b)
# common_genes_1_2 = set_gene1.intersection(set_gene2)
# common_genes_1_3 = set_gene1.intersection(set_gene3)
# common_genes_2_3 = set_gene2.intersection(set_gene3)
# print(f"geny wspólne dla pacjentów 1 i 2: {common_genes_1_2}")
# print(f"geny wspólne dla pacjentów 1 i 3: {common_genes_1_3}")
# print(f"geny wspólne dla pacjentów 2 i 3: {common_genes_2_3}")
# # c)
# exclusive_genes_1 = set_gene1.difference(set_gene3, set_gene2)
# print(f"Geny wystepujace tylko dla 1 pacjeta: {exclusive_genes_1}")

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3', 'GALNT14', 'ERCC1',
#                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']
# i = 0
# for gen in lista_gene1:
#     if gen == "FGFR4" or gen == "FGERA4":
#         index = lista_gene1.index(gen)
#         print(index + i)
#         i += 1
#         lista_gene1.pop(index)


#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?

# text = """Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza.
# Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze.
# Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki).
# Ale ku mojej uldze zabrakło jej najważniejszej umiejętności dziennikarza – zdolności do oddzielania interesujących informacji od tych zwyczajnie nudnych. Choć prawidłowo podkreśliła, że stopa bezrobocia się nie zmieniła, Emma nie zauważyła, że liczba osób szukających zatrudnienia wzrosła po raz pierwszy od prawie roku.
# Prawdą jest, że większość ludzi pracujących ze sztuczną inteligencją przyznaje, że nieprędko zastąpi ona człowieka. Po prostu nie jest jeszcze wystarczająco inteligentna. To co zaczynamy jednak obserwować, jest dosyć subtelne, ale nie mniej ważne. Granice pomiędzy pracą człowieka i pracą maszyny zaczynają się zacierać.
# Dla niektórych pracowników to mogłoby być dobrodziejstwo. Wyobrażam sobie sytuację, w której taka maszyna jak Emma mogłaby tworzyć podstawowe raporty na bazie powtarzalnych danych i wysyłać je do redaktora, który by je upiększał i uatrakcyjniał. Associated Press już teraz korzysta z programu zwanego Automated Insights, by pisać proste teksty o wynikach korporacji. W takich przypadkach ludzie mają przewagę – maszyny nie zastępują ich, a jedynie przejmują nudne elementy ich pracy, dzięki czemu więcej czasu mogą oni poświęcić na kreatywne lub ważne sprawy.
# Ale nie wszystkim ludziom maszyny pomogą skupić się na jakości. Istnieją pewne nudne czynności, przy których maszyny wypadają bardzo źle. Armia kiepsko opłacanych pracowników po cichu wykonuje więc te prace. Na przykład przy projekcie Amazon Mechanical Turk– stronie prowadzonej przez internetowego sprzedawcę, gdzie zleceniodawcy płacą za proste (choć pewnie nudne) drobne zadania, które dla maszyn są jednak zbyt skomplikowane. Chodzi  o transkrypcję klipów audio, tagowanie zdjęć przy użyciu odpowiednich słów kluczy, przepisywanie skopiowanych rachunków na arkusze. Amazon nazywa je „zadaniami dla ludzkiej inteligencji” lub HIT-ami (ang. Human Intelligence Task), a zleceniodawcy płacą kilka centów za sztukę. Nazwa Mechanical Turk pochodzi od sztucznej maszyny do gry w szachy z XVIII wieku: choć wyglądała jak robot, w środku schowany był w tajemnicy człowiek. """
#
# print(f"W tekscie slowo Emma pojawia sie {text.count('Emma')} razy")
#
# text_upper = text.upper()
# text_words = text.split(' ')
# print(f"W tekscie jest {text.count('.')} zdan")
########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta
# try:
#     number = int(input("Enter a number: "))
#     print(f"Liczba podana przez uzytkownika jest {'parzysta' if number % 2 == 0 else 'nieparzysta'}")
# except ValueError:
#     print("NIe podano liczby")
########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)


# points = int(input("Podaj ilos otrzymanych punktow: "))
# mean = points/15 * 100
# if mean >= 91:
#     print("Dostales 5.0")
# elif mean >= 81:
#     print("dostales 4.5")
# elif mean >= 71:
#     print("Dostales 4.0")
# elif mean >= 61:
#     print("dostales 3.5")
# elif mean >= 50:
#     print("dostales 3.0")


# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).
# sum = 0
# n = int(input("Enter number: "))
# for i in range(1, n+1):
#     sum += 1/n

###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while
# from math import sqrt
#
# i = 1
# while i <= 10:
#     print(f"Pierwiastek liczby {i} wynosi: {sqrt(i)}")
#     i += 1

###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0
# from math import sqrt
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
#
# delta = (b**2) - (4*a*c)
# if delta < 0:
#     print("Brak rzeczywistych miejsc zerowych")
# elif delta == 0:
#     x1 = (-b + sqrt(delta))/(2*a)
#     print(f"Jedno miejsce zerowe rowne {x1}")
# else:
#     x1 = (-b - sqrt(delta))/(2*a)
#     x2 = (-b + sqrt(delta))/(2*a)
#     print(f"dwa miejsca zerowe x1 = {x1}\nx2 = {x2}")


###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed
### in a comma-separated sequence on a single line.

# def all_even(number):
#     if number % 2 != 0:
#         return False
#     while number:
#         check = number % 10
#         if check % 2 != 0:
#             return False
#         number //= 10
#     return True
#
#
# numbers = [x for x in range(1, 1001)]
#
# for number in numbers:
#     if all_even(number):
#         print(number, end=', ')