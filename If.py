is_male = False
is_tall = True

if is_male :
    print("Eres hombre")
else:
    print("No eres hombre")

if is_male or is_tall:
    print("Eres hombre o alto o ambos")
else:
    print("No eres hombre o alto")

if is_male and is_tall:
    print("Eres hombre alto")
else:
    print("No eres hombre alto")

if is_male and is_tall:
    print("Eres hombre alto")
elif is_male and not (is_tall):
    print("Eres un hombre pequeño")
elif not(is_male) and (is_tall):
    print("No eres hombre pero eres alto")
else:
    print("No eres hombre o alto")