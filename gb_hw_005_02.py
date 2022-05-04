#   2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.


count_string = 0
with open(r"files\text_file_002.txt", 'r', encoding='utf-8') as file:
    for line in file:
        count_words = len(line.split())
        count_string += 1
        print(f'В {count_string}-й строке количество слов: {count_words}')

print(f"Всего строк в файле: {count_string}")
