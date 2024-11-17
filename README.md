# Google Search vs. Conversational AI: A Comparative Analysis
***Harkeerat Singh Sawhney***

## Introduction
This repository contains the scripts used for the Bachelor Project *Analyzing and Mitigating Information Pollution and Hallucinations in Children's Online Search Behavior: A Comparative Study between Google and ChatGPT*. This Project is a part of the Bachelor's Degree in Computer Science at the USI (Università della Svizzera italiana) Lugano, Switzerland.

## Project Description:
The objective of this project is to investigate and classify the occurrences of information pollution and hallucinations in children's online search behavior. The project aims to analyze search results retrieved from Google APIs and compare them with responses generated from conversational AI models like ChatGPT. By doing so, the project seeks to identify and classify the information pollution and hallucination patterns in children's online search behavior and propose possible solutions to mitigate them. The project also aims to investigate whether ChatGPT yields more pertinent outcomes compared to conventional methods of browsing, such as using Google. For the comparison, tools would be developed which would make it easier to come up with results.

## API Implementation:
### Google Search API
I am using the Google Search API to retrieve the results from the queries. The API is a part of the Google Custom Search API. The API is used to retrieve search results from Google Search. The API is a RESTful API that returns JSON-formatted results. The API can be used to retrieve search results from Google Search, Google Images, Google News, Google Books, and Google Videos. The API can also be used to retrieve search results from custom search engines that you create.

The API key is not provided, and that has to be obtained from the Google Custom Search API.

### ChatGPT OpenAI API
I am using the OpenAI API to retrieve the results from the queries. The API is a part of the OpenAI API. In the OpenAI API I am using it with `gpt-3.5-turbo` model.

The API key is not provided, and that has to be obtained from the OpenAI API.

## Likelhood Function Implementation:
### Jaccard Similarity Coefficient
The Jaccard similarity coefficient is a measure of similarity between two sets of data. It is calculated by dividing the size of the intersection of two sets by the size of their union.

In other words, it measures how similar two sets or objects are by comparing their common elements to their total elements. The coefficient ranges from 0 to 1, where 0 means no similarity and 1 means complete similarity.

The Jaccard similarity coefficient can be used for various purposes, such as comparing text documents, binary vectors, or images. It is commonly used in data mining and information retrieval to compare the similarity of two sets of data.

## Machine Learning Model Implementation:
Basic Machine Learning models are implemented to classify the results. The results are classified into two categories: *Relevant* and *Irrelevant*. This is done by spliting the training data into features and a targer variable using Pandas DataFrame indexing. 

The text data is preprocessed using CountVectorizer from the Scikit-learn library to convert the text data into numerical features that can be used to train a machine learning model. The text data is transformed by creating a vocabulary of words and then counting the number of times each word appears in each document (user_query and snippet).

The data is then split into training and testing sets using Scikit-learn's train_test_split function. The data is divided into a training set and a testing set so that the model can be trained on a subset of the data and evaluated on the remaining unseen data.

A logistic regression model is then trained on the training data using Scikit-learn's LogisticRegression function. The model is fit to the training data and then used to predict the target variable for the testing data.

The performance of the model is evaluated on the testing data using Scikit-learn's classification_report function. This function returns several metrics such as precision, recall, and F1 score that can be used to evaluate the performance of the model.

Finally, the trained model and CountVectorizer are saved using the numpy.save function. These saved files can be used to make predictions on new data without having to retrain the model and preprocess the data.

The code can be found in `search_relevance.ipynb` notebook. Along with that the `predicting_relevance.py` contains the code to predict the relevance of the results, by using the trained module.

## Scripts:
- `search_relevance.ipynb`
- `predicting_relevance.py`
- `search_results.py`
- `search_results.csv`

## Results:

All the results are stored under the directory `results`. 

## Python Libraries Needed:
I am using Python 3.8.5. With Python installed, I am using Conda to manage the environment. The following libraries are needed to run the scripts:
```bash
conda install -c conda-forge openai
conda install pandas 
```