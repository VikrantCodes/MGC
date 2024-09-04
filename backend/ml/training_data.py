import pandas as pd

# Sample training data
data = {
    'Word': ["सुंदर", "पार्क", "विशाल", "वनात", "मुलं", "मुली", "खेळतात", "उधाणलेल्या", "नदी", "काठी", "आर्या", "विशू", "विश्रांती", "घेतात", "आई", "विष्णू", "प्रकृतीचा", "आनंद"],
    'POS': ["Adjective", "Noun", "Adjective", "Noun", "Noun", "Noun", "Verb", "Adjective", "Noun", "Noun", "Noun", "Noun", "Noun", "Verb", "Noun", "Noun", "Noun", "Noun"],
    'Gender': ["Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Neutral/Not Applicable", "Female", "Male", "Neutral/Not Applicable", "Neutral/Not Applicable", "Female", "Male", "Neutral/Not Applicable", "Neutral/Not Applicable"]
}

df = pd.DataFrame(data)
df.to_csv('training_data.csv', index=False)
