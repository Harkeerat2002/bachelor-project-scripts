# Read the data form data.json and put it in a csv file
import csv
import json

# Read the data from data.json
with open('./raw_data.json') as json_file:
    data = json.load(json_file)

#Remove the plus between the workds in the user_query
for item in data:
    item['user_query'] = item['user_query'].replace('+', ' ')

# Open the csv file
with open('./data/new_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['session_id', 'user_query', 'url', 'source', 'title', 'snippet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

