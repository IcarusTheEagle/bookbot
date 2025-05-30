from stats import word_count
from stats import char_count
from stats import sort_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    return get_book_text(sys.argv[1])

n = word_count(main())
c = char_count(main())

sorted_list = sort_list(c)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {n} total words")
print("--------- Character Count -------")

for i in sorted_list:
    char = i["char"]
    count = i["num"]
    print(f"{char}: {count}")

print("============= END ===============")
