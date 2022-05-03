# first_number =float(input(("Первое число: ")))
# simbol = input('Действие: ')
# second_number =float(input(("Второе число: ")))
# result = None

while True:
    question = input("Для работы нажмите 'Enter', для окончания введите 'end': ")

    if question == "end":
        break
    else:
        first_number = float(input(("Первое число: ")))
        simbol = input('Действие: ')
        second_number = float(input(("Второе число: ")))
        result = None
        if simbol == "+":
            result = first_number + second_number
            print(f'Результат: {result}')

        elif simbol == "-":
            result = first_number - second_number
            print(f'Результат: {result}')

        elif simbol == "*":
            result = first_number * second_number
            print(f'Результат: {result}')

        elif simbol == "/":
            result = first_number / second_number
            print(f'Результат: {result}')

        else:
            print('Что-то пошло не так')

