import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics

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
                
def named_entity_recognition_line():
    x = np.arange(0, 77, 1)
    y_google = []
    y_chatgpt = []
    number_of_entity = 0
    query_google = "when was the last time capulin erupted\r\n"
    query_chatGPT = "when was the last time capulin erupted"
    
    with open ('../results/Google-NER.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query_google == row['query']:
                number_of_entity += 1
            else:
                y_google.append(number_of_entity)
                number_of_entity = 1
                query_google = row['query']
                
    y_google.append(number_of_entity)
    
    with open ('../results/ChatGPT-NER.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query_chatGPT == row['query']:
                number_of_entity += 1
            else:
                y_chatgpt.append(number_of_entity)
                number_of_entity = 1
                query_chatGPT = row['query']
    y_chatgpt.append(number_of_entity)
    

    plt.plot(x, y_google, label='Google NER')
    plt.plot(x, y_chatgpt, label='ChatGPT NER')
    plt.legend()
    plt.xlabel('Query')
    plt.ylabel('Number of Entities')
    plt.title('Query vs Number of Entities')
    
    plt.savefig('../results/graphs/number-of-entities.png')
    

def statistical_analysis():
    y_google = []
    y_chatgpt = []
    number_of_entity = 0
    query_google = "when was the last time capulin erupted\r\n"
    query_chatGPT = "when was the last time capulin erupted"
    
    dict_chatgpt = {}
    dict_google = {}
    
    with open ('../results/Google-NER.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query_google == row['query']:
                number_of_entity += 1
                if row['label'] in dict_google:
                    dict_google[row['label']] = dict_google[row['label']] + 1
                else:
                    dict_google[row['label']] = 1
            else:
                y_google.append(number_of_entity)
                number_of_entity = 1
                query_google = row['query']
                if row['label'] in dict_google:
                    dict_google[row['label']] = dict_google[row['label']] + 1
                else:
                    dict_google[row['label']] = 1
                
    y_google.append(number_of_entity)
    
    with open ('../results/ChatGPT-NER.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if query_chatGPT == row['query']:
                number_of_entity += 1
                if row['label'] in dict_chatgpt:
                    dict_chatgpt[row['label']] = dict_chatgpt[row['label']] + 1
                else:
                    dict_chatgpt[row['label']] = 1
            else:
                y_chatgpt.append(number_of_entity)
                number_of_entity = 1
                if row['label'] in dict_chatgpt:
                    dict_chatgpt[row['label']] = dict_chatgpt[row['label']] + 1
                else:
                    dict_chatgpt[row['label']] = 1
                query_chatGPT = row['query']
    y_chatgpt.append(number_of_entity)     
    
    # Get the Average:
    google_average = statistics.mean(y_google)
    chatgpt_average = statistics.mean(y_chatgpt) 
    
    
    # Get the top 5 entities for each model
    google_entities = sorted(dict_google.items(), key=lambda x: x[1], reverse=True)[:5]
    chatgpt_entities = sorted(dict_chatgpt.items(), key=lambda x: x[1], reverse=True)[:5] 
    
    print("Google Average: ", google_average)
    print("ChatGPT Average: ", chatgpt_average)
    print("Google Top 5 Entities: ", google_entities)
    print("ChatGPT Top 5 Entities: ", chatgpt_entities)
    
    print("Google Entities: ", dict_google)
    print("ChatGPT Entities: ", dict_chatgpt)
    
               
                    
                        
named_entity_recognition_line()
statistical_analysis()