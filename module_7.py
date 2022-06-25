import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot
from datetime import datetime

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
exchange_rate_table = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
rows = exchange_rate_table.find_all('tr')
dates = []
prices = []
#dt_string="25//06//2022 12:13:05"
#obj=datetime.strptime(dt_string, "%d//%m//%Y %H:%M:%S")
for row in rows:
	columns = row.find_all('td')
	if len(columns) > 0:

		dates.append(datetime.strptime(columns[0].text[2:], '%d.%m.%Y'))
		prices.append(float(columns[1].text))

pyplot.bar(dates, prices)
pyplot.show()