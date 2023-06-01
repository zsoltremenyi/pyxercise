from word_length import word_length


def comparing(first_word, second_word):
    length = word_length(first_word, second_word)
    counter = 0
    for i in first_word:
        if i in second_word:
            counter += 1

    if counter == length[0] and length[0] == length[1]:
        print(f"{first_word} and {second_word} are anagrams.")
    else:
        print(f"{first_word} and {second_word} are not anagrams.")