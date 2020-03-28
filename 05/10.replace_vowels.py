"""
Заменить в произвольной строке согласные буквы на гласные.
"""

try:
    string = input("Input text please: ")
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
    print('Your string should contain at lease one consonant')
    
# Output: 
# Input text please: The fool doth think he is wise, but the wise man knows himself to be a fool
# ThT fh l dfth thlnk h  ds wtsh, b t tht whsn mkn kn ws hhms lf ts b  w fs,l
