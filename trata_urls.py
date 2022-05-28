import csv
import os
from pprint import pprint

path = os.curdir
filepath = os.path.join(path, 'url_catalogofilosofia.csv')

urls = []

for row in open(filepath).readlines():
    if row.startswith('https://sucupira.capes.gov.br/sucupira/'):
        urls.append([row.strip()])

with open('url.csv', 'a') as f:
    filewriter = csv.writer(f)
    for url in urls:
        filewriter.writerow(url)
