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

def count_words(string_to_count):
    count = len(string_to_count.split())
    return count

main()
# # string =
# print(len(get_book_text('books/frankenstein.txt').split()))