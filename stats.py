def word_count(text):
    num_words = 0
    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def char_count(text):
    char_dict = {}

    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

