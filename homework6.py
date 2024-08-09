my_dict = {'Den': 1990, 'Max': 1992, 'Sveta': 1994 }
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Kolya', 'Такого значения нет'))
my_dict.update({'Masha': 1996, 'Katya': 1998})
print(my_dict)
a = my_dict.pop('Den')
print(a)
print(my_dict)

my_set = {1, 1, 1, 5, 5, 5, 'Urban', 'Hom', 'Hom', 'Urban'}
print(my_set)
print(my_set.add('Mama'))
print(my_set.add(8))
print(my_set)
print(my_set.discard(1))
print(my_set)
