
import nltk
import csv
import sys
import os
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def sentiment_analysis():

    # Get the current working directory
    current_directory = os.getcwd()

    # Specify the desired download location
    download_location = os.path.join(current_directory, 'vader_lexicon')

    # Download vader_lexicon to the specified location
    # nltk.download('vader_lexicon', download_dir=download_location)

    sys.path.append('../data-preprocess')
    from data_preprocessing import DataPreprocessing

    # DATA PREPROCESSING
    google_all_results, chatgpt_all_results = DataPreprocessing()
    
    print(len(google_all_results))

    # initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # example sentences
    comparsion_ChatGPT = []
    comparsion_Google = []

    # CHATGPT RESULTS
    for chatgpt_result in chatgpt_all_results:
        score = analyzer.polarity_scores(chatgpt_result["result"][0])
        comparsion_result = {
            "user_query": chatgpt_result["user_query"],
            "chatgpt_result": chatgpt_result["result"][0],
            "negative": score['neg'],
            "neutral": score['neu'],
            "positive": score['pos'],
            "compound": score['compound']
        }
        comparsion_ChatGPT.append(comparsion_result)

    # GOOGLE RESULTS
    for google_result in google_all_results:
        
        for r in google_result["result"]:
            print(r)
            # get sentiment scores for each sentence
            score = analyzer.polarity_scores(r)
            comparsion_result = {
                "user_query": google_result["user_query"],
                "google_result": google_result["result"],
                "negative": score['neg'],
                "neutral": score['neu'],
                "positive": score['pos'],
                "compound": score['compound']
            }
            comparsion_Google.append(comparsion_result)

    # PRINT RESULTS TO CSV FILE (CHATGPT)
    with open('../results/Sentiment-Analysis-Results-ChatGPT.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Query", "ChatGPT Result", "Negative", "Neutral", "Positive", "Compound"])
        for c in comparsion_ChatGPT:
            writer.writerow([c["user_query"], c["chatgpt_result"], c["negative"], c["neutral"], c["positive"], c["compound"]])

    # PRINT RESULTS TO CSV FILE (GOOGLE)
    with open('../results/Sentiment-Analysis-Results-Google.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Query", "Google Result", "Negative", "Neutral", "Positive", "Compound"])
        for c in comparsion_Google:
            writer.writerow([c["user_query"], c["google_result"], c["negative"], c["neutral"], c["positive"], c["compound"]])

    print("Sentiment Analysis Results are saved")
    
sentiment_analysis()