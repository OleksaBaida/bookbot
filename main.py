from stats import count_words

def main():
    path_to_book = 'books/frankenstein.txt'
    string = get_book_text('books/frankenstein.txt')
    num_words = count_words(string)
    print(f"{num_words} words found in the document")

def get_book_text(path_to_file):
    text = ''
    with open(path_to_file) as book:
        text = book.read()
    return text

main()