import sys
from stats import count_words, get_char_count, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def print_analysis_report(word_count, character_counts):
    # Print header
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print character counts
    for d in character_counts:
        if d["c"].isalpha():
            print(f"{d['c']}: {d['count']}")
    
    # Print footer
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    full_text = get_book_text(sys.argv[1])
    num_words = count_words(full_text)
    char_count = get_char_count(full_text)
    sorted_results = sort_char_count(char_count) 
    print_analysis_report(num_words, sorted_results)

main()