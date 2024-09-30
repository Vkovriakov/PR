first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print(3)
elif first == third or first == second or third == second:
    print(2)
else:
    print(0)