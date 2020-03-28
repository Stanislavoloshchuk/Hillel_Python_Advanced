"""
Вернуть полученную строку, сделав каждую вторую букву заглавной:
Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
"""


def idiotic_str(input_str):
    ret = ''
    l = False
    for letter in input_str:
        if l:
            ret += letter.upper()
        else:
            ret += letter.lower()
        l = not l
    return ret


print(idiotic_str(input('Please input string:')))

# Output: 
# Please input string: тестовая строка
# тЕсТоВаЯ СтРоКа
