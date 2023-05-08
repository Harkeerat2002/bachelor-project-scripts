def JaccardSimilarity(a, b):
    a = set(a["result"][0].split())
    b = set(b.split())
    intersection = len(a.intersection(b))
    union = len(a.union(b))
    jaccard_similarity = intersection / union
    return jaccard_similarity