import pandas as pd

def DataPreprocessing():
    # read csv file from results folder
    gr = pd.read_csv('../results/Google-Results.csv')
    cr = pd.read_csv('../results/ChatGPT-Results.csv')

    # DATA PREPROCESSING
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

    return google_all_results, chatgpt_all_results