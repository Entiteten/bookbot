from stats import word_count
def main():
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
