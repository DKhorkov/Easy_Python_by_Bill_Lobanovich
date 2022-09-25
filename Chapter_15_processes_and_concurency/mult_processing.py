import os
import multiprocessing
import time


def func(input):
    print(f'Here is a process with id {os.getpid()} and it says "{input}"!')


def another_func(name):
    func(name)
    start = 1
    stop = 1000
    for i in range(start, stop):
        print(f'Это номер {i} из {stop}!')
        time.sleep(1)


if __name__ == "__main__":
    func('smth')
    res = multiprocessing.Process(target=another_func, args=('Перебор цифр',))  # Создаем отдельный процесс.
    res.start()
    # Но не хотим ждать от начала и до конца и завершаем его через 10 секунд:
    time.sleep(10)
    res.terminate()
