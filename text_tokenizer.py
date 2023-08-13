import os
import re
import nltk

def read_file(filepath):
    """
    Reads content from a given file and returns it.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize_and_format_text(text):
    """
    Tokenizes the text into sentences using simple regex and returns the formatted content.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return '\n'.join(sentences)

def main():
    filepath = '/workspaces/anaconda-2/data.txt'
    output_file = '/workspaces/anaconda-2/formatted_data.txt'
    
    raw_content = read_file(filepath)
    formatted_content = tokenize_and_format_text(raw_content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Formatted data saved to {output_file}")

if __name__ == '__main__':
    main()
