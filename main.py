from stats import count_characters, count_words, sort_chars

def main():
    path_to_book = 'books/frankenstein.txt'
    string = get_book_text('books/frankenstein.txt')
    num_words = count_words(string)
    num_chars = count_characters(string)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {path_to_book}...")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for item in sort_chars(num_chars):
        print(f"{item['char']}: {item['count']}")
    print('============= END ===============')


def get_book_text(path_to_file):
    text = ''
    with open(path_to_file) as book:
        text = book.read()
    return text

main()