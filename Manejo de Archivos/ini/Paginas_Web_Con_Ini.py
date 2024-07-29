import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()

# Lectura de archivos ini

# Cargamos la data contenida en el archivo ini
config.read('Archivo.ini')

# Guardamos la data que queremos en una variable
# .get('Seccion', 'Variable')
navegadores = config.get('Navegador', 'chrome')
paginas = config.get("Pagina", "url")

driver = webdriver.Chrome()

driver.get(paginas)

input()

driver.quit()