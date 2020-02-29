"""
Дописать функцию, которая вернет Х символов из середины строки
(2 для четного кол-ва символов, 3 - для нечетного).
"""


def middle(input_str):
    if len(input_str) < 4:
        return input_str
    return middle(input_str[1:-1])


tests = ['bottle', 'bottles', 'x']
for test in tests:
    print(f"{test} -> {middle(test)}")
