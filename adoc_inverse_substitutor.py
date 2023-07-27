import re
import sys

def inverse_substitute_patterns(text):
    """
    Latex -> Asciidoctor

    Replace specific patterns in the given text.

    Args:
        text (str): The text to process.

    Returns:
        str: The text with "$...$" replaced by "stem:[...]".
    """
    pattern = r'\$\s*(.*?)\s*\$'
    return re.sub(pattern, r'stem:[\1]', text)


def process_file(filename):
    """
    Read a file, replace specific patterns in its content, and overwrite the file with the new content.

    Args:
        filename (str): The name of the file to process.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = inverse_substitute_patterns(text)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)


# Get filename from command line arguments
filename = sys.argv[1]

process_file(filename)
