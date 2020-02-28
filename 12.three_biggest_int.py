"""
Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
вывести 3 наибольших числа из исходного массива
"""
input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
list2 = input_list[:]  # make a copy of input_list
k = 3
result = []
for i in range(k):
    result.append(max(list2))  # append largest element to list of results
    list2.remove(max(list2))  # remove largest element from old list
print(result)
