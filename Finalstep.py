import nltk
import os
import pandas as pd

# Function to compute the average word length
def compute_average_word_length(text):
    tokens = nltk.word_tokenize(text.lower())
    total_characters = sum(len(word) for word in tokens)
    total_words = len(tokens)
    if total_words != 0:
        average_word_length = total_characters / total_words
    else:
        average_word_length = 0
    return average_word_length

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            average_word_length = compute_average_word_length(text)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'AVG WORD LENGTH'] = average_word_length

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
