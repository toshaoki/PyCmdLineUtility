import re
import sys
from adoc_substitutor import process_file

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

# Get filename from command line arguments
filename = sys.argv[1]

process_file(filename)
