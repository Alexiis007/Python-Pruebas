import csv
import os

# Escritura

data = ['Nombres', 'Genero', "Edad"]

with open('Archivo.csv', mode='a', newline='\n') as archivo_csv:
    csv_escritura = csv.writer(archivo_csv, delimiter=',')
    csv_escritura.writerow(data)

# Lectura

with open('Archivo.csv') as archivo_csv:
    csv_lectura = csv.reader(archivo_csv, delimiter=',')
    for i in csv_lectura:
        print(i, "\n")