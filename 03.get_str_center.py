"""
Дописать функцию, которая вернет Х символов из середины строки
(2 для четного кол-ва символов, 3 - для нечетного).
"""


def get_str_center(input_str):
    if len(input_str) < 4:
        return input_str
    return get_str_center(input_str[1:-1])


tests = ['bottle', 'bottles', 'x']
for test in tests:
    print(f"{test} -> {get_str_center(test)}")

# Output: 
#bottle -> tt
#bottles -> ttl
#x -> x
