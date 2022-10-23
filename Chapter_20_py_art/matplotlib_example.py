import matplotlib.pyplot as plt
from random import choice

numbers = list(range(1, 31))  # Создаем список от 1 до 30 в качестве координат Y
x_coords = [num + choice((-2, -1, 0, 1, 2)) for num in numbers]  # Создаем список от 1 до 30 в качестве координат X
ticks = list(range(0, 31))  # Создаем деления на графике

fig, plots = plt.subplots(nrows=1, ncols=2)  # Создаем шаблон графика, в котором будут два столбца и один ряд
for plot in plots:  # Для каждого из столбцов задаем деления
    plot.set_xticks(ticks)
    plot.set_yticks(ticks)

plots[0].plot(x_coords, numbers)  # Первый столбец - линейный график
plots[1].scatter(x_coords, numbers)  # Второй столбец - график из точек

# Делаем окно fig на весь экран
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
