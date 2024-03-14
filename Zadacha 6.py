words = []
word = str(input('Введите слово: '))

while word != 'stop':
    words.append(word)
    word = input('Введите слово: ')

result = " ".join(words)
print('Результат:', result)