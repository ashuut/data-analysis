Text Analysis Tool
Overview
This text analysis tool is designed to analyze text data from various sources and compute several metrics to gain insights into the content. It performs sentiment analysis, readability analysis, and computes various linguistic features such as word count, average word length, and syllable count per word.

Features
Sentiment Analysis: Determines the sentiment of the text by computing positive and negative scores, polarity score, and subjectivity score.
Readability Analysis: Calculates readability metrics including average sentence length, percentage of complex words, and Fog Index.
Average Number of Words Per Sentence: Computes the average number of words per sentence in the text.
Complex Word Count: Counts the number of complex words in the text.
Word Count: Calculates the total number of words in the text.
Syllable Count Per Word: Determines the number of syllables in each word, accounting for exceptions like words ending with "es" or "ed".
Personal Pronouns Count: Counts the occurrences of personal pronouns such as "I," "we," "my," "ours," and "us".
Average Word Length: Computes the average length of words in the text.
Usage
Input Data: Provide the input text files to be analyzed. These files should be stored in a directory specified by the extracted_texts_dir variable.
Stop Words and Master Dictionary: Ensure that the stop words and master dictionary directories are correctly set in the code (stop_words_dir and master_dict_dir variables).
Output: The analysis results will be saved to an output CSV file specified by the output_file_path variable.
How to Run
Clone or download the project repository.
Ensure that Python and the required libraries (NLTK, pandas) are installed.
Modify the input data paths and directory settings if necessary.
Run the main script (text_analysis.py).
View the output CSV file containing the analysis results.
Dependencies
Python 3.x
NLTK (Natural Language Toolkit)
pandas
Example
python
Copy code
python text_analysis.py
Contributors
Ashutosh Surve.
License
This project is licensed under the MIT License.
