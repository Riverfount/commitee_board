import csv
import json
import os
from collections import OrderedDict

path = os.curdir
pathfile = os.path.join(path, 'banca.json')

with open(pathfile) as f:
    data = json.load(f)

d = OrderedDict()

for l in data:
    d.setdefault((l['url'],), list()).append({'nome': l['nome'].title(), 'categoria': l['categoria'].title()})

new_dict = [{'url': k[0], 'banca': v.pop() if len(v) == 1 else v} for k, v in d.items()]

lista_intermediaria = []
lista_final = [['url', 'professor1', 'categoria1', 'professor2', 'categoria2', 'professor3', 'categoria3',
               'professor4', 'catetoria4']]

for nd in new_dict:
    lista_intermediaria += [nd['url']]
    for bc in nd['banca']:
        lista_intermediaria += list(bc.values())
    lista_final.append(lista_intermediaria)
    lista_intermediaria = []

with open('banca.csv', 'a') as f:
    filewriter = csv.writer(f, delimiter=',')
    for l in lista_final:
        filewriter.writerow(l)
