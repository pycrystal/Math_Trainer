import random

popt = 10
user_ans = 0

for train in range(10):
    math = ['Правильный треугольник описанный около окружности', 'Правильный четырехугольник описанный около окружности', 'Правильный шестиугольник описанный около окружности', 'Правильный треугольник вписанный в окружности', 'Правильный четырехугольник вписанный в окружности', 'Правильный шестиугольник вписанный в окружности']
    random_math = random.choice(math)
    print(random_math)
    user_input = input('Введите ответ: ')

    if random_math == math[0]:
        if user_input == 'a/√3':
            user_ans = user_ans + 1

    if random_math == math[1]:
        if user_input == 'a/√2':                                       
            user_ans = user_ans + 1

    if random_math == math[2]:
        if user_input == 'a':
            user_ans = user_ans + 1

    if random_math == math[3]:
        if user_input == 'a/2√3':
            user_ans = user_ans + 1

    if random_math == math[4]:
        if user_input == 'a/2':
            user_ans = user_ans + 1

    if random_math == math[5]:
        if user_input == 'a√3/2':
            user_ans = user_ans + 1

print(f'\nПравильно {user_ans} ответов из {popt}')