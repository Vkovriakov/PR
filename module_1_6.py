my_dict = {'Adelina': 20, 'Sveta': 29,'Kristina': 28}
print(my_dict)
print(my_dict['Adelina'])
print(my_dict.get('Elena'))
my_dict.update({'Olga': 44, 'Regina': 26})
del my_dict['Kristina']
print(my_dict.get('Kristina',28))
print(my_dict)
my_set = {3,5,9,1,3,5,8,3,8,5,'Bullet','Crown'}
print(my_set)
my_set.update({2,4,6,7,'Block'})
my_set.discard(1)
print(my_set)