import numpy as np
from sklearn.feature_extraction.text import CountVectorizer



def CosineSimilarity(a, b):
    # Create CountVectorizer object
    vectorizer = CountVectorizer().fit_transform([a, b])

    # Get vectors for each sentence
    vector1 = np.array(vectorizer[0].todense())[0]
    vector2 = np.array(vectorizer[1].todense())[0]

    # Normalize vectors
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    # Compute cosine similarity
    cosine_similarity = np.dot(vector1, vector2) / (norm1 * norm2)

    return cosine_similarity
