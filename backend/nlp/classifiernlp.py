import re
import sys
from nltk.tokenize import word_tokenize

# Custom stopwords for Marathi (example list)
custom_stopwords = set([
    "आणि", "पण", "तो", "ती", "ते", "एक", "आहे", "असे", "सर्व", "तुम्ही", "मी", "तुम्ही", "आम्ही", "कसे"
])

# Special cases for gender classification
special_cases = {
    "विष्णू": "Male"
}

def classify_gender(word):
    if word in special_cases:
        return special_cases[word]

    masculine_suffixes = ["ा", "ु", "क", "ी", "े", "य"]
    feminine_suffixes = ["ई", "आ", "या", "ण", "णी", "ा", "ाया"]
    neuter_suffixes = ["ं", "इ", "ो", "अ", "य", "ां", "े"]

    word = re.sub(r'[^\w\s]', '', word).strip()

    if any(word.endswith(suffix) for suffix in masculine_suffixes):
        return "Male"
    if any(word.endswith(suffix) for suffix in feminine_suffixes):
        return "Female"
    if any(word.endswith(suffix) for suffix in neuter_suffixes):
        return "Neutral/Not Applicable"

    return "Neutral/Not Applicable"

def pos_tagging(word):
    # Basic POS tagging based on custom rules
    if word in ["आणि", "किंवा", "तर", "अथवा"]:
        return "Conjunction"
    elif word in ["वर", "खाली", "अधिक", "साठी"]:
        return "Preposition"
    elif word in ["अरे", "वाह", "आय"]:
        return "Interjection"
    elif re.search(r'(ता|तो|ते|ला|ते|य|ने|त|न|च)', word):
        return "Verb"
    elif re.search(r'(ा|ी|े|या|ण)', word):
        return "Adjective"
    elif re.search(r'(पणे|ने)', word):
        return "Adverb"
    elif word in custom_stopwords:
        return "Pronoun"
    else:
        return "Noun"

def classify_text(text):
    words = word_tokenize(text)
    results = {}

    for word in words:
        pos = pos_tagging(word)
        gender = classify_gender(word) if pos in ["Noun", "Adjective", "Pronoun"] else "Neutral/Not Applicable"
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
