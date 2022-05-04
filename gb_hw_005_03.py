#   3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#   Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#   Пример файла:
#   Иванов 23543.12
#   Петров 13749.32
salary = {}
list_salaryes = []
with open(r"files\the_salary.txt", 'r', encoding='utf-8') as file:
    for line in file:
        list = line.split()
        salary[list[0]] = float(list[1])

for item in salary.items():
    list_salaryes.append(item[1])
    if item[1] < 20000.00:
        print(f'Сотрудник {item[0]} получает меньше 20000')

print(f'\nСредняя величина дохода всех сотрудников: {round(sum(list_salaryes) / len(list_salaryes), 2)}')
