import sys
from stats import count_characters, sort_dict, count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    words = get_book_text(sys.argv[1])
    count = count_words(words)
    char_count = count_characters(words)
    dict = sort_dict(char_count)

    print('============ BOOKBOT ============\n----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    for item in dict:
        print(f'{item["name"]}: {item["num"]}')
    print('============= END ===============')

main()