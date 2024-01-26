import re

def total_salary(path):  #повертає загальну та середню суму заробітної плати всіх робітників. Знаходить всі числа в тексті
    try:
        with open(path, "r") as salary_file:
            pattern = r"[\d]+"  #шаблон шукає всі числа
            salary = re.findall(pattern, salary_file.read())  #створює список з зарплат
            total_amount = 0
            for number in salary:   #повертає загальну суму
                total_amount += float(number)
            average_salary = total_amount/len(salary)

            return(total_amount, average_salary)
        
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте правильність шляху або ім'я файлу.")
    except IOError:
        print("Помилка вводу/виводу. Файл може бути пошкоджений або виникла інша проблема.")
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")
       

#total_salary("F:\Repository\goit-algo-hw-04\salary_file.txt")
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {int(total)}, Середня заробітна плата: {int(average)}")
