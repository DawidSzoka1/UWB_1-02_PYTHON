# import requests ## obsługa: url, stron www
# ## import wget   ## obsługa: adresy url
# #### instalujemy beautifulsoup4
# import bs4   ### obsługa: parsowanie www,   więcej na : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# import os    ## obsługa: dyski i katalogi PC
# import urllib.parse  ## obsługa: parsowanie url, więcej na: https://docs.python.org/3/library/urllib.parse.html
# # # #import urllib
# # # #import parser
# # instalujemy pillow
# # praca z plikami graficznymi, więcej: https://pillow.readthedocs.io/en/5.1.x/
# from PIL import Image
# #  praca z plikami, więcej na: https://www.tutorialspoint.com/python/python_files_io.htm
# from io import BytesIO

# # ########odczyt kodu HTML #######
# url = 'http://www.poranny.pl/'
# codeHTML = requests.get(url, verify=True).text # odczyt zawartości strony (HTML)
# #print(codeHTML)
# # #### tworzenie obiektu BeautifulSoup z zachowaniem struktury kodu strony
# soup = bs4.BeautifulSoup(codeHTML, 'html.parser')
# #print(soup)  #
#print(soup.prettify()) # wyświetlenie kodu z zachowaniem struktury
# ###################################
#print(soup.find_all("a"))  # obiekt lista której elementy zawierają kod z każdego znacznika <a>
# ###################################
# print(soup.find_all("a")[1]) # kod z drugiego znacznika <a>
# #####podstawowe wybrane metody wyodrębniania tekstu w oparciu o znaczniki#######
# list(print(tag.name) for tag in soup.find_all(True))  # wykaz wszystkich typów znaczników w kodzie
#print(soup.title)
#print(soup.title.string)  # jako typ string
#print(soup.div) # kod z znaczników <div>
# #### kod z pierwszego znacznika o nazwie <div>,
# ###### wyświetla zawartość jego klucza o nazwie class  np. <div class="zafixowanaGora">
# print(soup.div['class'])
# ###################################
# url = 'https://iist.uwb.edu.pl/nii/?student=studenci'
# iiUwB = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
# #print(iiUwB)
# onetags = iiUwB.find_all('a')[35] ##    3-ci z kolei znacznik <a>
# #print(onetags)
# print(onetags.attrs)   ##  zawartość jako atrybuty słownika klucz/wartość
# # ##################################################################3
# print(onetags.attrs['href']) # wyświetl zawartość kodu klucza:'href'
# ###################################
# url = 'http://www.poranny.pl/'
# poranny = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
# firstA = poranny.find_all('a')[1]
# #print(firstA)
# firstIMG = firstA.img   # szukamy obrazów, czyli zawartości znacznika img
# print(firstIMG.attrs)   # wyświetlam słownik z zawartością znacznika img
# imageLink = firstIMG.attrs['src'] # wyświetlam zawartość klucza src
# print(imageLink)
# ###################################
# url = 'http://www.poranny.pl/'
# poranny = bs4.BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
# tags = poranny.find_all("img")
# print(tags)
# # ############################################################
# # #### UWAGA: tu zwróć uwagę na skrócony wariant pisania pętli for ################################
# # #### poniżej zostaną użyte wybrane metody dla list i zmiennych typu string, jeżeli ich nie pamiętasz zajrzyj
# # #### do poprzednich zajęć lub na stronę: https://www.tutorialspoint.com/python/python_strings.htm
# # #print("\n".join(set(tag.attrs['src'] for tag in tags)))
# ###################################
# setOneTags = list()        # zapisz linki z obrazkami do listy wariant 1
# for tag in tags:
#     print(tag['src'])
#     setOneTags.append(tag['src'])
# print(setOneTags)
# ###################################
# setOneTags = list(tag['src'] for tag in tags) # zapisz linki z obrazkami do listy wariant 2
# # #print(setOneTags)
# ###################################
# setOneTagsSplit = list(tag.split('/') for tag in setOneTags) # rozdziel znaki separator '.'
# print(setOneTagsSplit)
# ###################################
# # sprawdź czy zawiera fragment tekstu 'jpg'
# setOneTagsSplitBool = list('jpg' in tag for tag in setOneTags)
# #print(setOneTagsSplitBool)
# indexes = [i for i in range(len(setOneTagsSplitBool)) if setOneTagsSplitBool[i]== True] # numery indeksów
# #print(indexes)
# urlJPG = list(setOneTags[indexes[i]] for i in range(len(indexes)))
#print(urlJPG)
# # # ######zapisz obraz z link nr 1#####
# response = requests.get(urlJPG[0])
# img = Image.open(BytesIO(response.content))  # otwórz plik graficzny
# img.show()      # pokaż zawartość pliku
# img.save('obraz.jpg', "JPEG") # zapisz plik

# # ######pliki pdf zapisz do folderu 3 pliki z #####
# # ################################################3
# url = 'https://iist.uwb.edu.pl/nii/?student=rozklady-zajec-i-stopien'
# # #print(url)
# page1 = requests.get(url, verify=True).text
# print(page1)
# soup = bs4.BeautifulSoup(page1, 'html.parser')
# print(soup)  #
# #
# # ######zwróć uwagę na różnice w treści:
# tags = soup.find_all('a')
# print(type(tags[1]))
# tags = soup.find('a')
# print(tags)
# ###########################
# #### wariant 1
# listLink = list()
# for link in soup.find_all('a'):
#     listLink.append(link.get('href'))
# #print(listLink)
# #
# # #### wariant2
# listLink = list(link.get('href') for link in soup.find_all('a'))
#print(listLink)
# ########W wariancie 2 pojawiły się elementy NoneType, należy je usunąć ########
# listLink1 = list(filter(None,listLink)) # odfiltruj elementy NoneType
# print(listLink1)
###################################
# listLink2 = [element for element in listLink1 if element.endswith('pdf')] # linki zakończone ciągiem znaków pdf
# #print(listLink2)

######uwaga czasami zamiast filtrowania wygodniej jest wykorzystać np. obsługę błędu########
##### więcej o obsłudze błędów i wyjątków możesz znaleźć tu: https://docs.python.org/2/tutorial/errors.html
# adresListPDF = list()
# for link in listLink:
#     try:     # 'złap' błąd
#         if link.endswith('pdf'):
#             adresListPDF.append(link)
#     except(RuntimeError, TypeError, NameError, AttributeError): # można wpisać więcej :)  # pomiń określone błędy
#         pass

# # pass - nie reaguj, nic nie wykonuj
# # break -  wyjście z najbliżej zagnieżdżonej pętli
# # continue - przejście do następnego kroku iteracji w pętli

#print(adresListPDF)

# #######zapis do pliku #########
# MyNameFolder = 'e:\\DYDAKTYKA\\Bioinformatyka\\Laboratorium2017_18\\filePdfLoad\\'
# for link in adresListPDF:
#     splitPathFile = os.path.split(link) # wynik to krotka: (ścieżka, nazwa pliku)
#     # print(os.getcwd()) # sprawdź nazwę ścieżki twojego folderu roboczego
#     fileName = splitPathFile[1]  # pierwszy element z krotki splitPathFile
#     joinMyNameFolderAndFileName = os.path.join(os.path.dirname(MyNameFolder), fileName)# połącz ścieżkę folderu i nazwe pliku
#     #print(joinMyNameFolderAndFileName)
#     # wget.download(link, joinMyNameFolderAndFileName)  # load and save file wariant wygodniejszy
#     urllib.request.urlretrieve(link, joinMyNameFolderAndFileName)