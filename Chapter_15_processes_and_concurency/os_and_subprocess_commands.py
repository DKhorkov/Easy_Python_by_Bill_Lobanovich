import os
import subprocess


# Чтобы узнать ID процесса используем следующую команду:
process_id = os.getpid()
print(f'{process_id} - это номер процесса текущего файла Python')

# Чтобы узнать текущий путь используем следующую команду:
current_dir = os.getcwd()
print(f'{current_dir} - текущая директория')

# С помощью модуля subprocess можно выполнять команды системы Unix внутри файла пайтон:
date = subprocess.getoutput('date')
print(f'текущая дата - {date}')
# Также можно посмотреть результат + статус запускаемой программы:
status_and_result = subprocess.getstatusoutput('date')
print(f'Статус команды - {status_and_result[0]}. Результат команды - {status_and_result[1]}.')  # 0 - успех в Unix
# Или просто статус:
status = subprocess.call('date')
print(f'Снова статус - {status}')

