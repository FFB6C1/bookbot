def word_count(str):
    return len(str.split())

def char_count(str):
    str = str.lower()
    dict_counter = {}
    for letter in str:
        if letter not in dict_counter:
            dict_counter[letter] = 1
        else:
            dict_counter[letter] += 1
    return dict_counter

def report(str):
    str = str.lower()
    words = word_count(str)
    chars = char_count(str)
    chars_ordered = []
    for entry in chars:
        if entry.isalpha():
            chars_ordered.append({"char": entry, "num": chars[entry]})
    def sort_num(dict):
        return dict["num"]
    chars_ordered.sort(reverse=True, key=sort_num)

    print(f"This book contains {words} words.")
    print("--------")
    print("CHARACTER COUNT")
    print("--------")
    for entry in chars_ordered:
        print(f"{entry["char"]} appears {entry["num"]} times.")

def get_text(book_doc):
    with open("books/" + book_doc) as f:
        return f.read()


def main():
    text = get_text("frankenstein.txt")
    report(text)

main()