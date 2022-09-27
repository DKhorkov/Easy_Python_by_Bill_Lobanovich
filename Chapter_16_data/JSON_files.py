import json

data = [{'color': "red", 'value': "#f00"}, {'color': "green", 'value': "#0f0"}, {'color': "blue",'value': "#00f"},
        {'color': "cyan", 'value': "#0ff"}, {'color': "magenta", 'value': "#f0f"}]

# Записываем данные в файл в формате JSON:
with open('json_file.json', 'w') as f:
    json.dump(data, f)

# Считываем данные:
with open('json_file.json', 'r') as f:
    json_data = json.load(f)

for elem in json_data:
    print(f'Значение цвета {elem["color"]} - {elem["value"]}.')
