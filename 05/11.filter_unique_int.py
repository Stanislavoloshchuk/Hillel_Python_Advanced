"""
Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
убрать из него повторяющиеся элементы
"""


def filter_unique_int(input_list):
    return list(dict.fromkeys(input_list))


input_list = filter_unique_int([10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1])
print(input_list)

# Output: [10, 11, 2, 3, 5, 8, 23, 76, 43, 32, 0, 1]
