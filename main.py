from stats import count_words
from stats import count_characters

def main():
    path_to_book = 'books/frankenstein.txt'
    string = get_book_text('books/frankenstein.txt')
    num_words = count_words(string)
    num_chars = count_characters(string)
    print(f"{num_words} words found in the document")
    print(num_chars)

def get_book_text(path_to_file):
    text = ''
    with open(path_to_file) as book:
        text = book.read()
    return text

main()