########################## Zadania do wykonania
# # ################################ Task 0
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation

# def div_by_7_not_5(*args):
#     """
#     takes some numbers checks if number is divisible by 7 and not multiply by 5
#     Args:
#         *args (int): numbers to check
#
#     Returns:
#         list: numbers that are divisible by 7 and not multiply by 5
#
#     """
#     good = []
#     for num in args:
#         if num % 7 == 0 and num % 5 != 0:
#             good.append(num)
#             print(num, end=',')
#     return good
#

#
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#
# ''
# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file
# import re
#
#
# def validate_password(to_check_password):
#     """
#     checks if to_check_password is correct or not:
#          1. At least 1 letter between [a-z]
#          2. At least 1 number between [0-9]
#          3. At least 1 letter between [A-Z]
#          4. Minimum length of transaction password: 4
#          5. Maximum length of transaction password: 8
#     Args:
#         to_check_password (str): password  to validate
#
#     Returns:
#         bool: True if to_check_password is correct else False
#
#     """
#     if len(to_check_password) < 4 or len(to_check_password) > 8:
#         print("Password must be at least 4 characters long or less than 8 characters")
#         return False
#     if not re.search("[a-z]", to_check_password):
#         print("Password must contain at least one lowercase letter")
#         return False
#     elif not re.search("[A-Z]", to_check_password):
#         print("Password must contain at least one uppercase letter")
#         return False
#     elif not re.search("[0-9]", to_check_password):
#         print("Password must contain at least one number")
#         return False
#     return True
#
#
# password = input("Enter your password: ")
# while True:
#     if validate_password(password):
#         print("Password is correct")
#         with open("validate_password.txt", "w") as t:
#             t.write(f"Podane haslo jest poprawne")
#         break
#     else:
#         password = input("Enter a correct password: ")
#         continue
################ Task 2
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line.
## You should to document your code by using python docstrings
## (dokumentacja kodu styl google)
## Don't forget to handle exceptions (obsłudze wyjątków)
## Save result to *.pkl file use picle package
# import pickle
#
#
# def div_by_7_not_5(num: int):
#     """
#     takes some number checks if number is div by 7 and not mul by 5
#     Args:
#         num(int): number to check
#
#     Returns:
#         bool: True if number is divisible by 7 and not multiply by 5 else False
#
#     """
#     return num % 7 and num % 5 != 0
#
#
# x = 1000
# y = 2101
# my_list = list(range(x, y, 1))
# my_list_correct = filter(div_by_7_not_5, my_list)
#
# with open("div_7_not_mul_5.pkl", "wb") as f:
#     pickle.dump(my_list_correct, f)

################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

def task3(*args):
    '''
    Takes numbers and append list with every number to the power of that number
    Args:
        *args: numbers

    Returns:
        list: list with every number to the power of that number
    '''
    if len(args) > 99:
        return "za duzo argmuentow"

    return [pow(x, x) for x in args]


# task3(3, 2, 5, 6, 7)
# print(x1)
################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Don't forget to handle exceptions (obsłudze wyjątków)
###############
def task4(*args):
    '''
    Takes key, values return string of every single number to the power of that number
    Args:
        *args (int): numbers

    Returns:
        creats new variabuls x1, x2, x3, ... xn with value x1^x1, x2^x2, ... xn^xn
        (list): paraments ** paramets
    Raises:
        ValueError: If the number of input parameters is grater than 99
        ValueError: If the argument isnt number
    '''
    numbers = []
    if len(args) > 99:
        raise ValueError("Number of inputs must be less or equal than 99")

    for i, num in enumerate(args, 1):
        try:
            globals()[f"x{i}"] = pow(num, num)
            numbers.append(pow(num, num))
        except ValueError as e:
            print(f"ValueError {e}")
    return numbers


input_params = input("Enter comma-separated numbers: ").split(',')
try:
    float_params = [float(x) for x in input_params]
    print(task4(*float_params))
except ValueError as e:
    print(f"ValueError {e}")

########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Next step: decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory
# import os
#
# main_path = os.getcwd()
# new_file_name = "task5"
# try:
#     os.mkdir(os.path.join(main_path, new_file_name))
#
# except FileExistsError as e:
#     print(f"FIleExistsError {e} ")
# file_names = ["Text1ID_ABC.txt", "Text2ID_405.txt", "Text3ID_607.txt", "Text4ID_ABC5.txt"," Text5ID_DEF.txt"]
# os.chdir(os.path.join(main_path, new_file_name))
# for i in file_names:
#     with open(i, "w") as f:
#         f.write(f"plik {i}. zawiera tekst. jakis tam. saffsdfdsfds. sdfsdfsdf .sdf sdfsdfsdfsdf. sdfsdf")
#
# os.chdir(main_path)
#

# def task5(*args):
#     """
#         takes names of files and prints how many words longer than 3 are in files that coitains ABC in their name
#
#     Args:
#         *args (str): name of file
#
#     Returns:
#
#     """
#     for file in args:
#         print(os.listdir(f"{file}"))
#         for file_name in os.listdir(f"{file}"):
#             if "ABC" in file_name:
#                 count = 0
#                 with open(file_name, "r") as f:
#                     for word in f:
#                         if len(word) > 3:
#                             count += 1
#                 print(f"ilosc slow dlugosci ponad 3: {count}")
