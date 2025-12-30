import sys
from stats import get_num_words
from stats import get_num_chars
from stats import format_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    chars = get_num_chars(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count ---------")
    report = format_report(chars)
    for blah in report:
        print(f"{blah['char']}: {blah['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
