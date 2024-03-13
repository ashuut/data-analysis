import pandas as pd
import os
import nltk

# Function to compute the syllable count per word
def compute_syllable_count(text):
    tokens = nltk.word_tokenize(text.lower())
    syllable_count = sum(len([v for v in token if v in 'aeiou']) for token in tokens)
    return syllable_count

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            syllable_count = compute_syllable_count(text)
            word_count = len(nltk.word_tokenize(text.lower()))
            syllable_count_ratio = syllable_count / word_count if word_count > 0 else 0
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'SYLLABLE COUNT PER WORD'] = syllable_count_ratio

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
