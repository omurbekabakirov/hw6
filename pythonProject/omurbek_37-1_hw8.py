
low = 0
high = 100
num_guess = (low + high) // 2
counter = 0
with open('results.txt', 'w', encoding='UTF-8') as file:
    file.write('Угадай цифру\n')

while True:
    print(f"Вы загадали {num_guess }?")
    user_answer = input("'Да' или 'меньше' или 'больше': ").lower()
    counter += 1
    if user_answer.lower() == 'да':
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Попытки: {counter}\n")
            file.write(f"Ваше число: {num_guess }\n")
            file.write(f'Программа завершила задачу:>')
            print("Программа завершено!")
            break
    elif user_answer == 'меньше':
        high = num_guess
        num_guess = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Предположение программы: '{num_guess }' >= Число\n")
    elif user_answer == 'больше':
        low = num_guess
        num_guess = (low + high) // 2
        with open('results.txt', 'a', encoding='UTF-8') as file:
            file.write(f"Предположение программы: '{num_guess }' <= Число\n")

    else:
        print('Попробуйте еще раз:')
        break