def translate(text):
    result = ""
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch.isalpha() and ch not in vowels:
            result += ch + "o" + ch
        else:
            result += ch

    return result

print(translate("this is fun"))