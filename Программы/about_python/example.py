#Переменные и коментарии
# name='Vova'
# age =32
# height =1.82
# isWorking= True
# print(f'my name is {name} and {age}, my height {height} and {isWorking}')

#Операции с числоми
# print(f'сложение (+): {3+3}')
# print(f'вычитание (-): {3-3}')
# print(f'умножение (*): {3*3}')
# print(f'деление (/): {3/3}')
# print(f'остаток от деление (%): {3%3}')
# print(f'целый остаток (//): {3//3}')

# операция со строками
# text ='операция для Oпытов'
# print(f' Взять первый элемент строки: {text[0]}')
# print(f' Взять второй элемент строки: {text[1]}')
# print(f' Взять последный элемент строки: {text[-1]}')
# print(f' Взять первые 5 элементов строки: {text[:5]}')
# print(f' Взять последные 5 элементов строки: {text[-5:]}')
# print(f' Взять с 5 по 10 элемент строки: {text[5:10]}')
# print(f' Сделать символи в строке маленкими: {text.lower()}')
# print(f' Замена текста: {text.replace('операции', 'Текст')}')
# print(f' Проверка нахождение фразы в строке: {'опыт' in text}')
# print(f' Разделить строку на слова: {text.split(' ')}')

#массивы и циклы
# product_string = 'Яблоко 25com, Апелсин 31som, Банан 18som, Ананас 92som, Дыня 150som'
# products = product_string.split(',')
# products.sort()
# print(f'Все продукты :{products}')
# print(f'Первый продукт: {products[0]}')
# print(f'Последный продукт: {products[-1]}')
# print(f'Количество продуктов : {len(products)}')

# prices =[]
# for product in products:
#     price =product.split(' ')[1].replace('som','')
#     prices.append(int(price))
# print(f'Только цены на продукты: {prices}')
# products_sum =0
# for price in prices:
#     products_sum +=price
# print(f'Средняя цена за все продукты :{products_sum}')
# print(f'Средняя цена на одинь продукт :{products_sum/len(products)}')

# Функция
# products_string = 'Яблоко 25com, Апелсин 31som, Банан 18som, Ананас 92som, Дыня 150som'
# products= products_string.split(',')
# products.sort()

# def get_product_info (product):
#     price =int(product.split(' ')[1].replace('som',''))
#     name =product.split(' ')[0]
#     return price, name
# def show_product (name, price):
#     print(f'{name}: {price}som')

# products_sum=0
# for price in prices:
#     products_sum +=price

# http запросы или как связать скрипт с интернетом
# import requests
# import time
# # url ='http://ya.ru'
# # response =requests.get(url)
# # print(f'По URL {url} получен ответ: \n {response.text[:3000]}')

# old_valute=None
# #Проверка изменение валют, через парсинг данных с Центрального Банка России

# def check_exchange_rate():
#     global old_valute
#     url = 'https://www.cbr-xml-daily.ru/daily_json.js'
#     response = requests.get(url)
#     json =response.json()
#     valute = json['Valute']
#     for key, value in valute.items():
#         if old_valute !=None:
#             old_rate = old_valute[key]['Value']
#             if old_rate !=value['Value']:
#                 print(f'Курс валюты : {key} изменился с {old_rate} на {'Value'} ')
#     print(f"Курс доллара :{valute['USD']['Value']} p за 1единицу")
#     old_valute= valute
    
# check_exchange_rate()

# сохранение строк в txt файл
old_valute=90
text_file =open('valute.txt', 'w')
text_file.write(str('donier'))
text_file.close()