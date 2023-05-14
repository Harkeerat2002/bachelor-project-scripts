import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

def EuclideanSimilarity(a, b):
    # Create CountVectorizer object
    vectorizer = CountVectorizer().fit_transform([a, b])

    # Get vectors for each sentence
    vector1 = np.array(vectorizer[0].todense())[0]
    vector2 = np.array(vectorizer[1].todense())[0]

    # Normalize vectors
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    normalized_vector1 = vector1 / norm1
    normalized_vector2 = vector2 / norm2

    # Compute the Euclidean distance between the two normalized vectors
    euclidean_similarity = 1 / (1 + euclidean_distances(normalized_vector1.reshape(1, -1), normalized_vector2.reshape(1, -1))[0][0])
    return euclidean_similarity