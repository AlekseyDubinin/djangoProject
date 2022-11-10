import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)


csvFilePath = r'ads.csv'
jsonFilePath = r'ads.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'categories.csv'
jsonFilePath = r'categories.json'
csv_to_json(csvFilePath, jsonFilePath)