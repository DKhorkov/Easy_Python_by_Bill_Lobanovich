from collections import OrderedDict, defaultdict

plain = {}
plain['a'] = 1
plain['b'] = 2
plain['c'] = 3
print(plain)

fancy = OrderedDict(plain)
print(fancy)

dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])
