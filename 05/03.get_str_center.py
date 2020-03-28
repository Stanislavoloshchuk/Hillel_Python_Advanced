"""
Дописать функцию, которая вернет Х символов из середины строки
(2 для четного кол-ва символов, 3 - для нечетного).
"""


def get_str_center(input_str):
    if len(input_str) < 4:
        return input_str
    return get_str_center(input_str[1:-1])

def get_str_center_checked(input_str):
    if len(input_str) <= 2:
        return ('Please enter more then one letter')
    return get_str_center(input_str)


tests = ['bottle', 'bottles', 'x']
for test in tests:
    print(get_str_center_checked(test))

# Output: 
#bottle -> tt
#bottles -> ttl
#x -> Please enter more then one letter
