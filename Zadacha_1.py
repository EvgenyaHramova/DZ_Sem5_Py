# Напишите программу, удаляющую из текста все слова, содержащие "а', 'б', 'в'.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input_file.txt', 'r', encoding='utf-8') as file:
    some_list = file.read().split()
    print(some_list)


new_list = list(filter(lambda word: 'а' not in word, some_list))
new_list = list(filter(lambda word: 'б' not in word, new_list))
new_list = ' '.join(list(filter(lambda word: 'в' not  in word, new_list)))

#print()
#print(new_list)

with open('output_file.txt', 'w', encoding="utf-8") as file:
      print(new_list, file = file)