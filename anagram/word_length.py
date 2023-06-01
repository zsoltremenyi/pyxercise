def word_length(word1, word2):
    word_length1 = 0
    word_length2 = 0
    for i in word1:
        word_length1 += 1
    for i in word2:
        word_length2 += 1
    return [word_length1, word_length2]