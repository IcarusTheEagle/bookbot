def word_count(text):
    num_words = 0

    words = text.split()
    for word in words:
        num_words += 1
    return num_words

def char_count(text):
    char_dict = {}

    for char in text:
        if char.isalpha():
            char_dict.get(char.lower(), 0)
            char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict

def sort_key(dict):
    return dict["num"]

def sort_list(char_dict):
    char_dict_list = []
    my_dict = {}

    for k in char_dict:
        my_dict = {"char": k, "num": char_dict[k]}
        char_dict_list.append(my_dict)

    char_dict_list.sort(reverse=True, key=sort_key)
    return char_dict_list