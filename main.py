def main():
    frankenstein_path = "books/frankenstein.txt"
    try:
        frankenstein_text = get_book_text(frankenstein_path)
    except FileNotFoundError:
        print(f'Error: File not found at path {frankenstein_path}')
        return
    except Exception as e:
        print(f'An error occurred: {e}')
        return

    generate_report(frankenstein_text, frankenstein_path)

    
def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def get_words_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict:
    characters = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for character in word:
            if character.isalpha():
                counter = characters.get(character, 0)
                counter += 1
                characters.update({character: counter})
    return characters

def generate_report(text: str, path: str) -> str:
    number_of_words = get_words_count(text)
    characters = get_char_count(text)
    # Sorting dictionary from most recurrent char to least
    characters = {key: value for key, value in sorted(characters.items(), key = lambda element: element[1], reverse = True)}

    # Print report to CLI
    print(f'--- Begin report of {path} ---')
    print(f'{number_of_words} found in the document\n')
    for char, number in characters.items():
        print(f'The "{char}" character was found {number} times')
    print(f'--- End report ---')


if __name__ == '__main__':
    main()
