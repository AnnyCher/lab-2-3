import random
count = 0
right_answers = 0
mistakes = 0
while mistakes < 3:
    number_1 = random.randint(1, 9)
    number_2 = random.randint(1, 9)
    right_answer= number_1 + number_2
    answer = input(f"{number_1} + {number_2} = ")
    if int(answer) == right_answer:
        print("Правильно!")
        right_answers += 1
    else:
        print("Ответ неверный")
        mistakes += 1
        count += 1
print(f'Игра окончена. Правильных ответов: {right_answers}')
