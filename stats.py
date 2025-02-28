def count_words(string_to_count):
    count = len(string_to_count.split())
    return count

def count_characters(string_to_count):
    count = {}
    for char in string_to_count:
        char = char.lower()
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1
    return count