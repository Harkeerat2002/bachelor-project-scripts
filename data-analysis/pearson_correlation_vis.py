import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics

def pearson_correlation_visualize():
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
    
    plt.plot(x, y, label='Pearson Correlation')
    plt.legend()
    plt.xlabel('Query')
    plt.ylabel('Pearson Correlation')
    plt.title('Query vs Pearson Correlation')
    plt.savefig('../results/graphs/pearson-correlation.png')
    print("Done")
    

def average():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Pearson Correlation']
        reader = csv.DictReader(csvfile)
        total = 0
        count = 0
        for row in reader:
            total += float(row['Pearson Correlation'])
            count += 1
        average = total / count
        print("Average = ", average)
        return average
    
def max():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Pearson Correlation']
        reader = csv.DictReader(csvfile)
        max = 0
        for row in reader:
            if float(row['Pearson Correlation']) > max:
                max = float(row['Pearson Correlation'])
        print("Max = ", max)
        return max

def min():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Pearson Correlation']
        reader = csv.DictReader(csvfile)
        min = 0
        for row in reader:
            if float(row['Pearson Correlation']) < min:
                min = float(row['Pearson Correlation'])
        print("min = ", min)
        return min

def median():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the values of row['Pearson Correlation']
        reader = csv.DictReader(csvfile)
        values = []
        for row in reader:
            values.append(float(row['Pearson Correlation']))
        # Calculate the median
        median = statistics.median(values)
        print("Median = ", median)
        return median


average()
max()
min()
median()