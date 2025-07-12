def main():
    filepath = "./books/frankenstein.txt"
    print(get_book_text(filepath))

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()
