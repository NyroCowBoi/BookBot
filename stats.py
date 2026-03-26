def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}
    for word in text:
        if word not in characters:
            characters[word] = 1
        else:
            characters[word] += 1
    return characters

def sorted_list(dictionary):
    new_list = []
    for k in dictionary:
        new_list.append({"char": k, "num": dictionary[k]})

    def sort_on(dict):
        return dict["num"]
    
    new_list.sort(reverse=True, key=sort_on)
    
    return new_list