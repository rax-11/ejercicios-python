number_grid = [
    [1, 2, 3],  # fila 0
    [4, 5, 6],  # fila 1
    [7, 8, 9],  # fila 2
    [0]         # fila 3
]

print(number_grid [0][2])

for row in number_grid: # imprime todo
    print(row)

for row in number_grid: # imprime cada valor dentro de las listas
    for col in row:
        print(col)