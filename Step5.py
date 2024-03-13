import pandas as pd
import os
import nltk
from nltk.corpus import cmudict

# Function to compute the complex word count
def compute_complex_word_count(text):
    words = nltk.word_tokenize(text.lower())
    cmu_dict = cmudict.dict()
    complex_word_count = sum(1 for word in words if len(cmu_dict.get(word, [])) > 2)
    return complex_word_count

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            complex_word_count = compute_complex_word_count(text)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'COMPLEX WORD COUNT'] = complex_word_count

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
