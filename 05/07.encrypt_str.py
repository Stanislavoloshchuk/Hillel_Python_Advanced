"""
Дописать функцию, которая будет шифровать полученную строку следующим
образом:
Пример 1: "www" -> "w3"
Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
"""

import itertools

input_str = 'aaaxxxxxxxxxxggggggggghhhhhhhssaaasssddee'
group = ((c, len(list(g))) for c, g in itertools.groupby(input_str))
encrypt_str = ''.join(c + (str(n) if n > 1 else '') for c, n in group)
print(encrypt_str)

# Output: a3x10g9h7s2a3s3d2e2
