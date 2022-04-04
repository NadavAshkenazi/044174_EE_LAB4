def printMatrix(m):
    for s in m:
        print(*s)


def vectorMul(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += (v1[i] * v2[i])
    return res


def getColumn(m, index):
    return [row[index] for row in m]


def getRow(m, index):
    return m[index]


def mat_mul(mat1, mat2):
    mat1Size = {"rows": len(mat1), "cols": len(mat1[0])}
    mat2Size = {"rows": len(mat2), "cols": len(mat2[0])}
    # (sigma from k = 0 to k = n-1 of Aik*Bkj) for each col of m2 and row of m1
    return [[vectorMul(getRow(mat1, i), getColumn(mat2, j)) for j in range(mat2Size["cols"])] for i in
            range(mat1Size["rows"])]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    mat2 = [[9, 10, 11], [12, 13, 14]]

    wantedMatrix = [[33, 36, 39], [75, 82, 89], [117, 128, 139], [159, 174, 189]]

    assert (mat_mul(mat1, mat2) == wantedMatrix)

    mat1 = [[1, 2], [3, 4], [5, 6]]
    mat2 = [[1, 2, 3], [4, 5, 6]]

    wantedMatrix = [[9, 12, 15], [19, 26, 33], [29, 40, 51]]

    assert (mat_mul(mat1, mat2) == wantedMatrix)
