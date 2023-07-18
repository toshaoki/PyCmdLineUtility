import sys
import re

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


def insert_spaces(text):
    """
    Insert a space between a full-width Japanese character and a half-width alphanumeric character.

    This function scans through the given text, and if it finds a full-width Japanese character (Hiragana, Katakana, or Kanji)
    followed by a half-width alphanumeric character (A-Z, a-z, 0-9), or a half-width alphanumeric character followed by a 
    full-width Japanese character, it inserts a space between them.

    Note: This function only considers full-width Japanese characters and half-width alphanumeric characters. Other full-width 
    characters (e.g., full-width spaces or symbols) or other half-width characters (e.g., half-width symbols) are not considered.

    Args:
        text (str): The text in which to insert spaces.

    Returns:
        str: The text with spaces inserted.
    """
    text_with_spaces = ""
    for i in range(len(text) - 1):
        text_with_spaces += text[i]
        if re.match(r'[A-Za-z0-9]', text[i]) and re.match(r'[\u3040-\u30FF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]', text[i+1]):
            text_with_spaces += " "
        elif re.match(r'[\u3040-\u30FF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]', text[i]) and re.match(r'[A-Za-z0-9]', text[i+1]):
            text_with_spaces += " "
    text_with_spaces += text[-1]
    return text_with_spaces


def process_file(filename):
    """
    Read a file, replace specific characters in its content, and overwrite the file with the new content.

    Args:
        filename (str): The name of the file to process.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    new_text = substitute_characters(text)
    new_text = insert_spaces(text)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)

# Get filename from command line arguments
filename = sys.argv[1]

process_file(filename)
