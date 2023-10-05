"""
Script to tokenize the text from an input file into sentences and save the tokenized sentences to an output file.
"""

# Necessary imports
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def read_file(filepath):
    """
    Reads content from a given file and returns it.
    
    Args:
    - filepath (str): Path to the file to be read.
    
    Returns:
    - str: Content of the file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filepath} not found. Please check the path and try again.")
        return None

def tokenize_and_format_text(text):
    """
    Tokenizes the text into sentences using nltk's sentence tokenizer.
    
    Args:
    - text (str): Text to be tokenized.
    
    Returns:
    - str: Formatted content with each sentence on a new line.
    """
    sentences = sent_tokenize(text)
    return '\n'.join(sentences)

def main(input_filepath, output_filepath):
    """
    Main function to read, tokenize, and save the tokenized content.
    
    Args:
    - input_filepath (str): Path to the input file.
    - output_filepath (str): Path where the tokenized content should be saved.
    """
    raw_content = read_file(input_filepath)
    if raw_content is None:
        return
    
    formatted_content = tokenize_and_format_text(raw_content)
    
    with open(output_filepath, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Formatted data saved to {output_filepath}")

if __name__ == '__main__':
    input_filepath = '/workspaces/Jarvis-Data-Tokenizer/data.txt'
    output_filepath = '/workspaces/Jarvis-Data-Tokenizer/formatted_data.txt'
    
    main(input_filepath, output_filepath)
