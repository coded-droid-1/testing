from time import sleep
import os
import requests
from bs4 import BeautifulSoup

def main():	
	r = requests.get("https://cbr.ru/currency_base/daily/")

	soup = BeautifulSoup(r.text, 'lxml')
	rate = soup.find('div', class_= 'table').find_all("td")[59]
	rate = str(rate)
	rate = rate.split("<")[1]
	rate = rate.split(">")[1]
	print("€ = " + rate)

while True:
	os.system("clear")
	main()
	sleep(20)
