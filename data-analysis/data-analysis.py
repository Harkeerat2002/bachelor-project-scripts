import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy

def compare_query():
    google_file = '../results/Google-API-Output.csv'
    chatgpt_file = '../results/ChatGPT-API-Output.csv'

    # read the queries from the Google file
    google_queries = set()
    with open(google_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            google_queries.add(row['user_query'])
    print(len(google_queries))

    # read the queries from the ChatGPT file
    chatgpt_queries = set()
    with open(chatgpt_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chatgpt_queries.add(row['query'])
    print(len(chatgpt_queries))

    # Remove the \n from the end of each query
    google_queries = [query.replace('\n', '') for query in google_queries]
    chatgpt_queries = [query.replace('\n', '') for query in chatgpt_queries]

    # # find the missing queries
    for query in chatgpt_queries:
        if query not in google_queries:
            print(query)
                        
def top_words_comparison():
    pass

# Named Entity Recognition
def named_entity_recognition():
    nlp = spacy.load("en_core_web_sm")
    
    #ChatGPT Analysis
    with open('../results/ChatGPT-API-Output.csv', 'r', newline='') as csvfile:
        with open('../results/ChatGPT-NER.csv', 'w', newline='') as f:
            reader = csv.DictReader(csvfile)
            writer = csv.writer(f)
            
            writer.writerow(['query', 'entity', 'label'])
            for i, row in enumerate(reader):
                doc = nlp(row['response'])
                x = 0
                for ent in doc.ents:
                    x += 1
                    writer.writerow([row['query'], ent.text, ent.label_])
                if x == 0:
                    writer.writerow([row['query'], 'None', 'None'])
                print("Query ", i, " done.")
                
    print("ChatGPT Analysis Done.")
    
    # Google Analysis
    with open('../results/Google-API-Output.csv', 'r', newline='') as csvfile:
        with open('../results/Google-NER.csv', 'w', newline='') as f:
            reader = csv.DictReader(csvfile)
            writer = csv.writer(f)
            
            writer.writerow(['query', 'entity', 'label'])
            for s, row in enumerate(reader):
                doc = nlp(row['snippet'])
                for ent in doc.ents:
                    writer.writerow([row['user_query'], ent.text, ent.label_])
                print("Query ", s, " done.")
            
    
     
#google_length_analysis()
named_entity_recognition()

