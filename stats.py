def get_text_count(text):
    word_count = len(text.split())
    return word_count


def get_each_text_count(text):
    lower_text = text.lower()
    char_count = {}
    for ch in lower_text:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count
def sort_on(items):
    return items["num"]


def sort_distionary(distionary):
    sorted_list_distinaries = []
    for items in distionary:
        if not items.strip():
            continue
        new_dist = {"char" : items , "num" : distionary[items]}
        sorted_list_distinaries.append(new_dist)
    sorted_list_distinaries.sort(reverse=True, key=sort_on )
    # print(sorted_list_distinaries)
    return sorted_list_distinaries

sort_distionary({'\ufeff': 1, 't': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7631, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2})