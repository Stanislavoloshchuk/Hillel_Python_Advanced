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
