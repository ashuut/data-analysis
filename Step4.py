import pandas as pd
import os
import nltk

# Function to compute the average number of words per sentence
def compute_avg_words_per_sentence(text):
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    words = nltk.word_tokenize(text)
    num_words = len(words)
    if num_sentences > 0:
        avg_words_per_sentence = num_words / num_sentences
    else:
        avg_words_per_sentence = 0
    return avg_words_per_sentence

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            avg_words_per_sentence = compute_avg_words_per_sentence(text)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'AVG NUMBER OF WORDS PER SENTENCE'] = avg_words_per_sentence

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
