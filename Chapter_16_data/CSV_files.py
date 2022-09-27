import csv

# Создадим файл формата CSV и запишем в него некоторую инфу (объекты внутри объекта должны быть итерируемыми):
lst = [[1, 2], [2], [3], ['some, text', 2]]
with open('csv.txt', 'w') as f:
    cvs_file = csv.writer(f)
    cvs_file.writerows(lst)

# Теперь считаем инфу обратно из CSV файла:
with open('tx.txt', 'r') as f:
    csv_file = csv.reader(f)  # Создан csv.reader object
    # for row in csv_file:
    #     print(row)
    data = [row for row in csv_file]  # Если мы уже пройдем по каждой строке, то тут будет пустой список.
    print(data)
