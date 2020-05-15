X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[9, 8, 7, 6],
     [6, 5, 4, 3],
     [3, 2, 1, 2]]
Z = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0 ,0, 0]]
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through row of Y
        for k in range(len(Y)):
            Z[i][j] += X[i][k] * Y[k][j]
for r in Z:
    print(r)