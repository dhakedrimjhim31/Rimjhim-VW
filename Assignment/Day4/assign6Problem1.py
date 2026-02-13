def rot13(text):
    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += ch  # keep spaces and punctuation

    return result

# Secret message
message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq !"

decoded = rot13(message)
print("Decoded Message:")
print(decoded)