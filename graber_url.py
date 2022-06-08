"""Скрипт собирает ссылки на товары со страницы указанной в переменной url"""
import random
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

useragent = UserAgent()
headers = {'User-Agent': useragent.random}
links = []
links_clean = []
links_all = []

# Цикл грабинга ссылок
for n in range(1, 9):
    url = f'https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki?sort=popular&page={n}'
    response = requests.get(url, headers=headers)
    """Выдёргивание всех ссылок со страницы"""
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        links_all.append(link.get('href'))
    print(f'\nDone - {n}')
    """Рандомная пауза"""
    time.sleep(random.uniform(1, 3))

# Отсеивание лишних ссылок
for link_all in links_all:
    if 'catalog' and '?targetUrl=GP' in link_all:
        links_clean.append(link_all)

# Выгрузка и небольшое модифицирование ссылок
for link_clean in links_clean:
    with open('links_wb.txt', 'a') as file_object:
        file_object.write(f'https://www.wildberries.ru{link_clean}\n')

print('-----------------------')
print('Finish')
