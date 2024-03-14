color_1 = str(input('Введите первый цвет: '))
color_2 = str(input('Введите второй цвет: '))
if (color_1 == 'красный' and color_2 == 'синий') or (color_2 == 'красный' and color_1 == 'синий'):
    print('фиолетовый')
elif (color_1 == 'красный' and color_2 == 'желтый') or (color_2 == 'красный' and color_1 == 'желтый'):
    print('оранжевый')
elif (color_1 == 'синий' and color_2 == 'желтый') or (color_2 == 'синий' and color_1 == 'желтый'):
    print('зеленый')
elif color_1 != 'красный' or color_1 != 'синий' or color_1 != 'желтый' or color_2 != 'красный' or color_2 != 'синий' or color_2 != 'желтый':
    print('Ошибка')