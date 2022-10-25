# importando pacotes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parsel import Selector
from datetime import date
import csv

# criando arquivo csv
#data = csv.writer(open('output.csv','w',encoding='latin'))

# escrevendo colunas do csv
#data.writerow(['Data','Cotação Dolar'])

# criando driver do Chrome
driver = webdriver.Chrome('chromedriver.exe')

# abrindo Google
driver.get('https://www.google.com')

# buscando cotação do dolar na pesquisa Google
driver.find_element(By.NAME, 'q')
driver.find_element(By.NAME, 'q').send_keys('cotação dolar')
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

# identificando elemento do valor do dolar
dolar = driver.find_element(By.CLASS_NAME, 'DFlfde')

response = Selector(text=driver.page_source)

# extraindo valor
dolar = response.xpath('//span/text()').extract()[15]

# convertendo para float
dolar = float(response.xpath('//span/text()').extract()[15].replace(',','.'))

# retornando a data atual
today = date.today()

# escrevendo no csv
with open('cotação_dolar.csv', 'a', newline='') as data:
    writer = csv.writer(data)
    writer.writerow([today, dolar])
