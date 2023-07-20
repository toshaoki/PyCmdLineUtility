"""
Asciidoctor to Latex
"""
import re
import sys

def substitute_patterns(text):
    """
    Asciidoctor -> Latex
    
    Replace specific patterns in the given text.

    Args:
        text (str): The text to process.

    Returns:
        str: The text with "stem:[...]" and "latexmath:[...]" replaced by "$...$".
    """
    pattern = r'(stem|latexmath):\[\s*(.*?)\s*\]'
    return re.sub(pattern, r'$\2$', text)

def process_file(filename):
    """
    Read a file, replace specific patterns in its content, and overwrite the file with the new content.

    Args:
        filename (str): The name of the file to process.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = substitute_patterns(text)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)

# Get filename from command line arguments
filename = sys.argv[1]

process_file(filename)
