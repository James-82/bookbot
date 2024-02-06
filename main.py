def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count = count_letters(file_contents)
        press = report(letter_count)

        
        print(file_contents)
        print("")
        print(f"{num_words(file_contents)} total words found in the doc!")
        print("")
        print(letter_count)
        print("")
        print("--- Begin report of books/frankenstein.txt ---")
        print("")
        report(letter_count)
        print("")
        print("--- End of Report ---")


def num_words(file_contents):
    words = file_contents.split()
    return (len(words))

def count_letters(file_contents):
    lowered_count = file_contents.lower()
    char_dict = {}
    for char in lowered_count:
        if char.isalpha():   
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def report(letter_count):
    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")
    


main()