def half_slice(word):
    length = len(word)
    first_half = word[:length//2]
    second_half = word[(length//2):]
    new_word = second_half+first_half
    return new_word


def no_first_last(word):
    new_word = word[1:-1]
    return new_word


def longest(phrase):
    list_of_words = phrase.split(" ")
    longest_word = list_of_words[0]
    for word in list_of_words:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)


def title_case(sentence):
    new_word_list = []
    individual_word_list = sentence.split(" ")
    for word in individual_word_list:
        cap_first_letter = word[0].upper()
        cap_word = cap_first_letter + word[1:]
        new_word_list.append(cap_word)
    final_cap_sentence = " ".join(new_word_list)
    return final_cap_sentence


def main():
    word = "bread"
    print(half_slice(word))
    print(no_first_last("python"))
    print(longest("If you tell the truth you don't have to remember anything"))
    print(title_case("We know what we are, but know not what we may be"))


main()
