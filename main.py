from stats import word_count
from stats import char_count

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.

    Returns:
        str: The content of the file as a string."""
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    return get_book_text("books/frankenstein.txt")

n = word_count(main())
c = char_count(main())
print(f"{n} words found in the document")
print(c)