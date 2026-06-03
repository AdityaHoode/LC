matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

rows = len(matrix)
cols = len(matrix[0])

flat_index = 5

row = flat_index // cols
col = flat_index % cols

reproduce_flat_index = row * cols + col

print(f"Flat index      : {flat_index}")
print(f"Row             : {row}")
print(f"Column          : {col}")
print(f"Matrix value    : {matrix[row][col]}")
print(f"Recreated index : {reproduce_flat_index}")