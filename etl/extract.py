import json

import pandas as pd
import requests


def get_data(url: str):
    request = requests.get(url)
    return request.json()


link = "https://servicodados.ibge.gov.br/api/v2/malhas/35/?resolucao=5&formato=application/vnd.geo+json&qualidade=4"


dataset = pd.read_json(json.dumps(get_data(link)))
dataset.head(2)
