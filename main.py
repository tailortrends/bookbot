from pathlib import Path
import sys
from stats import count_words, char_count, sort_char_counts


def get_book_text(filepath):
    with open(filepath,'r') as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    text = get_book_text(book_path)

    num_words = count_words(text)

    char_counts = char_count(text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()