"""
Дописать функцию, которая принимает список строк с оценками, а возвращает
список строк со средним баллом
Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
["Mike|65", "Jane|42"]
"""

scores = ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"]
avg_score = []
for score in scores:
    cols = score.split("|")
    nums = [int(i) for i in cols[1].split(", ")]
    avg_score.append("|".join([cols[0], str(round(sum(nums) / len(nums)))]))

print(avg_score)
