number = int(input('Введите количество слов: '))
result = ''
for i in range(number):
    word = str(input('Введите слово: '))
    result += word + ' '
    print('Результат: ', result * number)
    break