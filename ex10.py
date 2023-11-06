a = 7
import random
matrix = []
for i in range(a):
    c = []
    for j in range(a):
        ele = random.randint(0, 9)
        c.append(ele)
    matrix.append(c)

for i in range(a):
    for j in range(a):
        print(matrix[i][j], end=" ")
    print()

print("----------------------")
max_column_sum = -1
for j in range(a):
    s = 0
    for i in range(a):
        s += matrix[i][j]
    print(f" {j + 1} syan gumar: {s}")
    if s > max_column_sum:
        max_column_sum = s

print(max_column_sum)

