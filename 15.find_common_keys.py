"""
Найти общие ключи в двух словарях, вернуть список их названий
"""

dict1 = {
    'Vessel_type': 'LNG',
    'DWT': 350000,
    'LBP': '280 mtrs',
    'LOA': '295 mtrs',
    'Name': 'Morning Glory',
}
dict2 = {
    'Vessel_type': 'Bulk Carrier',
    'DWT': 180000, 'LBP': '220 mtrs',
    'LOA': '244 mtrs',
    'Call_Sign': 'CQAJ',
    'Flag': 'Portuguese',
}

common_key = dict1.items() & dict2.items()
common_key = {i[0]: i[1] for i in common_key}
common_keys = dict1.keys() & dict2.keys()

print(common_keys)

# Outupt: {'LOA', 'DWT', 'LBP', 'Vessel_type'}
