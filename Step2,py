import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict

# Set the path to stop words and master dictionary directories
stop_words_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\StopWords-20240311T041135Z-001\StopWords'
master_dict_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\MasterDictionary-20240311T041108Z-001\MasterDictionary'

# Function to read stop words from files
def read_stop_words(directory):
    stop_words = set()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r', encoding='latin-1') as file:
            stop_words.update(file.read().splitlines())
    return stop_words

# Function to read positive and negative words from files
def read_master_dict(directory):
    positive_words = set()
    negative_words = set()
    with open(os.path.join(directory, 'positive-words.txt'), 'r', encoding='latin-1') as file:
        positive_words.update(file.read().splitlines())
    with open(os.path.join(directory, 'negative-words.txt'), 'r', encoding='latin-1') as file:
        negative_words.update(file.read().splitlines())
    return positive_words, negative_words

# Function to clean text using stop words
def clean_text(text, stop_words):
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [token for token in tokens if token not in stop_words and token.isalpha()]
    return cleaned_tokens

# Function to perform text analysis and compute variables
def analyze_text(text, positive_words, negative_words):
    positive_score = sum(1 for word in text if word in positive_words)
    negative_score = sum(-1 for word in text if word in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(text) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

# Read stop words
stop_words = read_stop_words(stop_words_dir)

# Read positive and negative words
positive_words, negative_words = read_master_dict(master_dict_dir)

# Read input Excel file
input_excel_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\Input.xlsx'
input_data = pd.read_excel(input_excel_path)

# Iterate over input data
output_data = []
for index, row in input_data.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    text_path = os.path.join(extracted_texts_dir, f"{url_id}.txt")
    try:
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()
            cleaned_text = clean_text(text, stop_words)
            positive_score, negative_score, polarity_score, subjectivity_score = analyze_text(cleaned_text, positive_words, negative_words)
            output_data.append([url_id, url, positive_score, negative_score, polarity_score, subjectivity_score])
    except FileNotFoundError:
        print(f"File {text_path}  Page not found. Skipping...")

# Write output to CSV file
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
with open(output_file_path, 'w', encoding='utf-8') as csv_file:
    csv_file.write("URL_ID,URL,POSITIVE SCORE,NEGATIVE SCORE,POLARITY SCORE,SUBJECTIVITY SCORE\n")
    for row in output_data:
        csv_file.write(','.join(map(str, row)) + '\n')

print("Text analysis complete. Output saved to", output_file_path)
