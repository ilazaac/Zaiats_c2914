import requests
import sqlite3
from bs4 import BeautifulSoup


resp = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BD%D0%B8%D0%B3%D0%BE%D0%B2')
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features='html.parser')
    a1 = soup.find_all('tr', {'class': 'temperature'})
    t = a1[0].text
    ta = str(t.replace('°', ' '))
    a = ta.split(' ')
    t1 = a[1]
    t2 = a[3]
    t3 = a[5]
    t4 = a[7]
    t5 = a[9]
    t6 = a[11]
    t7 = a[13]
    t8 = a[15]
connection = sqlite3.connect('p10dz.sl3', 5) #создайте базу данных с таким же названием (если не скачали мою)
cur = connection.cursor()
cur.execute('CREATE TABLE weather (temperature TEXT, time TEXT);') # после первого запуска удалить (если скачали мою
# - удалить сразу)
cur.execute('UPDATE weather SET time="2:00" WHERE rowid=1;')
cur.execute('UPDATE weather SET time="5:00" WHERE rowid=2;')
cur.execute('UPDATE weather SET time="8:00" WHERE rowid=3;')
cur.execute('UPDATE weather SET time="11:00" WHERE rowid=4;')
cur.execute('UPDATE weather SET time="14:00" WHERE rowid=5;')
cur.execute('UPDATE weather SET time="17:00" WHERE rowid=6;')
cur.execute('UPDATE weather SET time="20:00" WHERE rowid=7;')
cur.execute('UPDATE weather SET time="23:00" WHERE rowid=8;')
cur.execute(f'UPDATE weather SET temperature={t1} WHERE rowid=1;')
cur.execute(f'UPDATE weather SET temperature={t2} WHERE rowid=2;')
cur.execute(f'UPDATE weather SET temperature={t3} WHERE rowid=3;')
cur.execute(f'UPDATE weather SET temperature={t4} WHERE rowid=4;')
cur.execute(f'UPDATE weather SET temperature={t5} WHERE rowid=5;')
cur.execute(f'UPDATE weather SET temperature={t6} WHERE rowid=6;')
cur.execute(f'UPDATE weather SET temperature={t7} WHERE rowid=7;')
cur.execute(f'UPDATE weather SET temperature={t8} WHERE rowid=8;')
connection.commit()

connection.close()