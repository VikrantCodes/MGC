import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Sample dataset
data = {
    'text': [
    "वडील",
    "आजोबा",
    "पणजोबा",
    "सासरे",
    "काका",
    "मामा",
    "भाऊ",
    "मोठा भाऊ",
    "लहान भाऊ",
    "दिर",
    "मेव्हणा",
    "जाऊबाप",
    "पती",
    "मुलगा",
    "जावई",
    "नातू",
    "भाचा",
    "पुतण्या",
    "साळू",
    "मावसा",
    "आई",        # Mother
    "आजी",        # Grandmother (paternal)
    "नणंद",      # Sister-in-law (wife's sister)
    "भावजयी",    # Sister-in-law (brother's wife)
    "पत्नी",      # Wife
    "धाकटी बहीण",  # Younger Sister
    " मोठी बहिण",  # Elder Sister
    "मुलगी",      # Daughter
    "सून",        # Daughter-in-law
    "माझी बहीण",  # My Sister
    "माझी पत्नी",  # My Wife
    "माझी मुलगी"   # My Daughter
    ],
    'gender': [
        "पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","पुरुष","महिला","महिला","महिला","महिला","महिला","महिला","महिला","महिला","महिला","महिला","महिला","महिला",
    ]
}

df = pd.DataFrame(data)

# Data Preprocessing
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['gender']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Function to predict gender of new text
def predict_gender(new_text):
    new_text_transformed = vectorizer.transform([new_text])  # Transform the new text
    prediction = model.predict(new_text_transformed)  # Predict using the trained model
    return prediction[0]

# Function to predict gender for multiple new texts
def predict_genders(new_texts):
    new_texts_transformed = vectorizer.transform(new_texts)  # Transform the new texts
    predictions = model.predict(new_texts_transformed)  # Predict using the trained model
    return predictions

# Example usage for multiple texts
new_texts = [
    "माझी आई आणि बहीण",
    "राजू माझा भाऊ आहे",
     "प्रिया आई आहे",
     "राजू माझा भाऊ. प्रिया आई आहे"
]
predicted_genders = predict_genders(new_texts)
for text, gender in zip(new_texts, predicted_genders):
    print(f"The predicted gender for the text '{text}' is: {gender}")