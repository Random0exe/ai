import nltk
import random
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download the required NLTK resources
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Load the movie reviews dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
random.shuffle(documents)

# Extract features from the documents
all_words = nltk.FreqDist(word.lower() for word in movie_reviews.words())
stop_words = set(stopwords.words('english'))

# Select the most common words as features
word_features = list(all_words.keys())[:2000]

# Define a function to extract features from a document
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

# Extract features for all documents
featuresets = [(document_features(doc), category) for (doc, category) in documents]

# Split the dataset into training and testing sets
train_set = featuresets[:1500]
test_set = featuresets[1500:]

# Train a logistic regression classifier
classifier = nltk.classify.SklearnClassifier(LogisticRegression())
classifier.train(train_set)

# Perform sentiment analysis on test set
y_true = [category for (features, category) in test_set]
y_pred = classifier.classify_many([features for (features, category) in test_set])

# Calculate accuracy score
accuracy = accuracy_score(y_true, y_pred)
print("Accuracy:", accuracy)
