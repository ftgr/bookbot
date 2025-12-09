from stats import words_counter
from stats import characters_counter_from_text
from stats import sorted_list_of_characters_counter
import sys

def get_book_text(filepath):
    # mode "r" = text read (default)
    with open(filepath, "r", encoding="utf-8") as f:
         # read entire file as one string
        content = f.read()
    return content



def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_book_text(filepath)
    num_words = words_counter(book_content)
    print(f"Found {num_words} total words")

    characters_count = characters_counter_from_text(book_content)
    #print(characters_count)
    sorted_list_dic_character = sorted_list_of_characters_counter(characters_count)
    for item in sorted_list_dic_character:
        letter = item["char"]
        count = item["num"]
        print(f"{letter}: {count}")
main()
