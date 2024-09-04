import re
import sys
from nltk.tokenize import word_tokenize
import joblib

# Load models and encoders
vectorizer = joblib.load('vectorizer.joblib')
le_pos = joblib.load('le_pos.joblib')
le_gender = joblib.load('le_gender.joblib')
pos_model = joblib.load('pos_model.joblib')
gender_model = joblib.load('gender_model.joblib')

# Custom stopwords for Marathi (example list)
custom_stopwords = set([
    "आणि", "पण", "तो", "ती", "ते", "एक", "आहे", "असे", "सर्व", "तुम्ही", "मी", "तुम्ही", "आम्ही", "कसे"
])

def classify_text(text):
    words = word_tokenize(text)
    results = {}

    for word in words:
        sanitized_word = re.sub(r'[^\w\s]', '', word).strip()
        if sanitized_word in custom_stopwords:
            pos = "Pronoun"
            gender = "Neutral/Not Applicable"
        else:
            X = vectorizer.transform([sanitized_word])
            pos = le_pos.inverse_transform(pos_model.predict(X))[0]
            gender = le_gender.inverse_transform(gender_model.predict(X))[0] if pos in ["Noun", "Adjective", "Pronoun"] else "Neutral/Not Applicable"

        results[word] = {'POS': pos, 'Gender': gender}

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide input text.")
        sys.exit(1)
    
    text = sys.argv[1]
    classification = classify_text(text)

    for word, info in classification.items():
        print(f"{word}: POS = {info['POS']}, Gender = {info['Gender']}")
