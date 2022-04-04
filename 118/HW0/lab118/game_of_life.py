import copy

DEAD = 0
ALIVE = 1


def printBoard(board):
    for s in board:
        print(*s)


def inRange(board, pos):
    rows = len(board)
    cols = len(board[0])
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


def getNeighbors(board, pos):
    neighbors = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            potentialNeighbor = [pos[0] + i, pos[1] + j]
            if inRange(board, potentialNeighbor):
                neighbors.append(potentialNeighbor)
    return neighbors


def getNextState(board, pos):
    neighbors = getNeighbors(board, pos)
    neighborsStateCount = [board[n[0]][n[1]] for n in neighbors].count(ALIVE)
    if board[pos[0]][pos[1]] == ALIVE:
        if neighborsStateCount in [2, 3]:
            return ALIVE
        else:
            return DEAD
    else:
        if neighborsStateCount == 3:
            return ALIVE
        else:
            return DEAD


def game_of_life(board, steps):
    newBoard = copy.deepcopy(board)
    rows = len(board)
    cols = len(board[0])
    for step in range(steps):
        for i in range(rows):
            for j in range(cols):
                newBoard[i][j] = getNextState(board, [i, j])
        board = copy.deepcopy(newBoard)
    return newBoard


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialBoard = [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                    [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
                    [DEAD, DEAD, ALIVE, ALIVE, ALIVE, DEAD, DEAD],
                    [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                    [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]]
    print("initial_board: ")
    printBoard(initialBoard)
    wantedBoard = [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                   [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
                   [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
                   [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
                   [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]]
    print("wanted_board: ")
    printBoard(wantedBoard)

    resBoard = game_of_life(board=initialBoard, steps=1)

    print("resBoard: ")
    printBoard(resBoard)
    assert(resBoard == wantedBoard)
    unwantedBoard = [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
                   [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
                   [DEAD, DEAD, ALIVE, DEAD, ALIVE, DEAD, DEAD],
                   [DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD, DEAD],
                   [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, ALIVE]]
    assert(resBoard != unwantedBoard)
