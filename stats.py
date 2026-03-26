def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}
    for ch in text:
        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1
    return characters

def sorted_list(dictionary):
    new_list = []
    for key in dictionary:
        new_list.append({"char": key, "num": dictionary[key]})

    def sort_on(dict):
        return dict["num"]
    
    new_list.sort(reverse=True, key=sort_on)
    
    return new_list
