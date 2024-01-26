

def get_cats_info(path):  #повертає список словників з інформацією про кожного кота.
    try:
        with open(path, "r") as cats_file:
            cats_info = []
            cats_info_str = [el.strip() for el in cats_file.readlines()] # створює окремий елемент спизку з кожноі строки файлу 
            for cat in cats_info_str: #оновлює вихідний список словником
                a = cat.split(",")
                cat_dict = {"id": a[0], "name": a[1], "age": a[2]}
                cats_info.append(cat_dict)
            return(cats_info)

    except FileNotFoundError:
        print("File not found. Check the correctness of the path or file name.")
    except IOError:
        print("Input/Output error. The file may be corrupted or there could be another issue.")
    except Exception as e:
        print(f"An unknown error occurred: {e}")
       


cats_info = get_cats_info("cats_file.txt")
print(cats_info)