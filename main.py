import sys
from stats import get_text_count, get_each_text_count, sort_distionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_text = f.read()
    return file_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv[1])
    path_to_file = sys.argv[1]
    file_contnet = get_book_text(path_to_file)
    word_count_of_book = get_text_count(file_contnet)
    char_count = get_each_text_count(file_contnet)
    sorted_list = sort_distionary(char_count)
    # print(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...") 
    print("----------- Word Count ----------")
    print(f"Found {word_count_of_book} total words")
    print("--------- Character Count -------")
    for items in sorted_list:
        if not items["char"].isalpha():
            continue
        print(f"{items["char"]}: {items["num"]}")
           
    print("============= END ===============")
    
     
    
main()
