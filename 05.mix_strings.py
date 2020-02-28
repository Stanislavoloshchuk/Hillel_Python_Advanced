"""
Дописать функцию, которая будет принимать 2 строки и вставлять вторую
в середину первой
"""


def mix_strings(str1, str2):
    return str1[:4] + str2 + str1[4:]


print(mix_strings("Hey, dude?", " how are you,"))

# Output: Hey, how are you, dude?
