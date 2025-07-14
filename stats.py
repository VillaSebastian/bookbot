def get_book_text(filepath):
    with open(filepath) as book:
        book_text = book.read()
    return book_text

def get_number_of_words(text):
    return len(text.split())

def get_number_of_characters(text):
    characters = {}
    for word in text:
        #print(f"word is {word}")
        word = word.lower()
        #print(f"word is {word}")

        for letter in word:
            if letter.isalpha():
                if letter not in characters:
                    characters[letter] = 1
                else:
                    characters[letter] += 1
    return characters

def sort_characters(characters, path):
    #number_of_words = get_words_count(text)
    number_of_words = get_number_of_words(get_book_text(path))
    #characters = get_char_count(text)

    # Sorting dictionary from most recurrent char to least
    characters = {key: value for key, value in sorted(characters.items(), key = lambda element: element[1], reverse = True)}

    # Print report to CLI
    #print(f'--- Begin report of {path} ---')
    
    print("----------- Word Count ----------")
    print(f'Found {number_of_words} total words')
    print("--------- Character Count -------")
    for char, number in characters.items():
        #print(f'The "{char}" character was found {number} times')
        print(f"{char}: {number}")
    print("============= END ===============")
