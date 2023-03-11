def translate(phrase):
    translation = ""                                    # variable donde se va a guardar la respuesta
    for letter in phrase:
        if letter in "AEIOUaeiou":                      # se puede usar if letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation + "G"
            else: translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input(" Pon una frase ")) )