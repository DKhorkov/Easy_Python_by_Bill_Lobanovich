from random import random
import multiprocessing as mp
from time import sleep
from datetime import datetime
import os


def get_seconds_to_sleep():
    result = random()
    return result


def data_for_process():
    proc_id = os.getpid()
    sec = get_seconds_to_sleep()
    cur_time = datetime.now()
    print(f'Начат процесс {proc_id}. Текущее время {cur_time}')
    sleep(sec)
    time_after_waiting = datetime.now()
    print(f'подождали {sec} секунд и теперь время равно {time_after_waiting}')
    print(f'Проверка, сколько подождали: {time_after_waiting - cur_time}')


for i in range(3):
    proc = mp.Process(target=data_for_process)
    proc.start()

