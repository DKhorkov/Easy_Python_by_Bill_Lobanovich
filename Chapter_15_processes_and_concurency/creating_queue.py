import multiprocessing as mp
import os
import time


def washing(dishes, output):
    print(f'Начат процесс мойки посуды под номером {os.getpid()}')
    for dish in dishes:
        print(f'Моем тарелку из под {dish}а.')
        time.sleep(1)
        output.put(dish)  # Ставим тарелку в очередь на сушку.
    print(f'Завершен процесс мойки посуды под номером {os.getpid()}')


def drying(input):
    print(f'Начат процесс сушки посуды под номером {os.getpid()}')
    while True:
        dish = input.get()  # Получаем объект из списка задач в очереди.
        print(f'Сущим тарелку из под {dish}а')
        input.task_done()


if __name__ == "__main__":
    dishes = ['салат', 'суп', 'десерт']
    dish_queue = mp.JoinableQueue()  # Создаем возможность добавления в очередь.
    drying_process = mp.Process(target=drying, args=(dish_queue,))
    drying_process.daemon = True  # По окончании работы со всеми элементами очереди процесс будет завершен.
    drying_process.start()
    washing(dishes, dish_queue)
    dish_queue.join()  # Сообщаем главному процессу (washing), что вся посуда высушена.
    print(f'Завершен процесс сушки посуды под номером {os.getpid()}')

