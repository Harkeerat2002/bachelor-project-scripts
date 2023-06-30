# Libraries
import requests
import json
import csv


API_KEY = 'API_KEY'
SEARCH_ENGINE_KEY = 'SEARCH_ENGINE_KEY'


def google_search_api():
    print("Google Search API")
    # Read the queries from the file
    with open('../results/Children-Queries.txt', 'r') as f:
        queries = f.readlines()

    # Remove the \n from the end of each query
    queriesWithPlus = []
    for i in range(len(queries)):
        queriesWithPlus.append(queries[i].replace(' ', '+'))

    # Get the data from the api
    allData = []

    index = 0
    for i in range(len(queriesWithPlus)):
        
        response = requests.get('https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_KEY + '&q=' + queriesWithPlus[i] + '&num=5')
        JSON = response.json()

        # Checking if JSON is empty
        if not JSON:
            print("Empty JSON ", index)
            continue
        else:
            try:
                for item in JSON["items"]:
                    if "snippet" in item:
                        data = {
                            'session_id': index,
                            'user_query': queries[i],
                            'url': item["link"],
                            'title': item["title"],
                            'snippet': item["snippet"],
                        }
                        print("Query ", index, " done.")
                        allData.append(data)
                index += 1
            except Exception as e:
                print("An error occured ", index)
                # print(JSON)
                print(e)
                continue

    # Output allData in json file
    with open('./data/raw_data.json', 'w') as outfile:
        json.dump(allData, outfile)
    
    get_data_from_csv()
    

def get_data_from_csv():
    # Read the data from data.json
    with open('./data/raw_data.json') as json_file:
        data = json.load(json_file)
    
    # Remove \u2013 from the data
    for item in data:
        item['snippet'] = item['snippet'].encode('ascii', 'ignore').decode('ascii')

    #Remove the plus between the workds in the user_query
    for item in data:
        item['user_query'] = item['user_query'].replace('+', ' ')

    # Open the csv file
    with open('../results/Google-API-Output.csv', 'w', newline='') as csvfile:
        fieldnames = ['session_id', 'user_query', 'url', 'title', 'snippet']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

google_search_api()