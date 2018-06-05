import csv
import json
import sys

delimiter = ','
rows = []
with open(sys.argv[1], newline='\n') as file:
    spamreader = csv.reader(file, delimiter=delimiter)
    for i, row in enumerate(spamreader):
        if i != 0:
            rows.append({
                "id": row[0],
                "title": row[1],
                "description": row[2],
            })
print(json.dumps(rows))
