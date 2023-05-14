import gensim
from gensim import corpora
from pprint import pprint

# Define the example corpus
corpus = ['The cat sat on the mat.',
          'The dog chased the cat.',
          'The mouse ran away from the cat and the dog.',
          'The cat and the dog slept together.']

# Tokenize the corpus
tokens = [gensim.utils.simple_preprocess(doc) for doc in corpus]

# Create a dictionary from the tokens
dictionary = corpora.Dictionary(tokens)

# Create a corpus from the dictionary
corpus_bow = [dictionary.doc2bow(doc) for doc in tokens]

# Define the number of topics to extract
num_topics = 2

# Build the LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus_bow,
                                            id2word=dictionary,
                                            num_topics=num_topics,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=10,
                                            passes=10,
                                            alpha='auto',
                                            per_word_topics=True)

# Print the extracted topics and their corresponding words
pprint(lda_model.print_topics())
