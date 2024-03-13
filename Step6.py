import pandas as pd
import os
import nltk

# Function to compute the word count
def compute_word_count(text):
    tokens = nltk.word_tokenize(text.lower())
    cleaned_tokens = [token for token in tokens if token.isalpha()]
    word_count = len(cleaned_tokens)
    return word_count

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = compute_word_count(text)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'WORD COUNT'] = word_count

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
