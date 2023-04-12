# Read the csv file in data
import csv


queries = []
queriesWithPlus = []
# open the csv file
with open('./data/old-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # read the row called 'user_query'
    for row in reader:
        queries.append(row['user_query'])
    # print len(queries)
    print(len(queries))
    # go through queries and remove duplicates
    queries = list(set(queries))
    

    # put + between words
    queriesWithPlus = queries
    for i in range(len(queries)):
        queriesWithPlus[i] = queriesWithPlus[i].replace(' ', '+')
       
    #return queries, queriesWithPlus
