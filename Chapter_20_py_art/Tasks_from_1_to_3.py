import matplotlib.pyplot as plt

x_coords = (0, 3, 6, 9, 14)
y_coords = (0, 5, 2, 8, 10)
ticks = list(range(0, 15))

fig, plots = plt.subplots(ncols=3)

for plot in plots:
    plot.set_xticks(ticks)
    plot.set_yticks(ticks)

plots[0].scatter(x_coords, y_coords)  # task 1
plots[1].plot(x_coords, y_coords)  # task 2
plots[2].plot(x_coords, y_coords, "o-")  # task 3

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())

plt.show()
