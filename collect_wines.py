import pandas as pd
from collections import defaultdict
import json


def processing_wines(path):
    wines_excel = pd.read_excel(path, keep_default_na=False)
    wines_before_processing = wines_excel.to_dict(orient='records')

    wines = defaultdict(list)
    for wine in wines_before_processing:
        wines[wine['Категория']].append(wine)

    return wines
