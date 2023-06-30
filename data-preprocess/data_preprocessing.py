import pandas as pd
import csv

def DataPreprocessing():
    # DATA PREPROCESSING
    single_result = {
        "user_query": "",
        "result": []
    }

    google_all_results = []
    temp_google_single_result = single_result.copy()
    i = 0
    
    with open ("../results/Google-API-Output.csv", "r") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            if temp_google_single_result["user_query"] == row[1] and i < 4:
                temp_google_single_result["user_query"] = row[1]
                temp_google_single_result["result"].append(row[4])
                i += 1
            else:
                temp_google_single_result = single_result.copy()
                temp_google_single_result["user_query"] = row[1]
                temp_google_single_result["result"] = [row[4]]
                google_all_results.append(temp_google_single_result.copy())
                i = 0
    
    chatgpt_all_results = []
    temp_chatgpt_single_result = single_result.copy()
    
    with open ("../results/ChatGPT-API-Output.csv", "r") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            temp_chatgpt_single_result = single_result.copy()
            temp_chatgpt_single_result["user_query"] = row[0]
            temp_chatgpt_single_result["result"] = [row[1]]
            chatgpt_all_results.append(temp_chatgpt_single_result.copy())
        
    
    
    # drop the first row
    google_all_results = google_all_results[1:]
    chatgpt_all_results = chatgpt_all_results[1:]
    return google_all_results, chatgpt_all_results
        
