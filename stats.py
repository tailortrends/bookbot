def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    counts = {}

    text = text.lower()

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def sort_char_counts(char_dict):
    # Convert to list of dictionaries, ignoring non-alphabetical chars
    char_list = [{"char": c, "num": n} for c, n in char_dict.items() if c.isalpha()]

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
