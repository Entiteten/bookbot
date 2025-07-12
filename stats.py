def word_count(text):
    words = text.split()
    return len(words)

def chars_dict(text):
    chars = {}
    #lowered = text.lower()
    for lowered in text.lower():
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(result):
    return result["num"]

def sort_chars(characters):
    result = []
    for char, num in characters.items():
        if char.isalpha():
            result.append({"char": char, "num": num})
    result.sort(reverse=True, key=sort_on)
    return result



#def sort_chars(chars_dict):
    #sorted = list(chars_dict.items())
    #sorted = []
    #char = chars_dict.split(0)
    #num = chars_dict.split(1)
    #for i in chars_dict:
    #    sorted.append()
    #sorted.sort(reverse=True, key=sort_on)
    #return sorted
