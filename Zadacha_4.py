# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input_file4.txt', 'r', encoding='utf-8') as file:
    string = file.read()
    print(string)


letter = string[:1]
letter_count = 1
result = ''
for i in string[1:]:
    if i != letter:
        result += (str(letter_count) + letter)
        letter = i
        letter_count = 1
    else:
        letter_count += 1
result += (str(letter_count) + letter)

print (result)

with open('output_file4.txt', 'w', encoding="utf-8") as file:
      print(result, file = file)

with open('output_file4.txt', 'r', encoding='utf-8') as file:
    string2 = file.read()
    print(string2)


# def new_string[:1]
# letter_count = 1
# result = ''
# for i in string[1:]:
#     if i != letter:
#         result += (str(letter_count) + letter)
#         letter = i
#         letter_count = 1
#     else:
#         letter_count += 1
# result += (str(letter_count) + letter)

# print (result)

# with open('output_file4.txt', 'w', encoding="utf-8") as file:
#       print(result, file = file)