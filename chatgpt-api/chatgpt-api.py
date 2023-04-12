import openai
import csv

openai.api_key = "ADD YOUR API KEY HERE"

with open('../results/Children-Queries.txt', 'r') as f:
    queries = f.read().splitlines()

response_text = {
    "query": "",
    "response": ""
}

response_list = []

for index, query in enumerate(queries):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},                
            ]
        
        )

        response_text["query"] = query
        response_text["response"] = response["choices"][0]["message"]["content"]
        response_list.append(response_text.copy())
        print("Query ", index, " done.")
    except Exception as e:
        response_text["query"] = query
        response_text["response"] = "Error"
        response_list.append(response_text.copy())
        print("An error occured")
        print(e)
    

# Writing to a csv file
with open('chatgpt-api-output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=response_text.keys())
    writer.writeheader()
    writer.writerows(response_list)



