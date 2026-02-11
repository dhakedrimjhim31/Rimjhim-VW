def filter_long_words(words, length):
    long_words = []
    for word in words:
        if len(word) > length:
            long_words.append(word)
    return long_words

# Take list of words from user
words_list = input("Enter words separated by space: ").split()

# Take length from user
length = int(input("Enter the minimum length: "))

# Call function
result = filter_long_words(words_list, length)

print("Words longer than", length, "are:", result)