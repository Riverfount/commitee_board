import json
import os
from collections import OrderedDict

path = os.curdir
path_source_file = os.path.join(path, 'banca.json')
path_destination_file = os.path.join(path, 'banca_sanitizada.json')

with open(path_source_file) as f:
    data = json.load(f)

d = OrderedDict()

for l in data:
    d.setdefault((l['url'],), list()).append({'nome': l['nome'].title(), 'categoria': l['categoria'].title()})

new_dict = [{'url': k[0], 'banca': v.pop() if len(v) == 1 else v} for k, v in d.items()]

with open(path_destination_file, 'w') as f:
    json.dump(new_dict, f)
