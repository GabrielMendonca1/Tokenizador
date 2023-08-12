import os
from nltk.tokenize import sent_tokenize

def read_files_from_directory(directory):
    """
    Reads all text files from a given directory and returns the concatenated content.
    """
    content = ''
    
    for filename in os.listdir(directory):
        if filename.endswith('data.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content += file.read() + '\n'
    
    return content

def tokenize_and_format_text(text):
    """
    Tokenizes the text into sentences and returns the formatted content.
    """
    sentences = sent_tokenize(text)
    return '\n'.join(sentences)

def main():
    directory = 'path_to_your_text_files_directory'
    output_file = 'formatted_data.txt'
    
    raw_content = read_files_from_directory(directory)
    formatted_content = tokenize_and_format_text(raw_content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Formatted data saved to {output_file}")

if __name__ == '__main__':
    main()
