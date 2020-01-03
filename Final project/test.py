import os
import json

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
os.chdir(file_path)

f = open('Final project/Resource/Map/Obs.json')
data = json.load(f)
print(type(data))

with open('Final project/Resource/Map/Obs.json', 'w+', encoding='utf-8') as f:

    b = json.dump(data*2, f, ensure_ascii=False)
