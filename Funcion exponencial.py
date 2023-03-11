print(2**3)

def elevar_al_poder(num_base, num_poder):
    result = 1
    for index in range(num_poder):
        result = result * num_base
    return result

print(elevar_al_poder(3,4))