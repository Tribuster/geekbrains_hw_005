#   4. Создать (не программно) текстовый файл со следующим содержимым:
#   One — 1
#   Two — 2
#   Three — 3
#   Four — 4
#   Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#   При этом английские числительные должны заменяться на русские.
#   Новый блок строк должен записываться в новый текстовый файл.

def russification():
    numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    rus_text = []
    try:
        with open(r'files\Numbers_eng.txt', 'r', encoding="utf-8") as eng_file:
            with open(r'files\Numbers_rus.txt', 'w', encoding="utf-8") as rus_file:
                line_f = eng_file.readlines()
                for i in line_f:
                    list = i.split(' ', 1)
                    rus_text.append(numbers[list[0]] + ' ' + list[1])
                rus_file.writelines(rus_text)
    except FileNotFoundError:
        return 'Файл отсутствует.'

russification()
