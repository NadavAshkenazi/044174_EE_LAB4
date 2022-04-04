import os


def printMatrix(matrix):
    for s in matrix:
        print(*s)


def writeMatrix(filename="matrix.txt", matrixString="5 4 1 8\n5 2 9 6\n7 3 3 2"):
    with open(filename, "a") as f:
        f.write(matrixString)


def getMatrix(filename="matrix.txt"):
    matrix = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            matrix.append([int(i) for i in line.split("\n")[0].split(" ")])
    # printMatrix(matrix)
    return matrix


def inRange(matrix, pos):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


def findHeaviestPathAux(matrix, initialPos, endPos):
    if initialPos[0] == endPos[0] and initialPos[1] == endPos[1]:
        return [matrix[endPos[0]][endPos[1]]]

    rightPos = [initialPos[0], initialPos[1] + 1]
    downPos = [initialPos[0] + 1, initialPos[1]]

    positionElement = matrix[initialPos[0]][initialPos[1]]
    rightHeaviestPath = [0]
    downHeaviestPath = [0]

    if inRange(matrix, rightPos):
        rightHeaviestPath = findHeaviestPathAux(matrix, rightPos, endPos)
    if inRange(matrix, downPos):
        downHeaviestPath = findHeaviestPathAux(matrix, downPos, endPos)

    if sum(rightHeaviestPath) > sum(downHeaviestPath):
        return [positionElement] + rightHeaviestPath
    else:
        return [positionElement] + downHeaviestPath


def findHeaviestPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return findHeaviestPathAux(matrix, [0, 0], endPos=[rows - 1, cols - 1])


def two_ways_path_sum(filename):
    matrix = getMatrix(filename)
    return findHeaviestPath(matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if os.path.exists("matrix.txt"):
        os.remove("matrix.txt")
    writeMatrix()
    res = two_ways_path_sum("matrix.txt")
    assert (res == [5, 5, 2, 9, 6, 2])

    if os.path.exists("matrix2.txt"):
        os.remove("matrix2.txt")
    writeMatrix(filename="matrix2.txt", matrixString="5 4 1 100\n5 2 9 6\n7 3 3 2")
    res2 = two_ways_path_sum("matrix2.txt")
    assert (res2 == [5, 4, 1, 100, 6, 2])
