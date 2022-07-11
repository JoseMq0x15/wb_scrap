from bs4 import BeautifulSoup
import requests
from sympy import content

website = 'https://www.transparencia.gob.pe/reportes_directos/pte_transparencia_reg_visitas.aspx?id_entidad=10031&ver=&id_tema=500#.Ystf73ZBxHV'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('div', class_="col-sm-12 col-xs-12") # elemento que contiene la info deseada
title = box.find('h2').get_text() # contiene el titulo
info = box.find('p', class_="esp-text-01").get_text(strip=True, separator=" ") # contiene descripcion
# print(title)
# print(info)
with open(f'{title}.txt', 'w') as file: # w: modo escritura, r: modo lectura
    file.write(info)
    