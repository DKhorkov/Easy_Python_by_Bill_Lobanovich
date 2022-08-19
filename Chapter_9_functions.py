# Task - 1:
def good():
    return ['Harry', 'Ron', 'Hermione']

# Task - 2:
def get_odds():
    for number in range(1, 10, 2):
        yield number


count = 1
for i in get_odds():
    if count == 3:
        print(i)
        break
    else:
        count += 1

# Task - 3:
def test(func):
    def new_func(*arg, **kwargs):
        print('start')
        result = func(*arg, **kwargs)
        print(f'Result is {result}')
        print('end')
        return result
    return new_func


@test
def test_func(a):
    return a**a


test_func(8)

# Task - 4:
class OopsExeption(Exception):
    pass


try:
    raise OopsExeption
except OopsExeption:
    print('Caught an oops')