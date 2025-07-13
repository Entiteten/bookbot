import sys
if not sys.argv[1:]:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import word_count, chars_dict, sort_chars
def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = word_count(text)
    characters = chars_dict(text)
    sorted = sort_chars(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
