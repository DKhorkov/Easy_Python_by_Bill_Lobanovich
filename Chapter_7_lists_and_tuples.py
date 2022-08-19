# Task 1:
years_list = [1998 + year for year in range(5)]

# Task 2:
third_birthday = years_list[3]

# Task 3:
oldest = years_list[-1]

# Task 4 - 5:
things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = things[1].title()
print(things)

# Task 6:
things[0] = things[0].upper()
print(things)

# Task 7:
things.pop()
print(things)

# Task 8 - 9:
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
print(surprise[-1][::-1].capitalize())

# Task 10:
even = [number for number in range(10)]
print(even)

# Task 11:
start1 = ['fee', 'fie', 'foe']
rhymes = [('floop', 'get a mop'),
          ('fope', 'turn the rope'),
          ('fa', 'get your ma'),
          ('fudge', 'call the judge'),
          ('fat', 'pet the cat'),
          ('fog', 'walk the dog'),
          ('fun', 'say we\'re done')]
start2 = 'Someone better'
for string in start1:
    for each_tuple in rhymes:
        print(f'{string.title()}! {each_tuple[0].title()}! ')

for each_tuple in rhymes:
    print(f'{start2} {each_tuple[1]}.')

for each_tuple in rhymes:
    print(f'{start1[0].title()}! '
          f'{start1[1].title()}! '
          f'{start1[2].title()}! '
          f'{each_tuple[0].title()}! ')
    print(f'{start2} {each_tuple[1]}.')
