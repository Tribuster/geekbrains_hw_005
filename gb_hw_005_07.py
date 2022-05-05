#   7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
#   данные о фирме: название, форма собственности, выручка, издержки.
#   Пример строки файла: firm_1 ООО 10000 5000.
#   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#   Если фирма получила убытки, в расчёт средней прибыли её не включать.
#   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#   Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
#   Итоговый список сохранить в виде json-объекта в соответствующий файл.
#   Пример json-объекта: #   [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#   Подсказка: использовать менеджер контекста.

import json

try:
    with open(r'files\firms_profits.txt', "r", encoding='utf-8') as firm_file:
        firm_prof = {}                                      #   Список фирм и прибыли
        list_av_total = []                                  #   Список положительных прибылей фирм
        for line in firm_file:
            list = line.split()
            total = int(list[2]) - int(list[3])
            firm_prof[list[0]] = total
            if total > 0:
                list_av_total.append(total)
        a_profit = int(sum(list_av_total) / len(list_av_total))
        av_profit = {"average_profit": a_profit}
        end_list = [firm_prof, av_profit]

        print(end_list)
except ZeroDivisionError:
    print("У компаний нет прибыли")
    end_list = [firm_prof, {'averege_profit': 0}]
    print(end_list)
except FileNotFoundError:
    print("Такого файла нет!")

try:
    with open(r'files\averege_profit.json', "w", encoding='utf-8') as file_json:
        json.dump(end_list, file_json)

except FileNotFoundError:
    print("Такого файла нет!")