"""
Заменить в произвольной строке согласные буквы на гласные.
"""
try:
    string = input("Input letters please: ")
    vowel = 'aeiouAEIOU'
    x = list(filter(lambda x: x not in vowel, string))
    x *= len(list(filter(lambda x: x in vowel, string))) // len(x) + 1
    index = 0
    for i in string:
        if i in vowel:
            print(x[index], end='')
            index += 1
        else:
            print(i, end='')
except ZeroDivisionError:
    print('Your string doesnt have a vowel')
