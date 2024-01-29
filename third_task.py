import sys
from pathlib import Path
from colorama import Fore

def catalogue(path, indent=0):
    if path.is_dir():
        name = path.name
        indent = "|" + "  |"*(indent-1) + "--"*(bool(indent))
        print(f"{indent}{Fore.LIGHTYELLOW_EX}[directory]{Fore.RESET}: {name}")

def file(path, indent=0):
    name = path.name
    indent = "|" + "  |"*(indent-1)+"--"
    print(f"{indent}{Fore.LIGHTCYAN_EX}[file]{Fore.RESET}: {name}")

def open_directory(directory, indent=0):
    for path in directory.iterdir():
        if path.is_dir():
            catalogue(path, indent+1)
            open_directory(path, indent+1)
            
    for path in directory.iterdir():
         if path.is_file():
            file(path, indent+1)
    return


         
def main():
    arguments = sys.argv
    if len(arguments) < 2:
        print("Usage: python third_task.py <directory path>")
    else:
        path_to_the_directory = arguments[1]
        directory = Path(path_to_the_directory)
        if directory.exists() and directory.is_dir():
            (catalogue(directory))
            open_directory(directory)
        else:
            print("the catalogue does not exist")
    
if __name__ == "__main__":
    main()

