def near_values(list, values=0):
    return values, sorted(list, key=lambda num: abs(values - num))


print(tuple(near_values([258, 467, 6, 222, 278, 98, 9, 88, 123, 231], 5)))

def output_by_index(sentece):
    while True:
        print('для выхода введите exit')
        try:
            index = input('Введите индекс: ')
            if index == 'exit':
                print('Программа завершена')
                break
            print(sentece[int(index)])
        except:
                     print(f'Вводите только числа от 0 до {len(sentece) -1}')

print(output_by_index(['Hello', ':>', 'nothing', True, 45, False,[],()]))
#map
tup = (2, 5, 20, 44, 64, 72, 80, 210, 222, 290)
number = tuple(map(lambda x: x + 10, tup))
print(list(number))

#filter
y = filter(lambda x: (x >= 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
print(list(y))
c = filter(lambda z: (z <= 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
print(list(c))