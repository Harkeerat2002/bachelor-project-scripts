
import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics


def cosine_similairty():    
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        user_query = "when was the last time capulin erupted"
        data = []
        average = 0
        for row in reader:
            # print(row['User Query'], row['Cosine Similarity'])
            # y.append(len(row['Cosine Similarity']))
            
            if user_query == row['User Query']:
                average += float(row['Cosine Similarity'])
            else :
                data.append(average / 5)
                average = float(row['Cosine Similarity'])
                user_query = row['User Query']
        data.append(average / 5)
        
    return data
   

def euclidean__similairty():    
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        user_query = "when was the last time capulin erupted"
        data = []
        average = 0
        for row in reader:
            # print(row['User Query'], row['Cosine Similarity'])
            # y.append(len(row['Cosine Similarity']))
            
            if user_query == row['User Query']:
                average += float(row['Euclidean Similarity'])
            else :
                data.append(average / 5)
                average = float(row['Euclidean Similarity'])
                user_query = row['User Query']
        data.append(average / 5)
    return data


def jaccard_similarity():
    x = np.arange(0, 77, 1)
    y = []
    
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        average = 0
        user_query = "when was the last time capulin erupted"
        for row in reader:
            # print(row['User Query'], row['Cosine Similarity'])
            # y.append(len(row['Cosine Similarity']))
            
            if user_query == row['User Query']:
                average += float(row['Jaccard Similarity'])
            else :
                y.append(average / 5)
                average = float(row['Jaccard Similarity'])
                user_query = row['User Query']
        y.append(average / 5)
    
    return y

def pearson_correlation():
    x = np.arange(0, 77, 1)
    y = []
    
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        average = 0
        user_query = "when was the last time capulin erupted"
        for row in reader:
            # print(row['User Query'], row['Cosine Similarity'])
            # y.append(len(row['Cosine Similarity']))
            
            if user_query == row['User Query']:
                average += float(row['Pearson Correlation'])
            else :
                y.append(average / 5)
                average = float(row['Pearson Correlation'])
                user_query = row['User Query']
        y.append(average / 5)
    
    return y
    
    
def box_graph():
    euclidean_data = euclidean__similairty()
    cosine_data = cosine_similairty()
    jacard_data = jaccard_similarity()
    
    fig, ax = plt.subplots()
    ax.boxplot([euclidean_data, cosine_data, jacard_data])
    ax.set_xticklabels(['Euclidean', 'Cosine', 'Jaccard'])
    ax.set_xlabel('Similarity Function')
    ax.set_ylabel('Similarity')
    ax.set_title('Query vs Similarity')
    plt.savefig('../results/graphs/cosine-similarity-box.png')
    print("Done")

box_graph()