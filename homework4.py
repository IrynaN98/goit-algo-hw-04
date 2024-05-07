def total_salary(path):
    total = 0
    count = 0


    try:
        with open(path, 'r', encoding= 'utf-8') as file:
             for line in file:
                 parts = line.strip().split(',')
                 if len(parts) ==2:
                    salary = int(parts[1]) 
                    total += salary 
                    count += 1 
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print (f"Помилка: {e}")
        return None 
    

    if count == 0:
        print("Файл містить некоректні дані.")
        return None
    
    average_salary = total / count
    return total, average_salary 

result = total_salary("path/to/salary_file.txt")
if result:
    total, average = result 
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")