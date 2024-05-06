import csv
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv

def parcing(table):
    l_table = len(table)

    day = []
    time = []
    sum_cashe = []
    type_transactions = []

    for i in range(l_table):
        tabel_new = table[i].split()
        day.insert(i, tabel_new[1][:-1])
        if len(day[i]) > 1:
            time.insert(i, f'{tabel_new[0]} {day[i]} {tabel_new[2]} {tabel_new[3]} {tabel_new[4]}')
        else:
            time.insert(i, f'{tabel_new[0]} 0{day[i]} {tabel_new[2]} {tabel_new[3]} {tabel_new[4]}')
        time12 = datetime.strptime(time[i], '%B %d %Y %I:%M:%S %p')
        date24 = (time12 + timedelta()).strftime('%d %B %Y %H:%M:%S')
        time[i] = date24
        sum_cashe.insert(i, tabel_new[5])
        type_transactions.insert(i, tabel_new[-1])
    row = [('Дата-времяТранзакции', 'Сумма', 'Тип Транзакции')]
    l_t = len(time)
    for i in range(l_t):
        row.insert(i + 1, (time[i], int(sum_cashe[i]), type_transactions[i]))

    load_dotenv()
    base_folder_allure = os.getenv("FOLDER_ALLURE")

    with open(f'{base_folder_allure}transactions.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(row[0])
        w.writerows(row[1:])

