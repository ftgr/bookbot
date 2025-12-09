def words_counter(text):
    words = text.split()
    return len(words)

def characters_counter_from_text(text):
    characters_counter = {}
    text_list = text.split()
    for word in text_list:
        for character in word.lower():
            if character in characters_counter:
                characters_counter[character] += 1
            else:
                characters_counter[character] = 1

    return characters_counter

def sort_on(items):
    return items["num"]

def sorted_list_of_characters_counter(characters_counter):
    letter_list_dic = []
    for letter in characters_counter:
        if letter.isalpha():
            temp = {"char": letter, "num": characters_counter[letter]}
            letter_list_dic.append(temp)
    letter_list_dic.sort(reverse=True, key=sort_on)
    return letter_list_dic

