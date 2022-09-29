import csv
import sqlite3

# Task 1:
data = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss, "Eats, Shoots & Leaves"'''
with open('books.csv', 'w') as f:
    f.write(data)

# Task 2:
with open('books.csv', 'r') as f:
    books = csv.DictReader(f)
    for row in books:
        print(row)

# Task 3:
data_2 = '''title,author,year
The Weidestone of Brisingamen, Alan Garner, 1960
Perdido Street Station, China Mieville, 2000
Trud!, Terry Pratchett, 2005
The Spellman Files, Lisa Lutz, 2007
Small Gods, Terry Pratchett, 1992'''

with open('books_2.csv', 'w') as f:
    f.write(data_2)


# Task 4:
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
create_table = 'CREATE TABLE IF NOT EXISTS books  (title CHAR, author CHAR, year INT)'
cursor.execute(create_table)
connection.commit()
connection.close()

# Task 5:
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
command = 'INSERT INTO books VALUES(?, ?, ?)'
with open('books_2.csv', 'r') as f:
    file = csv.reader(f)
    data = [line for line in file]
    line_num = 1
    for line in data:
        if line_num > 1:
            print(line)
            cursor.execute(command, line)
        else:
            line_num += 1
            continue
connection.commit()
connection.close()

# Task 6:
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
command = 'SELECT title FROM books ORDER BY title ASC'
books_table = cursor.execute(command)
for row in books_table:
    print(row)
connection.close()

# Task 7:
connection = sqlite3.connect('books.db')
cursor = connection.cursor()
command = 'SELECT * FROM books ORDER BY year ASC'
books_table = cursor.execute(command)
for row in books_table:
    print(*row, sep=',')  # Выводим не список, где инфа является его элементами, а единую строку
connection.close()
