n = input()
d = [int(x) for x in n.split(',')]
rowNum = d[0]
colNum = d[1]

mat = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        mat[row][col] = row*col

print(mat)
