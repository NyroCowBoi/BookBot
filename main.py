import sys
from stats import count_words, count_characters, sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_characters = sorted_list(num_characters)
    print_report(book_path, num_words, sorted_characters)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def print_report(book_path, num_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dictionary in sorted_characters:
        if dictionary["char"].isalpha():
            char = dictionary["char"]
            num = dictionary["num"]
            print(f"{char}: {num}")
        else:
            continue

    print("============= END ===============")

main()