import openai
import csv

# Set the OpenAI API key
openai.api_key = "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"

def chatgpt_api():
    # Read the queries from the file
    with open('../results/Children-Queries.txt', 'r') as f:
        queries = f.read().splitlines()

    # Initialize the response text
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
            print("An error occured", index)
            print(e)
        

    # Writing to a csv file
    with open('../results/ChatGPT-API-Output.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=response_text.keys())
        writer.writeheader()
        writer.writerows(response_list)

chatgpt_api()

