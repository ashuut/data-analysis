import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Read the input Excel file
input_file_path = r'E:\OneDrive\Desktop\interview prepration\blackoffers\Input.xlsx'
df = pd.read_excel(input_file_path)

# Create a directory to save the extracted article texts
output_directory = r'E:\OneDrive\Desktop\interview prepration\blackoffers\extracted_texts'
os.makedirs(output_directory, exist_ok=True)

# Function to extract article title and text from URL
def extract_article_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract article title
            article_title = soup.find(class_="entry-title").get_text()
            # Extract article text
            article_text = soup.find(class_="td-post-content").get_text()
            return article_title, article_text
        else:
            print(f"Failed to fetch {url}. Status code: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"An error occurred while fetching {url}: {e}")
        return None, None

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    print(f"Processing URL_ID: {url_id}")
    
    # Extract article title and text
    article_title, article_text = extract_article_info(url)
    
    if article_title and article_text:
        # Save the article title and text to a text file
        output_file_path = os.path.join(output_directory, f"{url_id}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(article_title + '\n\n')
            f.write(article_text)
        print(f"Article title and text saved to {output_file_path}")
    else:
        print("Failed to extract article title and text.")

print("Extraction complete.")
