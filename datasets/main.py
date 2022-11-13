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


csvFilePath = r'ad.csv'
jsonFilePath = r'ad.json'
csv_to_json(csvFilePath, jsonFilePath)
csvFilePath = r'category.csv'
jsonFilePath = r'category.json'
csv_to_json(csvFilePath, jsonFilePath)

csvFilePath = r'location.csv'
jsonFilePath = r'location.json'
csv_to_json(csvFilePath, jsonFilePath)

csvFilePath = r'user.csv'
jsonFilePath = r'user.json'
csv_to_json(csvFilePath, jsonFilePath)