import pandas as pd
import os
import re

# Function to compute total count of personal pronouns
def compute_total_personal_pronouns(text):
    pronouns = {"I", "we", "my", "ours", "us"}
    total_count = sum(len(re.findall(r'\b{}\b'.format(pronoun), text, flags=re.IGNORECASE)) for pronoun in pronouns)
    return total_count

# Read existing output file into a DataFrame
output_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\output.csv'
output_df = pd.read_csv(output_file_path)

# Iterate over extracted text files
extracted_texts_dir = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'

for filename in os.listdir(extracted_texts_dir):
    if filename.endswith('.txt'):
        with open(os.path.join(extracted_texts_dir, filename), 'r', encoding='utf-8') as file:
            text = file.read()
            total_count = compute_total_personal_pronouns(text)
            output_df.loc[output_df['URL_ID'] == filename[:-4], 'TOTAL_PERSONAL_PRONOUNS'] = total_count

# Write updated DataFrame back to the output file
output_df.to_csv(output_file_path, index=False)
print("text analysis completed")
