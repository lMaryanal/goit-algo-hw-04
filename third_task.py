import sys
from pathlib import Path
from colorama import Fore

def catalogue(path):
    if path.is_dir():
        name = path.name
        print(f"{Fore.LIGHTYELLOW_EX}[directory]{Fore.RESET}: {name}")

def file(path):
    name = path.name
    print(f"{Fore.LIGHTCYAN_EX}[file]{Fore.RESET}: {name}")

def open_directory(directory):
    for path in directory.iterdir():
        if path.is_dir():

            catalogue(directory)
            open_directory(path)
        return()
        if path.is_file():
            file(path)
        

        

        
# Получаем аргументы командной строки
arguments = sys.argv


# Проверяем, что передан хотя бы один аргумент (первый аргумент - имя самого скрипта)
if len(arguments) < 2:
    print("Использование: python script.py <параметр>")
else:
    path_to_the_directory = arguments[1]
    directory = Path(path_to_the_directory)
    if directory.exists() and directory.is_dir():
       # print (catalogue(directory))
        print(directory.iterdir())
        #open_directory(directory)
    else:
        print("the catalogue does not exist")
    


#python third_task.py F:\Repository\exemple