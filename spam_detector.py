import pandas as pd

# Load the dataset
df = pd.read_csv('spam.csv')
print(df.head())  # To check the loaded data

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Features and Labels
X = df['message']  # The messages
y = df['label']    # The labels (spam or ham)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Model Training
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Predictions
predictions = model.predict(X_test_vectorized)

# Evaluation
print(metrics.classification_report(y_test, predictions))
print(df.columns)