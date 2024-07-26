# Se importa la libreria para el manejo de JSON
import json

'''
    Aqui se aplicara la escritura 'w' y lectura 'r'
    de un archivo JSON desde python 
'''

# Creo la data que pusheare a el archivo JSON
new_data = {
    "Personas": [
        {
            "nombre": "Alexis",
            "edad": 20
        },
        {
            "nombre": "Christian",
            "edad": 40
        }
    ]
}

# Abro el archivo.json en modo escritura y pusheo la data
with open('Archivo.json', 'w') as archivo_json:
    json.dump(new_data, archivo_json)


# Ahora la lectura del archivo JSON
with open('Archivo.json', 'r') as archivo_json:
    # Pasamos la data del json a una variable
    data_json = json.load(archivo_json)
    # Imprimimos la variable
    print('-'*20, "Data Completa", '-'*20)
    print(data_json)
    print("\n")

# Ahora una lectura especifica
with open('Archivo.json', 'r') as archivo_json:
    # Pasamos la data del json a una variable
    data_json = json.load(archivo_json)
    # Imprimimos la variable
    print('-'*20, "Data Especifica", '-'*20)
    print(data_json['Personas'])
    print("\n")