"""
Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
вывести индекс минимального элемента массива
"""
array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def get_min_indexes(array):
    min_value = min(array)
    if array.count(min_value) > 1:
        return [i for i, x in enumerate(array) if x == min(array)]
    else:
        return array.index(min(array))


print(get_min_indexes(array))

# Output: 17
