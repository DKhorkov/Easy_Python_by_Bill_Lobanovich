from datetime import date, datetime, timedelta, time
import time as tm

dat = date(2022, 9, 22)  # Создаем объект, хранящий значение текущего года, месяца и дня.
print(f'Current day is {dat.day}, month is {dat.month} and year is {dat.year}.')

# Также можно вывести содержимое созданного объекта с помощью метода isoformat():
print(dat.isoformat())

# Чтобы создать с текущим днем можно использовать один из следующих методов:
current_date_1 = date.today()
current_date_2 = datetime.now()  # тут уже не просто дата, но еще и текущее время.
print(current_date_1, '|', current_date_2)

# Для добавления или вычитания времени используется модуль timedelta:
day_to_add = timedelta(days=1)
next_day = current_date_1 + day_to_add
print(f'Next day data will be {next_day}.')
month_later = current_date_1 + 30 * day_to_add  # Также можно умножать объект timedelta.
print(f'Same day will be at {month_later}.')

# Для получения времени используется модуль time:
time = time(11, 14, 55)
print(f'Current time is {time.hour} hours, {time.minute} minutes and {time.second} seconds.')


# С помощью модуля datetime можно объединить дату и время или разделить единый объект с датой и временем на дату
# и время по отдельности:
date_from_datetime = current_date_2.date()
time_from_datetime = current_date_2.time()
print(f'Date from datetime object is {date_from_datetime} and time is {time_from_datetime}.')

datetime_from_date_and_time = datetime.combine(current_date_1, time)
print(f'Combining current day and time u will get current datetime witch is {datetime_from_date_and_time}.')


# Для перевода времени в часовые пояса и нахождения локального времени используются следующие функции:
localtime = tm.localtime()
UTC_time = tm.gmtime()
print(f'Current local datetime is {list(localtime[x] for x in range(9))}.')  # Range 9 так как это длина объекта
                                                                                # time.struct_time
print(f'Current UTC datetime is {list(UTC_time[x] for x in range(9))}.')
localtime_in_seconds = tm.mktime(localtime)  # Перевод локального времени в секунды с начала эпохи (линукс)ю
print(f'Local time in second is {localtime_in_seconds}.')

# Спецификаторы и функции srtftime - преобразует дату и время в строку|strrptime - преобразует строку в дату и время:
print(f"Local time with readeble format is {tm.strftime('%d %m %Y', localtime)}.")


# Task 1:
cur_time = date.today().isoformat()
with open('today.txt', 'w') as f:
    f.write(cur_time)

# Task 2:
with open('today.txt', 'r') as f:
    today_string = f.read()
print(today_string)

# Task 4:
date = date(1998, 5, 6)

# Task 5:
print(f'I was born at {date.strftime("%A")} {date.strftime("%d")} {date.strftime("%B")} {date.strftime("%Y")}Y.')

