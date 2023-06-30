import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.stats import pearsonr

def PearsonCorrelation(a, b):
    # Create CountVectorizer object
    vectorizer = CountVectorizer().fit_transform([a, b])

    # Get vectors for each sentence
    vector1 = np.array(vectorizer[0].todense())[0]
    vector2 = np.array(vectorizer[1].todense())[0]

    # Normalize vectors
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    # Compute Pearson correlation
    pearson_correlation = pearsonr(vector1, vector2)[0]

    return pearson_correlation