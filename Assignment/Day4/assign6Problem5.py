text = input("Enter a string: ")

# replace only whole word 'this'
words = text.split()

new_words = []

for word in words:
    if word == "this":
        new_words.append("That")
    else:
        new_words.append(word)

result = " ".join(new_words)

print("Output:", result)