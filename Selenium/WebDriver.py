from selenium import webdriver
from selenium.webdriver.common.by import By

# Se selecciona Chrome para trabahar
driver = webdriver.Chrome()

# Se selecciona una URL de una pagina
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Trae el titulo de la pagina seleccionada
title = driver.title

print(title, '\n')

# Le damos unos segundos al navegador para que se sincronice de manera correcta
driver.implicitly_wait(5)

# Ubicar elementos del DOM por name o por CSS selector
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

print("Text Box", text_box)
print("Button Submit", submit_button)

# Podemos interactuar con el DOM
# Ejemplos, llenamos un txt box y ejecutamos el metodo click de un button
text_box.send_keys("Selenium")
submit_button.click()

# Ubicar elementos por id
message = driver.find_element(by=By.ID, value="message")
print("Busqueda de elementos por su valor: ", message)

# --------------- Evita que termine el codigo ---------------
input("Cerrar web driver con enter:")

# Termina la sesion
driver.quit()