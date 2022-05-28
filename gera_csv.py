import csv
import json
import os

lista_intermediaria = []
lista_final = [['url', 'professor1', 'categoria1', 'professor2', 'categoria2', 'professor3', 'categoria3',
                'professor4', 'catetoria4']]

path = os.curdir
path_source_file = os.path.join(path, 'banca_sanitizada.json')
path_destination_file = os.path.join(path, 'banca.csv')

with open(path_source_file) as f:
    data_frame = json.load(f)

for df in data_frame:
    lista_intermediaria += [df['url']]
    if isinstance(df['banca'], dict):
        lista_intermediaria += list(df['banca'].values())
    else:
        for bc in df['banca']:
            lista_intermediaria += list(bc.values())
    lista_final.append(lista_intermediaria)
    lista_intermediaria = []

with open('banca.csv', 'a') as f:
    filewriter = csv.writer(f, delimiter=',')
    for l in lista_final:
        filewriter.writerow(l)
