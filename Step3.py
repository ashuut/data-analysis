import pandas as pd
import os
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import cmudict
import string

# Function to calculate Average Sentence Length
def calculate_avg_sentence_length(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    words = word_tokenize(text)
    num_words = len(words)
    return num_words / num_sentences

# Function to calculate Percentage of Complex Words
def calculate_percentage_complex_words(text):
    cmu_dict = cmudict.dict()
    words = [word for word in word_tokenize(text.lower()) if word.isalpha()]
    complex_words = [word for word in words if len(cmu_dict.get(word, [])) > 2]
    return len(complex_words) / len(words)

# Function to calculate Fog Index
def calculate_fog_index(avg_sentence_length, percentage_complex_words):
    return 0.4 * (avg_sentence_length + percentage_complex_words)

# Read existing data from output file into DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files and calculate variables
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'
for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            avg_sentence_length = calculate_avg_sentence_length(text)
            percentage_complex_words = calculate_percentage_complex_words(text)
            fog_index = calculate_fog_index(avg_sentence_length, percentage_complex_words)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'AVG SENTENCE LENGTH'] = avg_sentence_length
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'FOG INDEX'] = fog_index

# Write updated DataFrame back to output file
output_df.to_csv(output_file_path, index=False)

print("Analysis of Readability complete. Updated output saved to", output_file_path)
