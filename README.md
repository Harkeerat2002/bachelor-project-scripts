# Bachelor Project Scripts
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


## Python Libraries Needed:
I am using Python 3.8.5. With Python installed, I am using Conda to manage the environment. The following libraries are needed to run the scripts:
```bash
conda install -c conda-forge openai
conda install pandas 
```