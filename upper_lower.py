

def upper_lower(word):
    lowercase = word.lower()
    uppercase = word.upper()
    processed_output = lowercase + " " + uppercase
    print(processed_output)


def printing_letters(word):
    for character in word:
        print(character)


def main():
    user_input = input("Please write what you would like to have converted to upper and lower case:")
    upper_lower(user_input)
    printing_letters(user_input)


if __name__ == '__main__':
    main()
