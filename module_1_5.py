immutable_var = 7,4,'Z','F'
print(immutable_var)
# immutable_var[0] = 1
# TypeError: 'type' object does not support item assignment     Кортеж не поддерживает изменение элементов!
mutable_list = [0,5,6,'Grid','Hawk']
print(mutable_list)
mutable_list[0] = 3
mutable_list[1] = 1
mutable_list[2] = 9
mutable_list[3] = 'Heart'
mutable_list[4] = 'Chip'
print(mutable_list)