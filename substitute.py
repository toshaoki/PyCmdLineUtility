import sys

def substitute_characters(text):
    """
    Replace specific characters in the given text.

    Args:
        text (str): The text to process.

    Returns:
        str: The text with "。" replaced by "．" and "、" replaced by "，".
    """
    text = text.replace("。", "．")
    text = text.replace("、", "，")
    return text

def process_file(filename):
    """
    Read a file, replace specific characters in its content, and overwrite the file with the new content.

    Args:
        filename (str): The name of the file to process.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = substitute_characters(text)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)

# Get filename from command line arguments
filename = sys.argv[1]

process_file(filename)
