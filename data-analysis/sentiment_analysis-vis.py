import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics

def chatGPT_Negative():
    with open ('../results/Sentiment-Analysis-Results-ChatGPT.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y_ = []
        for row in reader:
            y_.append(float(row['Negative']))
            
    plt.figure()
    plt.plot(x, y_, label='ChatGPT Negative Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Negative Sentiment')
    plt.title('Query vs Negative Sentiment')
    plt.savefig('../results/graphs/negative-sentiment-analysis-chatgpt.png')


def chatGPT_Neutral():
    with open ('../results/Sentiment-Analysis-Results-ChatGPT.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y_ = []
        for row in reader:
            y_.append(float(row['Neutral']))
    plt.figure()
    plt.plot(x, y_, label='ChatGPT Neutral Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Neutral Sentiment')
    plt.title('Query vs Neutral Sentiment')
    plt.savefig('../results/graphs/neutral-sentiment-analysis-chatgpt.png')

def chatGPT_Positive():
    with open ('../results/Sentiment-Analysis-Results-ChatGPT.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y_ = []
        for row in reader:
            y_.append(float(row['Positive']))
    plt.figure()  
    plt.plot(x, y_, label='ChatGPT Positive Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Positive Sentiment')
    plt.title('Query vs Positive Sentiment')
    plt.savefig('../results/graphs/positive-sentiment-analysis-chatgpt.png')


def chatGPT_Statistics():
    # Get Negative, Neutral, Positive Sentiment values
    negative = []
    neutral = []
    positive = []
    with open('../results/Sentiment-Analysis-Results-ChatGPT.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            negative.append(float(row['Negative']))
            neutral.append(float(row['Neutral']))
            positive.append(float(row['Positive']))

    # Calculate Average, Max, Min, Median for Negative, Neutral, Positive Sentiment values
    avg_negative = sum(negative) / len(negative)
    avg_neutral = sum(neutral) / len(neutral)
    avg_positive = sum(positive) / len(positive)

    max_negative = max(negative)
    max_neutral = max(neutral)
    max_positive = max(positive)

    min_negative = min(negative)
    min_neutral = min(neutral)
    min_positive = min(positive)

    median_negative = statistics.median(negative)
    median_neutral = statistics.median(neutral)
    median_positive = statistics.median(positive)

    # Print the results
    print("ChatGPT Sentiment Analysis Statistics:")
    print("Negative Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_negative, max_negative, min_negative, median_negative))
    print("Neutral Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_neutral, max_neutral, min_neutral, median_neutral))
    print("Positive Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_positive, max_positive, min_positive, median_positive))        
    print()
def google_negative():
    with open ('../results/Sentiment-Analysis-Results-Google.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y = []
        average = 0
        query = "when was the last time capulin erupted\n"
        all_queries = []
        all_queries.append(query)
        for row in reader:
            if row['User Query'] == query:
                average += float(row['Negative'])
            else:
                y.append(average / 5)
                average = float(row['Negative'])
                query = row['User Query']
                all_queries.append(query)
                
        y.append(average / 5)
    
    # print(len(all_queries))
    plt.figure()
    plt.plot(x, y, label='Google Negative Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Negative Sentiment')
    plt.title('Query vs Negative Sentiment')
    plt.savefig('../results/graphs/negative-sentiment-analysis-google.png')
    
def google_neutral():
    with open ('../results/Sentiment-Analysis-Results-Google.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y = []
        average = 0
        query = "when was the last time capulin erupted\n"
        for row in reader:
            if row['User Query'] == query:
                average += float(row['Neutral'])
            else:
                y.append(average / 5)
                average = float(row['Neutral'])
                query = row['User Query']
                
        y.append(average / 5)
    plt.figure()
    plt.plot(x, y, label='Google Neutral Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Neutral Sentiment')
    plt.title('Query vs Neutral Sentiment')
    plt.savefig('../results/graphs/neutral-sentiment-analysis-google.png')

def google_positive():
    with open ('../results/Sentiment-Analysis-Results-Google.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        x = np.arange(0, 77, 1)
        y = []
        average = 0
        query = "when was the last time capulin erupted\n"
        for row in reader:
            if row['User Query'] == query:
                average += float(row['Positive'])
            else:
                y.append(average / 5)
                average = float(row['Positive'])
                query = row['User Query']
                
        y.append(average / 5)
    plt.figure()
    plt.plot(x, y, label='Google Positive Sentiment Analysis')
    plt.legend()
    plt.xlabel('User Query')
    plt.ylabel('Positive Sentiment')
    plt.title('Query vs Positive Sentiment')
    plt.savefig('../results/graphs/positive-sentiment-analysis-google.png')

def google_statistics():
    # Get Negative, Neutral, Positive Sentiment values
    negative = []
    neutral = []
    positive = []
    with open('../results/Sentiment-Analysis-Results-Google.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            negative.append(float(row['Negative']))
            neutral.append(float(row['Neutral']))
            positive.append(float(row['Positive']))

    # Calculate Average, Max, Min, Median for Negative, Neutral, Positive Sentiment values
    avg_negative = sum(negative) / len(negative)
    avg_neutral = sum(neutral) / len(neutral)
    avg_positive = sum(positive) / len(positive)

    max_negative = max(negative)
    max_neutral = max(neutral)
    max_positive = max(positive)

    min_negative = min(negative)
    min_neutral = min(neutral)
    min_positive = min(positive)

    median_negative = statistics.median(negative)
    median_neutral = statistics.median(neutral)
    median_positive = statistics.median(positive)

    # Print the results
    print("Negative Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_negative, max_negative, min_negative, median_negative))
    print("Neutral Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_neutral, max_neutral, min_neutral, median_neutral))
    print("Positive Sentiment: Average = {:.2f}, Max = {:.2f}, Min = {:.2f}, Median = {:.2f}".format(avg_positive, max_positive, min_positive, median_positive))
                
    
    
if __name__ == '__main__':
    # Run all the functions
    chatGPT_Negative()
    chatGPT_Neutral()
    chatGPT_Positive()
    chatGPT_Statistics()
    google_negative()
    google_neutral()
    google_positive()
    google_statistics()
        