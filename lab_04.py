import os


########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.

# def change_dir(new_dir_path, files_size=False):
#     if os.path.isdir(new_dir_path):
#         os.chdir(new_dir_path)
#         print(f"You are now in {new_dir_path}")
#         # print(os.listdir('.'))
#         if files_size:
#             for file in os.listdir('.'):
#                 print(f"The file {file} have size {os.path.getsize(file)}")
#     else:
#         print("This directory does not exist")
#

#
# while True:
#     answer = input("Would you like to change the directory: ")
#     if answer == "yes":
#         new_dir = input("Enter the new directory path: ")
#         change_dir(new_dir)
#         break

########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym

# parent_dir = os.getcwd()
# directory_name = "Dokumenty"
# path = os.path.join(parent_dir, directory_name)
# try:
#     os.mkdir(path)
#     print(f"Directory {directory_name} created successfully")
# except FileExistsError:
#     print("This file already exists")
# print(f"Pliki w folderze {os.listdir('.')}")
# change_dir(path)
# print(f"You are now in {os.getcwd()}")
# for i in range(3):
#     if os.path.exists(os.path.join(parent_dir, directory_name+f"/lab_0{i+1}.doc")):
#         print(f"File already exists")
#     else:
#         with open(f"lab_0{i+1}.doc", 'w') as f:
#             f.write(f"This is lab_0{i+1}")
#
# print("All files in directory: ", os.listdir('.'))
# print("All files in directory with .doc extension: ")
# for i in os.listdir('.'):
#     if i.endswith('.doc'):
#         print(i)

########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku
# parent_dir = os.getcwd()
# directory_names = ["StudentDoc", "StudentObrazy"]
# path_student_doc = os.path.join(parent_dir, directory_names[0])
# path_student_obrazy = os.path.join(parent_dir, directory_names[1])
# try:
#     os.mkdir(path_student_doc)
#     os.mkdir(path_student_obrazy)
#     print(f"Directory {directory_names} created successfully")
# except FileExistsError:
#     print("Files already exists")
# for directory in directory_names:
#     change_dir(directory)
#     if not os.path.exists("text_file") and not os.path.exists("photo_file"):
#         with open('text_file.txt', 'w') as text_file:
#             text_file.write(f'{directory}\n to jest sobie teks')
#         with open('photo_file.jpg', 'w') as photo_file:
#             photo_file.write(f'a')
#     else:
#         print("Files already exists")
#     change_dir(parent_dir)
#
#
# for file in os.listdir('.'):
#     if os.path.isdir(file):
#         os.chdir(file)
#         print(f"Files in directory {file}")
#         for file_in_dir in os.listdir('.'):
#
#             print(f"The file {file_in_dir} have size {os.path.getsize(file_in_dir)}")
#         os.chdir(parent_dir)

########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.
# local_path = os.getcwd()
# new_file_path = os.path.join(local_path, "change")
# try:
#     os.mkdir(new_file_path)
# except FileExistsError:
#     print("File exists!")
# try:
#     os.rename(new_file_path, os.path.join(local_path, "after_change"))
# except FileExistsError:
#     print("File exists!")

########################## Zadanie 6 ########################
# # Utwórz trzy listy, zapisz, usuń a następnie odczytaj z pliku listy, użyj pickle
# import pickle
#
# list1 = [1, 2, 3, 4]
# list2 = ["12", "32"]
# list3 = ["owoce wow", "owoce wow"]
# with open("testpickle.txt", "wb") as f:
#     pickle.dump([list1, list2, list3], f)
#
# del list1, list2, list3
# with open("test.pickle.txt", "rb") as f:
#     obj1, obj2, obj3 = pickle.load(f)
#
# print(obj1, obj2, obj3)
########################## Zadanie 7 ########################
## Zapisz do pliku liczbę 123456789, spakuj, rozpakuj dane
## Sprawdź w dokumentacji pakietu struct typ danej
## https://docs.python.org/3/library/struct.html
# import struct
#
# with open("struct_test.txt", "wb") as file:
#     file.write(struct.pack('q', 123456789))
#
#
# with open("struct_test.txt", "rb") as file:
#     packed_data = file.read()
#
#
# unpacked_data = struct.unpack('q', packed_data)
#
# print("Pakowane dane:", packed_data)
# print("Rozpakowane dane:", unpacked_data[0])

######################### Zadanie 8 #########################
# Utwórz i zapisz do folderu 5 dowolnych plików tekstowych z dowolnym tekstem
##(więcej niż 5 zdań), możesz tez skopiować dowolny tekst.
## Nazwy plików: Tekst1ID_ABC, Tekst2ID_405.txt, Tekst3ID_607.txt, Tekst4ID_ABC.txt, Tekst5ID_DEF.txt
## Uwaga: pisząc program przyjmij założenie, że masz takich nazw plików w folderze tysiące,
## program ma działać niezależnie od liczby plików w folderze
## Utwórz funkcję która:
## a) odczyta z folderu nazwy wszystkich plików
## b) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.
## Utwórz dodatkowową funkcję która wykorzystując poprzednią funkcję sprawdzi:
## a) ile plików zawiera w identyfikatorze ID liczbę 0
## b) dla wszystkich plików które w nazwie nie mają liczby 0
##    wyznaczy liczbę słów
## c) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.

# file_names = ["Tekst1ID_ABC.txt", "Tekst2ID_405.txt", "Tekst3ID_607.txt", "Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]
# path_home = os.getcwd()
# new_dir_path = os.path.join(path_home, 'task8_lab_04')
# try:
#     os.mkdir(new_dir_path)
# except FileExistsError as e:
#     print(f"FIleExistsError exeption {e}")
#
# for file_name in file_names:
#     with open(os.path.join(new_dir_path, file_name), 'w') as f:
#         f.write(
#             f"fdbgdfuhbvkjdfhkjvbdfjbvhjdfb {file_name} {new_dir_path}. "
#             f"daohdija ahsfdshu gggydtdtd gdgfdggf. sdufhsdufhiu. sdifhsudhfiusdh hsdiufhsdiufhsdiufh iushdfiuh siudfh."
#             f" sdfiohsdiufhiusdhfiusdhfiu. sdofjidshfiushdiughdu dfuh gudfhgu hdfughd fu . fdgdfg")
#
#
# def directory_read(path_to_dir):
#     print(os.listdir(path_to_dir))
#     for filename in os.listdir(path_to_dir):
#         if filename.split(".")[0].split('_')[1].endswith('ABC'):
#             with open(os.path.join(path_to_dir, filename), 'r') as f:
#                 count = 0
#                 for word in f.read().split(' '):
#                     if len(word) >= 3:
#                         count += 1
#                 print(f"Ilosc wyrazow z dlugoscia co najmniej 3 {count}")
#     return os.listdir(path_to_dir)
#
#
# def second_func(path):
#     files_with_0 = [file for file in directory_read(path) if '0' in file.split('ID_')[1]]
#     print(f"Liczba plikow zawierajaca 0 w nazwie: {len(files_with_0)}")
#
#     files_without_0 = [file for file in directory_read(path) if '0' not in file]
#     for file in files_without_0:
#         with open(os.path.join(path, file), 'r') as f:
#             print(f"Ilosc slow: {len(f.read().split(' '))}")
#
#
# directory_read(new_dir_path)
