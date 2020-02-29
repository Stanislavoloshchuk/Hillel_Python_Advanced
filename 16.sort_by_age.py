"""
Дан массив из словарей. C помощью sort() отсортировать массив из словарей
по значению ключа 'age', сгруппировать данные по значению ключа 'city'
вывод должен быть такого вида :
{
   'Kiev': [ {'name': 'Viktor', 'age': 30 },
                {'name': 'Andrey', 'age': 34}],
   'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                   {'name': 'Artem', 'age': 50}],
   'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                {'name': 'Dmitriy', 'age': 21}]
}
"""

students = [
    {'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
    {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
    {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
    {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
    {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
    {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}
]

cities = {s['city'] for s in students}
group_by_city = {c: [] for c in cities}
for s in students:
    group_by_city[s['city']].append({k: v for k, v in s.items() if k != 'city'})
print(group_by_city)

# Output: {'Kiev': [{'name': 'Viktor', 'age': 30}, {'name': 'Andrey', 'age': 34}], \
# 'Lviv': [{'name': 'Vladimir', 'age': 32}, {'name': 'Dmitriy', 'age': 21}], \
# 'Dnepr': [{'name': 'Maksim', 'age': 20}, {'name': 'Artem', 'age': 50}]}
