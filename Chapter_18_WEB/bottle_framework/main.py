from bottle import route, run, static_file


@route('/')  # Создаем URL(базовый в данном случае)
def home_page():
    return static_file('index.html', root='/home/dkhorkov/Рабочий стол/PythonProjects/Easy_Python_by_Bill_Lobanovich/'
                                          'Chapter_18_WEB/bottle_framework/')


run(host='localhost', port=5000, debug=True)  # Запускаем по адресу локального хоста с портом 5000
