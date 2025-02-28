def main():
    print(get_book_text('books/frankenstein.txt'))

def get_book_text(path_to_file):
    text = ''
    with open(path_to_file) as book:
        text = book.read()
    return text

main()