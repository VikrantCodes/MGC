import re
import sys

# Marathi vowels, consonants, and symbols
vowels = "अआइईउऊएऐओऔऋॠऌॡअंअः"
consonants = "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"
symbols = "।,;:.!?()[]{}\"'`~@#$%^&*-+=<>\\/|0123456789"

# Define Marathi parts of speech and grammatical rules
nouns = {
    "सूरज": "Masculine", 
    "मुलगा": "Masculine", 
    "शाळा": "Feminine", 
    "पुस्तक": "Neuter"
}
adjectives = {
    "सुंदर": "Descriptive", 
    "उत्साही": "Descriptive", 
    "वेगवान": "Descriptive"
}
verbs = {
    "खेलतो": "Action", 
    "पढतो": "Action", 
    "यात्रा": "Action"
}

# Singular, Dual, and Plural forms
singular = {"सूरज", "मुलगा"}
dual = {"आम्ही"}
plural = {"सगळे", "मुलगे"}

# Function to classify each character
def classify_characters(word):
    classifications = []

    for char in word:
        if char in vowels:
            classifications.append({'Character': char, 'Type': 'Vowel'})
        elif char in consonants:
            classifications.append({'Character': char, 'Type': 'Consonant'})
        elif re.match(r'\s', char):
            classifications.append({'Character': char, 'Type': 'Whitespace'})
        elif char in symbols:
            classifications.append({'Character': char, 'Type': 'Symbol'})
        else:
            classifications.append({'Character': char, 'Type': 'Unknown'})
    
    return classifications

# Function to break down the word into its base components
def analyze_word(word):
    morphemes = []
    prefixes = ["अ", "प्र", "उ"]
    suffixes = ["ा", "ी", "े", "तो", "ने", "का", "की"]

    # Check for prefixes and suffixes
    for prefix in prefixes:
        if word.startswith(prefix):
            morphemes.append({'Component': prefix, 'Type': 'Prefix'})
            word = word[len(prefix):]

    for suffix in suffixes:
        if word.endswith(suffix):
            morphemes.append({'Component': suffix, 'Type': 'Suffix'})
            word = word[:-len(suffix)]

    if word:
        morphemes.append({'Component': word, 'Type': 'Root'})
    
    return morphemes

# Enhanced POS Tagging Function
def pos_tagging(word):
    # Define rules for different parts of speech
    noun_suffixes = ["आ", "ई", "न"]
    adjective_suffixes = ["ा", "ी"]
    verb_suffixes = ["तो", "ते", "ला"]
    pronoun_suffixes = ["हा", "ही", "हे"]
    prepositions = ["मध्ये", "वर", "खाली"]
    conjunctions = ["आणि", "किंवा", "परंतु"]
    adverbs = ["ने", "पणे"]

    # Check suffixes for nouns
    if any(word.endswith(suffix) for suffix in noun_suffixes):
        return f'Noun (Gender: Unknown)'

    # Check suffixes for adjectives
    if any(word.endswith(suffix) for suffix in adjective_suffixes):
        return 'Adjective'

    # Check suffixes for verbs
    if any(word.endswith(suffix) for suffix in verb_suffixes):
        return 'Verb'

    # Check known pronouns
    if word in ["माझा", "तू", "त्यांनी"]:
        return 'Pronoun'

    # Check known prepositions
    if word in prepositions:
        return 'Preposition'

    # Check known conjunctions
    if word in conjunctions:
        return 'Conjunction'

    # Check known adverbs
    if any(word.endswith(suffix) for suffix in adverbs):
        return 'Adverb'

    return 'Unknown'

# Function to detect singular, dual, or plural forms
def number_classification(word):
    if word in singular:
        return 'Singular (एकवचन)'
    elif word in dual:
        return 'Dual (द्विवचन)'
    elif word in plural:
        return 'Plural (बहुवचन)'
    else:
        return 'Unknown'

# Function to format output for better readability
def print_formatted_output(char_classification, morpheme_analysis):
    # Calculate the maximum width for each column
    max_char_length = max(len(info['Character']) for info in char_classification)
    max_type_length = max(len(info['Type']) for info in char_classification)
    
    print("Character Classification:")
    for info in char_classification:
        print(f"[ {info['Character'].ljust(max_char_length)} | {info['Type'].ljust(max_type_length)} ]")
    
    print("\nMorpheme and POS Analysis:")
    for word, analysis in morpheme_analysis.items():
        pos = pos_tagging(word)
        number = number_classification(word)
        print(f"Word: {word} (POS: {pos}, Number: {number})")
        for part in analysis:
            print(f"  Component: {part['Component']}, Type: {part['Type']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 classifier.py \"<text>\"")
        sys.exit(1)
    
    text = sys.argv[1]
    char_classification = classify_characters(text)

    # Analyze words for morphemes and parts of speech
    words = text.split()
    morpheme_analysis = {word: analyze_word(word) for word in words}

    # Print formatted output
    print_formatted_output(char_classification, morpheme_analysis)
