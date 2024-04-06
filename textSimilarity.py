from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample data (replace with your own dataset)
predefinedStories = [
    'Once upon a time, there was a princess who lived in a castle.',
    'In a faraway land, there was a brave knight who fought dragons.',
    'Long ago, in a magical forest, there was a wise wizard with extraordinary powers.'
]
inputSentence = 'A knight embarked on a quest to rescue a princess.'

# Preprocess data
def preprocess(text):
    text = text.lower()
    text = text.replace('.', '')
    text = text.replace(',', '')
    return text

predefinedStories = [preprocess(story) for story in predefinedStories]
inputSentence = preprocess(inputSentence)

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(predefinedStories + [inputSentence])

# Calculate cosine similarity between input sentence and predefined stories
similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])


numStories = 3
# Find the index of the most similar story
closestStories = np.argpartition(similarities[0], -numStories)[-numStories:]
closestStories = closestStories[np.argsort(similarities[0][closestStories])][::-1]


for index in closestStories:
    print(f"story #{index}:") 
    print(predefinedStories[index])