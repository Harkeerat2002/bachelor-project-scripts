import jaccard_similarity_likelihood as js
import cosine_similarity as cs
import euclidean_similarity as es
import pearson_correlation as pc
import csv
import sys

sys.path.append('../data-preprocess')
from data_preprocessing import DataPreprocessing


comparsion = []

# DATA PREPROCESSING
google_all_results, chatgpt_all_results = DataPreprocessing()

# SIMILARITY ANALYSIS
comparsion = []
for chatgpt_result in chatgpt_all_results:
    for google_result in google_all_results:

        if chatgpt_result["user_query"] == google_result["user_query"]:
            comparsion_result = {
                "user_query": chatgpt_result["user_query"],
                "chatgpt_result": chatgpt_result["result"][0],
                "google_result": google_result["result"],
                "result": {
                    "jaccard_similarity": [],
                    "cosine_similarity": [],
                    "euclidean_similarity": [],
                    "pearson_correlation": []
                },
            }
            for r in google_result["result"]:
                # SIMILARITY ANALYSIS
                jaccard_similarity = js.JaccardSimilarity(chatgpt_result["result"][0], r)
                cosine_similarity = cs.CosineSimilarity(chatgpt_result["result"][0], r)
                euclidean_similarity = es.EuclideanSimilarity(chatgpt_result["result"][0], r)
                pearson_correlation = pc.PearsonCorrelation(chatgpt_result["result"][0], r)

                comparsion_result["result"]["jaccard_similarity"].append(jaccard_similarity)
                comparsion_result["result"]["cosine_similarity"].append(cosine_similarity)
                comparsion_result["result"]["euclidean_similarity"].append(euclidean_similarity)
                comparsion_result["result"]["pearson_correlation"].append(pearson_correlation)
                
                # # DEBUGING PURPOSES
                # print("User Query: ", chatgpt_result["user_query"])
                # print("Jaccard Similarity: ", jaccard_similarity)
                # print("Cosine Similarity: ", cosine_similarity)
                # print("Euclidean Similarity: ", euclidean_similarity)
                # print("Pearson Correlation: ", pearson_correlation)
                # print("--------------------------------------------------")

            comparsion.append(comparsion_result)
            

# PRINT RESULTS TO CSV FILE
with open('../results/Similarity-Analysis-Results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User Query", "ChatGPT Result", "Google Result", "Jaccard Similarity", "Cosine Similarity", "Euclidean Similarity", "Pearson Correlation"])
    for c in comparsion:
        for i in range(len(c["result"]["jaccard_similarity"])):
            writer.writerow([c["user_query"], c["chatgpt_result"], c["google_result"][i], c["result"]["jaccard_similarity"][i], c["result"]["cosine_similarity"][i], c["result"]["euclidean_similarity"][i], c["result"]["pearson_correlation"][i]])

print("Similarity Analysis Results are saved to results/Similarity-Analysis-Results.csv")
