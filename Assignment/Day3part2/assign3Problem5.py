def find_longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

# Take words from user
words_list = input("Enter words separated by space: ").split()

# Call function
result = find_longest_word(words_list)

print("Length of longest word is:", result)
