import pandas as pd
import json
from collections import defaultdict


def wines_processing(path):
    wines_excel = pd.read_excel(path)
    wines_json = json.loads(wines_excel.to_json(orient='records', force_ascii=False))

    wines = defaultdict(list)
    for wine in wines_json:
        wines[wine['Категория']] = [item for item in wines_json if item['Категория'] == wine['Категория']]

    return wines

