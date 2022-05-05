#   6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
#   учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
#   Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
#   были все типы занятий.
#   Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#   Вывести его на экран.
#   Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#   Физика: 30(л) — 10(лаб)
#   Физкультура: — 30(пр) —
#   Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

dictionary_classes = {}
try:
    with open(r'files\classes.txt', "r", encoding='utf-8') as class_file:
        for line in class_file:
            list = [", ".join(x.split()) for x in re.split(r'[-.():—]',line) if x.strip()]
            list_2 = [el for el in list if el != "л" and el != "лаб" and el != "пр"]
            subject_name = list_2[0]
            hours_summ = sum(map(int, list_2[1:]))
            dictionary_classes[subject_name] = hours_summ

        print(dictionary_classes)
except FileNotFoundError:
    print("Такого файла нет!")