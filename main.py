from stats import count_characters, count_words, sort_chars
import sys
def main():
    # if len(sys.argv) <= 1 :
    # print()

    # path_to_book = sys.argv[1]
    try:
        path_to_book = sys.argv[1]
    except:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    string = get_book_text(path_to_book)
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