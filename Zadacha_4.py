# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# 1 вариант кодирования:

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

print(result)

with open('output_file4.txt', 'w', encoding="utf-8") as file:
    print(result, file=file)


# # 2 вариант кодирования:

# with open('input_file4.txt', 'r', encoding='utf-8') as file:
#     string = file.read()
#     print(string)


# result = ''
# i = 0
# while i < len(string):
#     letter_count = 1

#     while i+1 < len(string) and string[i] == string[i+1]:
#         letter_count = letter_count +1
#         i=i + 1
#     result += (str(letter_count) + string[i])
#     i=i+1

# print (result)

# with open('output_file4.txt', 'a', encoding="utf-8") as file:
#        print(result, file = file)


# декодирование:

with open('output_file4.txt', 'r', encoding='utf-8') as file:
    string2 = file.readline().rstrip()
    print(string2)


result2 = ""
j = 0
k = 0

while (j <= len(string2)-1):
    count = int(string2[j])
    letter = string2[j+1]

    for k in range(count):
        result2 = result2+letter
        k = k + 1
    j = j + 2

print(result2)

with open('output_file4.txt', 'a+', encoding="utf-8") as file:
    print(result2, file=file)
