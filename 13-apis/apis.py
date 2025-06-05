# pip install requests pandas

import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"

resposta = requests.get(url)

print(resposta.status_code)

dados = resposta.json()

for i in dados:
    print(i['localized_name'])

df = pd.DataFrame(dados)
df.to_csv("heroes_dota.csv", sep = ";")
