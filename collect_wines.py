
import pandas as pd
from collections import defaultdict


def wines_processing(path):
    wines_excel = pd.read_excel(path, keep_default_na=False)
    wines_json = wines_excel.to_dict(orient='records')

    wines = defaultdict(list)
    for wine in wines_json:
        wines[wine['Категория']] = [item for item in wines_json if item['Категория'] == wine['Категория']]

    return wines

