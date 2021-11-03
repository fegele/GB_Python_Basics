def int_func(word):
    """Returns a capitalized word

    Parameters:
    word (string)

    Returns:
    string: capitalized argument
    """
    result = word[0].upper() + word[1:].lower()
    return result


def int_func_ext(sentence):
    """Takes a string, splits it by spaces and returns a string of capitalized elements

    Parameters:
    sentence (string) - a string of words with spaces in between

    Returns:
    string: a string of capitalized words
    """
    word_list = []
    for word in sentence.split():
        word_list.append(int_func(word))
    result = ' '.join(word_list)
    return result


input_word = input("Enter a word: ")
print(int_func(input_word))

input_sentence = input("Enter a sentence: ")
print(int_func_ext(input_sentence))
