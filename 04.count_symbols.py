"""
Дописать функцию, которая считает сколько раз каждая из букв
встречается в строке, разложить буквы в словарь парами
{буква:количество упоминаний в строке}
"""


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(char_frequency('The fool doth think he is wise, but the wise man knows himself to be a fool.'))

# Output: {'T': 1, 'h': 6, 'e': 7, ' ': 16, 'f': 3, 'o': 7, 'l': 3, 'd': 1, 't': 5, 'i': 5, 'n': 3, 'k': 2, 's': 5, 'w': 3, ',': 1, 'b': 2, 'u': 1, 'm': 2, 'a': 2, '.': 1}
