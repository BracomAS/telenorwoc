import json
import pandas as pd

# Filstien til JSON-filen
json_file = "WoCReport_CwmProductionDetailedReport.json"

# Les JSON-dataene
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Konverter JSON til en Pandas DataFrame
df = pd.json_normalize(data)

# Eksporter til Excel
excel_file = "output.xlsx"
df.to_excel(excel_file, index=False)

print(f"JSON-data er eksportert til {excel_file}")
