"""Скрипт берёт список ссылок из файла links_wb.txt, собирает данные со страниц и выгружает
в таблицу с помощью библиотеки pandas"""
import random
import time
import requests
from bs4 import BeautifulSoup
import pandas
from fake_useragent import UserAgent

# Фейковый юзер-агент
useragent = UserAgent()
headers = {'User-Agent': useragent.random}

url_list = []
item_list = []
price_list = []
links = []
count = 0

# Загружаем файл со списком ссылок для скрапинга
with open('links_wb.txt') as links_wb:
    for line in links_wb:
        links.append(line.rstrip())

# Цикл парсинга
for url in links:
    try:
        """ Загрузка страницы """
        response = requests.get(url, headers=headers)
        print()
        """ Выдёргивание данных со страницы """
        soup = BeautifulSoup(response.text, 'lxml')
        item = soup.find('h1', class_='same-part-kt__header')
        price = soup.find('span', class_='price-block__final-price')
        """ Залив данных в таблицу внутри парсера """
        url_list.append(url)
        item_list.append(item.text)
        price_list.append(price.text.strip())
        print(url)
        """ Рандомная пауза в 1..3 секунды """
        time.sleep(random.uniform(1, 3))
        count += 1
        print(f'Done - {count}')
    except AttributeError:
        pass

# Формируем результат в таблицу внутри парсера
result_excel = pandas.DataFrame({
    'URL': url_list,
    'Товар': item_list,
    'Цена': price_list
})

# Выгружаем результат из программы в Excel
df = pandas.DataFrame(result_excel)
print(df)
df.to_excel('wb.xlsx', )

print('Done!')
