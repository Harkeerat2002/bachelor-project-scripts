import pandas as pd
import json

# read csv file from results folder
gr = pd.read_csv('../results/Google-Results.csv')
cr = pd.read_csv('../results/ChatGPT-Results.csv')


single_result = {
    "user_query": "",
    "result": []
    }

google_all_results = []
temp_google_single_result = single_result.copy()
i = 0
for index, row in gr.iterrows():
    # remove /n from user_query
    row["user_query"] = row["user_query"].replace("\n", "")
    if temp_google_single_result["user_query"] == row["user_query"] and i < 4:
        temp_google_single_result["user_query"] = row["user_query"]
        temp_google_single_result["result"].append(row["snippet"])
        i += 1

    else:
        temp_google_single_result = single_result.copy()
        temp_google_single_result["user_query"] = row["user_query"]
        temp_google_single_result["result"] = [row["snippet"]]
        google_all_results.append(temp_google_single_result.copy())
        i = 0


chatgpt_all_results = []
temp_chatgpt_single_result = single_result.copy()
for index, row in cr.iterrows():
    temp_chatgpt_single_result = single_result.copy()
    temp_chatgpt_single_result["user_query"] = row["query"]
    temp_chatgpt_single_result["result"] = [row["response"]]
    chatgpt_all_results.append(temp_chatgpt_single_result.copy())

comparsion = []
for chatgpt_result in chatgpt_all_results:
    for google_result in google_all_results:
        
        if chatgpt_result["user_query"] == google_result["user_query"]:            
            comparsion_result = {
                "user_query": chatgpt_result["user_query"],
                "common_result": [],
                "average": 0
            } 
            for r in google_result["result"]:
                    # Jaccard Similarity Implementation
                    a = set(chatgpt_result["result"][0].split())
                    b = set(r.split())
                    intersection = len(a.intersection(b))
                    union = len(a.union(b))
                    jaccard_similarity = intersection / union
                    comparsion_result_single = jaccard_similarity
                    comparsion_result["common_result"].append(comparsion_result_single)
            comparsion.append(comparsion_result)
            # Average of common results
            average = sum(comparsion_result["common_result"]) / len(comparsion_result["common_result"])
            comparsion_result["average"] = average
            
print(comparsion)


                

