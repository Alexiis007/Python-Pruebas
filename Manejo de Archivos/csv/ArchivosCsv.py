import csv
import os

# Escritura (mode="w" escribira la data pero boorando lo anterior)
# Escritura (mode='a' escribira la data pero conservando lo contenido)
# En el caso de "a" se agrega el newLine para que la nueva data se escriba abajo

data = ['nombres', 'genero', "edad"]

with open('Archivo.csv', mode='a', newline='\n') as archivo_csv:
    csv_escritura = csv.writer(archivo_csv, delimiter=',')
    csv_escritura.writerow(data)

# Lectura

with open('Archivo.csv') as archivo_csv:
    csv_lectura = csv.reader(archivo_csv, delimiter=',')
    for i in csv_lectura:
        print(i, "\n")