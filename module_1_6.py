my_dict = {'Иван': 1990, 'Мария': 1985, 'Петр': 1975, 'Анна': 1980}
print(my_dict)

print(my_dict['Иван'])
print(my_dict.get('Сергей', 'Ключ не найден'))

my_dict['Дмитрий'] = 1995
my_dict['Елена'] = 1992
print(my_dict)

del my_dict['Петр']
print(my_dict.get('Петр', 'Ключ не найден'))
print(my_dict)

my_set = {1, 'abc', 3.14, 'xyz', 1, 2.71}
print(my_set)

my_set.add(5)
my_set.add(7)
print(my_set)

my_set.remove(3.14)
print(my_set)