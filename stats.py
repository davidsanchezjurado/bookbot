def count_words(file_text):
    arr = file_text.split()
    return len(arr)


def count_characters(file_text):
    dict = {}
    for char in file_text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    list = []
    for key in dictionary:
        if key.isalpha():
            list.append({"name":key, "num": dictionary[key]})
    list.sort(reverse=True, key=sort_on)
    return list