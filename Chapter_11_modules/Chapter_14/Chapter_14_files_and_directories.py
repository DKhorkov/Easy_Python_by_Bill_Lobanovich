import glob
import os

# Записать инфу в файл можно в т.ч. с помощью функции print, однако в конце будет добавлена новая строка:
f = open("text.txt", 'w')
print('here is some text\nand another text\nand so on', file=f)
f.close()

# С помощью функции read() можно достать из файла нужное кол-во символов:
f = open("text.txt", 'r')
text = f.read(10)
f.close()
print(text)

# Считывать текст по лииням из файла можно с помощью readlines() или с помощью итерации:
f = open("text.txt", 'r')
text = '1)'
for i in range(2):
    line = f.readline()
    if not line:
        break
    text += line
f.close()
print(text)

f = open("text.txt", 'r')
text = '2)'
for line in f:
    text += line
f.close()
print(text)

# Также можно записывать и считывать информацию в бинарном режиме:
binary_data = bytes([1, 2, 3])
f = open("text2.txt", 'wb')
f.write(binary_data)
f.close()

f = open("text2.txt", 'rb')
print(f.tell())  # Данная функция позволяет понять, на каком байте в файле мы сейчас находимся.
f.seek(1) # А сейчас мы перескочили на первый байт. Поэтому длина файла будет двум и мы прочитаем только 2 и 3 байт.
bin_data = f.read()
f.close()
print(bin_data, len(bin_data))

# ДАЛЕЕ ИДУТ ОПЕРАЦИИ С ФАЙЛАМИ И КАТАЛОГАМИ.

# Проверка, существует ли файл:
print(f'1){os.path.exists("text.txt")}')
print(f'2){os.path.exists("text3.txt")}')

# Проверка, что объект файл:
print(f'3){os.path.isfile("text.txt")}')
print(f'4){os.path.isfile("..")}')

# Проверка, что объект директория:
print(f'5){os.path.isdir("text.txt")}')
print(f'6){os.path.isdir("..")}')

# Для работы с файлами используются Unix-подобные команды по типу chmod, chown, copy, move, rename, mkdir, rmdir и т.д.

# например, можно посмотреть список файлов и папок в директории:
files_and_dirs = os.listdir('Chapter_14')
print(files_and_dirs)
# и вывести все файла, начинающиеся на 't' в папке Chapter_14:
os.chdir('Chapter_14')
print(glob.glob('t*'), end='\n\n')


# Task 1:
files_and_dirs_for_chapter_14 = os.listdir()
for number, file in enumerate(files_and_dirs_for_chapter_14, start=1):
    print(f'{number}) {file}.')

# Task 2:
files_from_parent_dir = os.listdir('..')
for number, file in enumerate(files_from_parent_dir, start=1):
    print(f'{number}) {file}.')

# Task 3:
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'w') as f:
    f.write(test1)

# Task 4:
with open('test.txt', 'r') as f:
    test2 = f.read()

print(f'Равны? {test2 == test1}')
