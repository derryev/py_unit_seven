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
    word = input("What word would you like to have its first and last half swapped? ")
    first_last_word = input("What word would you like to have its first and last letters removed? ")
    longest_phrase = input("Please type the phrase with which you want to determine the length of the longest word: ")
    title_sentence = input("Please type the sentence you would like to convert to title case: ")
    print(half_slice(word))
    print(no_first_last(first_last_word))
    print(longest(longest_phrase))
    print(title_case(title_sentence))


main()
