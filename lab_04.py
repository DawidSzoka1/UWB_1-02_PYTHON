import os


########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.

def change_dir(new_dir_path, files_size=False):
    if os.path.isdir(new_dir_path):
        os.chdir(new_dir_path)
        print(f"You are now in {new_dir_path}")
        # print(os.listdir('.'))
        if files_size:
            for file in os.listdir('.'):
                print(f"The file {file} have size {os.path.getsize(file)}")
    else:
        print("This directory does not exist")


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
parent_dir = os.getcwd()
directory_names = ["StudentDoc", "StudentObrazy"]
path_student_doc = os.path.join(parent_dir, directory_names[0])
path_student_obrazy = os.path.join(parent_dir, directory_names[1])
try:
    os.mkdir(path_student_doc)
    os.mkdir(path_student_obrazy)
    print(f"Directory {directory_names} created successfully")
except FileExistsError:
    print("Files already exists")
for directory in directory_names:
    change_dir(directory)
    if not os.path.exists("text_file") and not os.path.exists("photo_file"):
        with open('text_file.txt', 'w') as text_file:
            text_file.write(f'{directory}\n to jest sobie teks')
        with open('photo_file.jpg', 'w') as photo_file:
            photo_file.write(f'a')
    else:
        print("Files already exists")
    change_dir(parent_dir)


for file in os.listdir('.'):
    if os.path.isdir(file):
        os.chdir(file)
        print(f"Files in directory {file}")
        for file_in_dir in os.listdir('.'):

            print(f"The file {file_in_dir} have size {os.path.getsize(file_in_dir)}")
        os.chdir(parent_dir)
