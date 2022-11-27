import pandas as pd
import json
from collections import defaultdict


wines_excel_data = pd.read_excel('wine3.xlsx')
wines_json_data = json.loads(wines_excel_data.to_json(orient='records', force_ascii=False))

wines = defaultdict(list)
for wine in wines_json_data:
    wines[wine['Категория']] = [item for item in wines_json_data if item['Категория'] == wine['Категория']]

# print(json.dumps(wines, indent=4, ensure_ascii=False))
