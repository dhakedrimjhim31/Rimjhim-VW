text = """Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.Indentation
Python is dynamically typed and garbage-collected.
It supports multiple programming paradigm, including structured, object-oriented and functional programming."""

text = text.lower()

letter_count = {}

for ch in text:
    if ch.isalpha():        #count only letters
        if ch in letter_count:
            letter_count[ch] += 1
        else:
            letter_count[ch] = 1

for letter in sorted(letter_count):
    print(letter, ":", letter_count[letter])