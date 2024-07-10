def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frankenstein_path)
    number_of_words = get_words_count(frankenstein_text)
    print(f'The text Frankenstein has {number_of_words} words')
    

def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()

def get_words_count(text: str) -> int:
    words = text.split()
    return len(words)


if __name__ == '__main__':
    main()
