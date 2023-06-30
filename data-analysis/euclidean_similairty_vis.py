import numpy as np
import csv
import matplotlib.pyplot as plt
import spacy
import statistics

def euclidean_similairty_visualize():
    x = np.arange(0, 77, 1)
    y = []
    
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        average = 0
        user_query = "when was the last time capulin erupted"
        for row in reader:
            # print(row['User Query'], row['Euclidean Similarity'])
            # y.append(len(row['Euclidean Similarity']))
            
            if user_query == row['User Query']:
                average += float(row['Euclidean Similarity'])
            else :
                y.append(average / 5)
                average = float(row['Euclidean Similarity'])
                user_query = row['User Query']
        y.append(average / 5)
    
    plt.plot(x, y, label='Euclidean Similarity')
    plt.legend()
    plt.xlabel('Query')
    plt.ylabel('Euclidean Similarity')
    plt.title('Query vs Euclidean Similarity')
    plt.savefig('../results/graphs/euclidean-similarity.png')
    print("Done")
    

def average():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Euclidean Similarity']
        reader = csv.DictReader(csvfile)
        total = 0
        count = 0
        for row in reader:
            total += float(row['Euclidean Similarity'])
            count += 1
        average = total / count
        print("Average = ", average)
        return average
    
def max():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Euclidean Similarity']
        reader = csv.DictReader(csvfile)
        max = 0
        for row in reader:
            if float(row['Euclidean Similarity']) > max:
                max = float(row['Euclidean Similarity'])
        print("Max = ", max)
        return max

def min():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the average of row['Euclidean Similarity']
        reader = csv.DictReader(csvfile)
        min = 0
        for row in reader:
            if float(row['Euclidean Similarity']) < min:
                min = float(row['Euclidean Similarity'])
        print("min = ", min)
        return min

def median():
    with open('../results/Similarity-Analysis-Results.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Get the values of row['Euclidean Similarity']
        reader = csv.DictReader(csvfile)
        values = []
        for row in reader:
            values.append(float(row['Euclidean Similarity']))
        # Calculate the median
        median = statistics.median(values)
        print("Median = ", median)
        return median


average()
max()
min()
median()