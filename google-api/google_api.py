#Libraries
import requests
import json



API_KEY = 'ADD_YOUR_API_KEY_HERE'
SEARCH_ENGINE_KEY = 'ADD_YOUR_SEARCH_ENGINE_KEY_HERE'


with open('./data/children-queries.txt', 'r') as f:
    queries = f.readlines()

queriesWithPlus = []

for i in range(len(queries)):
    queriesWithPlus.append(queries[i].replace(' ', '+'))

allData = []


index = 0
for i in range(len(queriesWithPlus)):
    response = requests.get('https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_KEY + '&q=' + queriesWithPlus[i] + '&num=5')
    JSON = response.json()

    for item in JSON["items"]:    
        if "snippet" in item:  
            data = {
                'session_id': index,
                'user_query': queries[i],
                'url': item["link"],
                'source': 'NR',
                'title': item["title"],
                'snippet': item["snippet"],
            }
            print(index)
            allData.append(data)
    index += 1

# Output allData in json file
with open('./raw_data.json', 'w') as outfile:
    json.dump(allData, outfile)
    


