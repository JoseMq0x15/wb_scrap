from selenium import webdriver  #    interactua con el navegador 
from selenium.webdriver.support.select import Select # permite seleccionar un elemento de una lista
from selenium.webdriver.common.by import By # 
# from itertools import dropwhile

import time  # libreria de tiempo
import pandas as pd # para manejar dataFrame 

# -----------Acceder al driver y visitar el sitio web -----------
website = 'https://www.adamchoi.co.uk/teamgoals/detailed' # sitio web
executable_path = 'D:\workspace\driver\chromedriver.exe' # ubicacion del driver
driver  = webdriver.Chrome(executable_path) 

driver.get(website) #---------- ACCEDER AL NAVEGADOR ---------------

# -----------------Hacer click  en una lista en el navegador ----------------------
# xpath ABSOLUTO: va siempre al mismo punto pero al minimo cambio genera errores, 
# all_matches_button = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
# all_matches_button.click()

# xpath RELATIVO (recomendado): Realiza una busqueda con las caracteristicas deseadas
# estructura del XPATH # //: apunta al elemento o etiqueta <label>, @:identifica un atributo, 
# busca la etiqueta <label> q tenga el atributo @analytics-event con el valor "All matches"
all_matches_button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()  #Hacer click sobre el boton

# -----------------Seleccionar un elemento de la lista despegable --------------
dropdown = Select(driver.find_element(By.ID, 'country')) # selecciona el id = "country"
dropdown.select_by_visible_text('Spain') # selecciona spain

#time.sleep(5) # como se observo q la web demora en cargar se usa un delay

# ---------------- Seleccionar varios elementos - TABLA ------------------
# elements en plural ya q son uchos elementos 
# obtener el  nombre de la etiqueta (localizador) 'tr' donde se almacena los registros del partido
matches = driver.find_elements(By.TAG_NAME, 'tr') # filas
# ---------------- Inprime las filas ----------------
for match in matches:
    print(match.text)

# ---------------- almacenar en un DF
partidos = []
for match in matches:   
    partidos.append(match.text)

driver.quit() # --------------- CERRAR EL NAVEGADOR ---------------

df = pd.DataFrame({'partidos': partidos})
print(df)
df.to_csv('partidos.csv', index = False)