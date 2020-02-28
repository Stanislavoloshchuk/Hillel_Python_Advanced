def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """


url_list = [
    'www.google.com/catalog/names',
    'www.ya.com/catalog/cars',
    'www.dou.com.ua/jobs/python_junior',
    'www.hillel.ua/catalog/courses',
    'www.yahoo.com',
]

catalog_finder = ['/catalog/']
filtered_urls = [u for u in url_list for l in catalog_finder if u.find(l) != -1]
print(filtered_urls)
