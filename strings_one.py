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
    pass


def title_case(sentence):
    pass

def main():
    #input("What word would you like to use?")
    word = "bread"
    print(half_slice(word))
    print(no_first_last("python"))
main()
