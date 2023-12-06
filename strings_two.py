def four_letters(phrase):
    split_word_list = phrase.split(" ")
    new_censored_list = []
    print(split_word_list)
    for word in split_word_list:
        if "," in word:
            length = len(word)-1
            if length == 4:
                word = "#$%@"
            else:
                word = word
        else:
            length = len(word)
            if length == 4:
                word = "#$%@"
            else:
                word = word
        new_censored_list.append(word)
    final_sentence = " ".join(new_censored_list)
    return final_sentence


def bubble_sort(words):
    new_list = words.split(" ")
    for x in range(len(new_list)):
        for word in new_list:
            if word > x:


    return sorted_list

def main():
    print(four_letters("We know what we are, but know not what we may be"))
    print(bubble_sort("Karen, Brian"))

main()
