import xml.etree.ElementTree as ET

# Abrimos el archivo y cargamos los datos contenidos en la raiz
tree = ET.parse('Archivo.xml')
root = tree.getroot()

# Recorremos la raiz en base a todas las personas
for a in root.findall('personas'):
    # Guardamos la data contenida por persona
    persona = a
    # En base a esa data por persona la recorremos
    for b in a.findall('persona'):
        # En base a la data de persona buscamos unicamente nombre
        # Y la regresamos como texto
        print(b.find('nombre').text)