import requests
from bs4 import BeautifulSoup


resp = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features='html.parser')
    soup_list = soup.find_all('td', {'data-label': 'Офіційний курс'})
    res = soup_list[7]
    rate = res.text
    c = float(rate.replace(',', '.'))
    print('Наразі курс доллара до гривні становить:', c, 'UAH')

a = float(input('Скільки гривень ви хочете обміняти? '))
b = a/c
b = round(b, 2)
print('Ви отримаєте', b, '$')