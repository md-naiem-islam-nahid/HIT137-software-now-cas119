# -*- coding: utf-8 -*-
"""Untitled.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hfGeGiCr2iatMFRhkgXMHrXG60PX6QOg

# Task 1: Extract the text from multiple CSV files
"""

import pandas as pd
import os
import zipfile
import warnings
import re
# Suppress all warnings
warnings.filterwarnings("ignore")

class TextProcessor:
    def __init__(self, zip_path, output_directory, output_file, chunk_size=1024*1024):
        self.zip_path = zip_path
        self.output_directory = output_directory
        self.output_file = output_file
        self.chunk_size = chunk_size
        self.output_path = os.path.join(output_directory, output_file)

    @staticmethod
    def create_output_directory(directory):
        """Create the output directory if it does not exist."""
        os.makedirs(directory, exist_ok=True)

    def extract_csv_from_zip(self):
        """Extract CSV files from the zip archive and return a list of DataFrames."""
        dfs = []
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename.endswith('.csv'):
                    with zip_ref.open(file_info.filename) as file:
                        df = pd.read_csv(file)
                        dfs.append(df)
        return dfs

    @staticmethod
    def extract_and_clean_texts(dfs):
        """Extract and clean texts from a list of DataFrames and return a generator of cleaned texts."""
        for df in dfs:
            if 'TEXT' in df.columns:
                for text in df['TEXT'].dropna():
                    yield TextProcessor.clean_text(text)

    @staticmethod
    def clean_text(text):
        """Clean text by removing non-English characters and extra spaces."""
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        return cleaned_text.strip()

    def process_texts(self):
        """Process and clean texts from CSV files and save the combined cleaned text."""
        self.create_output_directory(self.output_directory)
        dfs = self.extract_csv_from_zip()

        with open(self.output_path, 'w', encoding='utf-8') as outfile:
            for cleaned_text in self.extract_and_clean_texts(dfs):
                outfile.write(cleaned_text + '\n')


zip_path = './CSV.zip'
output_directory = './output'
output_file = 'combined_texts.txt'

processor = TextProcessor(zip_path, output_directory, output_file)
processor.process_texts()

"""# Task 2: Install the necessary libraries"""

print("Installing...")
# !pip install spacy
# !pip install scispacy
# !pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_core_sci_sm-0.5.0.tar.gz
# !pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_ner_bc5cdr_md-0.5.0.tar.gz
# !pip install transformers
print("Done.")

"""# Task 3.1: Count the Top 30 most common words"""

from collections import Counter
import csv

class WordAnalyzer:
    def __init__(self, file_path, chunk_size=1024*1024, word_number=30):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.word_number = word_number

    def count_words(self):
        """Count the occurrences of words in the file."""
        word_counter = Counter()

        with open(self.file_path, 'r', encoding='utf-8') as infile:
            while True:
                chunk = infile.read(self.chunk_size)
                if not chunk:
                    break

                # Process chunk
                words = chunk.split()
                word_counter.update(words)

        return word_counter.most_common(self.word_number)

    @staticmethod
    def save_to_csv(top_words, output_csv_path):
        """Save the top words and their counts to a CSV file."""
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Count'])
            writer.writerows(top_words)

    def process(self, output_csv_path):
        """Run the word count and save the results to a CSV file."""
        top_words = self.count_words()
        self.save_to_csv(top_words, output_csv_path)


file_path = './output/combined_texts.txt'
output_csv_path = './output/top_30_words.csv'

analyzer = WordAnalyzer(file_path)
analyzer.process(output_csv_path)
pd.read_csv('./output/top_30_words.csv').head(5)

