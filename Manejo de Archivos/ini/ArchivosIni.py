import configparser

# Configuracmos el parser
config = configparser.ConfigParser()

# Configuramos la data que le pasaremos al archivo ini
config['Navegador'] = {"chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"}
config['Pagina'] = {"url": "https://www.outlook.com"}

# Abrimos el archivo ini
with open('Archivo.ini', 'w') as archivo_ini:
    # Le adjuntamos la data al archivo ini
    config.write(archivo_ini)

'''
    OJO Me di cuenta que la ruta en la seccion
    'with open('Archivo.ini', 'w') as archivo_ini:' 
    Dependiendo de el compilador crea el archivo en la rayz del proyecto (VsCode) 
    Y en Pycharm crea el archivo a un lado de el archivo .py que seria la idea 
    principal. OJO
''' 

# Lectura de archivos ini

# Cargamos la data contenida en el archivo ini
config.read('Archivo.ini')

# Guardamos la data que queremos en una variable
# .get('Seccion', 'Variable')
navegadores = config.get('Navegador', 'chrome')
paginas = config.get("Pagina", "url")

# Imprimimos la data traida
print("Secion navegadores / Chrome: ", navegadores)
print("Seccion Paginas / URL: ", paginas)

