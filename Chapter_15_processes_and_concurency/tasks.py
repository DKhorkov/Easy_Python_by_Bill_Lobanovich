from random import random
import multiprocessing as mp
from time import sleep, time


def get_seconds_to_sleep():
    result = random()
    return result


def data_for_process():
    sec = get_seconds_to_sleep()
    cur_time = time()
    print(f'Текущее время {cur_time}')
    sleep(sec)
    time_after_waiting = time()
    print(f'подождали {sec} секунд и теперь время равно {time_after_waiting}')
    print(f'Проверка, сколько подождали: {time_after_waiting - cur_time}')


for i in range(3):
    proc = mp.Process(target=data_for_process)
    proc.start()

