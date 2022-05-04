#  5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

try:
    with open(r'files\list_numbers.txt', 'w+', encoding='utf-8') as file:
        line = input('Введите цифры через пробел: ')
        file.writelines(line)
        file.seek(0)
        line_file = file.readline()
        numbers = line_file.split()
        print(f'Сумма чисел в файле равна: {sum(map(float, numbers))}')
except IOError:
    print('Файл не найден, проверьте путь.')
except ValueError:
    print('Нужно вводить только цифры')