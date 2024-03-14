place = int(input('Введите номер Вашего места: '))
if place % 2 == 0 and place <= 36:
    print('Это верхнее место в купе')
elif place % 2 != 0 and place <= 36:
    print('Это нижнее место в купе')
elif place % 2 == 0 and place > 36:
    print('Это верхнее боковое место')
else:
    print('Это нижнее боковое место')