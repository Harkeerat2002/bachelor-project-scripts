import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics

def google_length_analysis_visualize():
    # x is from 0 to 75
    x = np.arange(0, 77, 1)

    y = []
    with open('../results/Google-API-Output.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        average = 0
        id = 0
        for row in reader:
            if id == int(row['session_id']):
                # print(len(row['snippet']), row['session_id'])
                average += len(row['snippet'])
            else:
                y.append(average / 5)
                average = len(row['snippet'])
                id += 1
        y.append(average / 5)
    
    chatgpt_lenght_analysis_visualize(x, y)

def chatgpt_lenght_analysis_visualize(x, y):
    x_chatGPT = np.arange(0, 77, 1)
    y_chatGPT = []
    with open('../results/ChatGPT-API-Output.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['query'], len(row['response']))
            y_chatGPT.append(len(row['response']))
    
    print(y_chatGPT)
    plt.plot(x_chatGPT, y_chatGPT, label='ChatGPT Query')
    plt.plot(x, y, label='Google Query')
    plt.legend()
    
    plt.xlabel('Query')
    plt.ylabel('Length of Query Response')
    plt.title('Query vs Length of Query Response')

    plt.savefig('../results/graphs/length-of-snippet.png')

def google_length_statistics():
    y = []
    with open('../results/Google-API-Output.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        average = 0
        id = 0
        for row in reader:
            if id == int(row['session_id']):
                # print(len(row['snippet']), row['session_id'])
                average += len(row['snippet'])
            else:
                y.append(average / 5)
                average = len(row['snippet'])
                id += 1
        y.append(average / 5)
    
    # Calculate the Average:
    print("Average: ", sum(y) / len(y))
    # Calculate the Median:
    print("Median: ", statistics.median(y))
    # Calculate the Minimum:
    print("Minimum: ", min(y))
    # Calculate the Maximum:
    print("Maximum: ", max(y))

def chatGPT_length_statistics():

    y_chatGPT = []
    with open('../results/ChatGPT-API-Output.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['query'], len(row['response']))
            y_chatGPT.append(len(row['response']))
    
    
    # Calculate the Average:
    print("Average: ", sum(y_chatGPT) / len(y_chatGPT))
    # Calculate the Median:
    print("Median: ", statistics.median(y_chatGPT))
    # Calculate the Minimum:
    print("Minimum: ", min(y_chatGPT))
    # Calculate the Maximum:
    print("Maximum: ", max(y_chatGPT))

google_length_statistics()
chatGPT_length_statistics()