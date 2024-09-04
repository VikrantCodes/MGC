import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load training data
df = pd.read_csv('training_data.csv')

# Vectorize words
vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 3))
X = vectorizer.fit_transform(df['Word'])

# Encode POS and Gender labels
le_pos = LabelEncoder()
le_gender = LabelEncoder()

y_pos = le_pos.fit_transform(df['POS'])
y_gender = le_gender.fit_transform(df['Gender'])

# Train/test split
X_train, X_test, y_pos_train, y_pos_test, y_gender_train, y_gender_test = train_test_split(X, y_pos, y_gender, test_size=0.2, random_state=42)

# Train models
pos_model = MultinomialNB()
pos_model.fit(X_train, y_pos_train)

gender_model = MultinomialNB()
gender_model.fit(X_train, y_gender_train)

# Save models and encoders
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(le_pos, 'le_pos.joblib')
joblib.dump(le_gender, 'le_gender.joblib')
joblib.dump(pos_model, 'pos_model.joblib')
joblib.dump(gender_model, 'gender_model.joblib')
