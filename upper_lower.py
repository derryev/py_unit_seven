

def upper_lower(word):
    lowercase = word.lower()
    uppercase = word.upper()
    processed_output = lowercase + " " + uppercase
    print(processed_output)


def main():
    user_input = input("Please write what you would like to have converted to upper and lower case:")
    upper_lower(user_input)


if __name__ == '__main__':
    main()
