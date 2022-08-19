# Task - 1:
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)

# Task - 2:
print(e2f['walrus'])

# Task - 3:
f2e = {value: key for key, value in e2f.items()}
print(f2e)

# Task - 4:
print(f2e['chien'])

# Task - 5:
for key in e2f.keys():
    print(key)

# Tasks 6 - 9:
life = {'animals': {'cats': ['Henry', 'Grumpy', 'Luci'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
for key in life.keys():
    print(key)

for key in life['animals'].keys():
    print(key)

for value in life['animals']['cats']:
    print(value)

# Task - 10:
print(squares := {num: num ** 2 for num in range(10)})

# Task - 11:
print(odd := {num for num in range(10) if num % 2 == 0})

# Task - 12:
for string in ['Got ' + str(num) for num in range(10)]:
    print(string)

# Task - 13:
dictionary = {}
for key, value in zip(('optimist', 'pessimist', 'troll'),
                       ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')):
    dictionary[key] = value

print(dictionary)

# Task - 14:
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks on a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
print(movies := {title: plot for title, plot in zip(titles, plots)})
