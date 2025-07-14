import sys
from stats import get_book_text
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    number_of_words = get_number_of_words(get_book_text(path))
    print(f"Analyzing book found at", path)
    print(f"{number_of_words} words found in the document")
    characters = get_number_of_characters(get_book_text(path))
    #print (characters)
    sort_characters(characters, path)
    

main()
