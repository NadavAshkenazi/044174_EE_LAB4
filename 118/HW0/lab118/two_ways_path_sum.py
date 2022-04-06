import copy
import os
import sys


def printMatrix(matrix):
    for s in matrix:
        print(*s)


def writeMatrix(filename, matrixString):
    with open(filename, "a") as f:
        f.write(matrixString)


def getMatrix(filename):
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


def findHeaviestPath(matrix):
    endPos = [len(matrix) - 1, len(matrix[0]) - 1]
    weightMatrix = copy.deepcopy(matrix)
    for a in range(len(weightMatrix)):
        for b in range(len(weightMatrix[0])):
            weightMatrix[a][b] = {"weight": -float('inf'), "path": []}
    for i in range(endPos[0], -1, -1):
        for j in range(endPos[1], -1, -1):
            rightPos = [i, j + 1]
            downPos = [i + 1, j]
            if [i, j] == endPos:
                weightMatrix[i][j] = {"weight": matrix[i][j], "path": [matrix[i][j]]}
            else:
                if inRange(matrix, rightPos):
                    rightWeight = weightMatrix[rightPos[0]][rightPos[1]]["weight"]
                else:
                    rightWeight = -float('inf')
                if inRange(matrix, downPos):
                    downWeight = weightMatrix[downPos[0]][downPos[1]]["weight"]
                else:
                    downWeight = -float('inf')

                if rightWeight > downWeight:
                    weightMatrix[i][j]["weight"] = matrix[i][j] + rightWeight
                    weightMatrix[i][j]["path"] = [matrix[i][j]] + weightMatrix[rightPos[0]][rightPos[1]]["path"]
                else:
                    weightMatrix[i][j]["weight"] = matrix[i][j] + downWeight
                    weightMatrix[i][j]["path"] = [matrix[i][j]] + weightMatrix[downPos[0]][downPos[1]]["path"]
    print("matrix")
    printMatrix(matrix)
    print("weightMatrix")
    printMatrix(weightMatrix)
    return weightMatrix[0][0]["path"]


def two_ways_path_sum(filename):
    matrix = getMatrix(filename)
    return findHeaviestPath(matrix)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     filename = r"Test\matrix.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="5 4 1 8\n5 2 9 6\n7 3 3 2")
#     res = two_ways_path_sum(filename)
#     assert (res == [5, 5, 2, 9, 6, 2])
#
#     filename = r"Test\matrix2.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="5 4 1 100\n5 2 9 6\n7 3 3 2")
#     res2 = two_ways_path_sum(filename)
#     assert (res2 == [5, 4, 1, 100, 6, 2])
#
#     filename = r"Test\matrix3.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="-5 -4 -1 -8\n-5 -2 -9 -6\n-7 -3 -3 -2")
#     res3 = two_ways_path_sum(filename)
#     assert (res3 == [-5, -4, -2, -3, -3, -2])
#
#     filename = r"Test\matrix4.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="-2 1 -3\n-1 -1 8\n-1 -1 -5\n-1 -1 1")
#     res4 = two_ways_path_sum(filename)
#     assert (res4 == [-2, 1, -1, 8, -5, 1])
#
#     filename = r"Test\matrix5.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="1 1 1 1 1\n-2 1 1 1 1\n-2 1 1 1 1\n100 1 1 1 1")
#     res5 = two_ways_path_sum(filename)
#     assert (res5 == [1, -2, -2, 100, 1, 1, 1, 1])
#
#     filename = r"Test\matrix6.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#     writeMatrix(filename=filename, matrixString="1 1 1\n1 1 11\n100 10 5")
#     res5 = two_ways_path_sum(filename)
#     assert (res5 == [1,1,100,10,5])
