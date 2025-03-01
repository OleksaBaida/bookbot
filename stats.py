def count_words(string_to_count):
    count = len(string_to_count.split())
    return count

def count_characters(string_to_count):
    count = {}
    for char in string_to_count:
        if char.isalpha():
            char = char.lower()
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1
    return count


def sort_chars(dict_to_sort):
    char_list = [{"char": key, "count": value} for key, value in dict_to_sort.items()]
    char_list.sort(reverse=True, key=lambda item: item["count"])
    return char_list