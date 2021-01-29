def removeIslands(matrix):
    visited = set()
    for row in range(1,len(matrix) - 1):
        for col in range(1, len(matrix[0]) - 1):
            islandMembers = []
            validIsland = False

            if matrix[row][col] == 1:
                validIsland = validateAndFindIslandMembers(
                    row, col, islandMembers, matrix, visited)

            if validIsland and len(islandMembers) > 0:
                removeIsland(islandMembers, matrix)

    return matrix


def validateAndFindIslandMembers(row, col, islandMembers, matrix, visited):
    validIsland = True
    isOne = matrix[row][col] == 1
    key = str(row) + "-" + str(col)

    if key in visited:
        return True

    visited.add(key)
    upperNeighbor, bottomNeighbor, leftNeighbor, rightNeighbor = findNeighbors(
        row, col, matrix)

    # check for invalid neighbors
    validIsland &= checkNeighbor(
        upperNeighbor, row-1, col, islandMembers, matrix, visited)
    validIsland &= checkNeighbor(
        bottomNeighbor, row+1, col, islandMembers, matrix, visited)
    validIsland &= checkNeighbor(
        leftNeighbor, row, col-1, islandMembers, matrix, visited)
    validIsland &= checkNeighbor(
        rightNeighbor, row, col+1, islandMembers, matrix, visited)

    if isOne and validIsland:
        islandMembers.append((row, col))
    return validIsland


def checkNeighbor(neighbor, row, col, islandMembers, matrix, visited):
    validNeighborIsland = True
    isOne = neighbor == 1
    rowIsBorder = row == 0 or row == len(matrix) - 1
    colIsBorder = col == 0 or col == len(matrix[0]) - 1

    if neighbor is None:
        return True
    if isOne and (colIsBorder or rowIsBorder):
        return False
    elif isOne:
        validNeighborIsland = validateAndFindIslandMembers(
            row, col, islandMembers, matrix, visited)

    return validNeighborIsland


def findNeighbors(row, col, matrix):
    upperNeighbor, bottomNeighbor, leftNeighbor, rightNeighbor = None, None, None, None
    if row > 0:
        upperNeighbor = matrix[row-1][col]
    if row < len(matrix) - 1:
        bottomNeighbor = matrix[row+1][col]
    if col > 0:
        leftNeighbor = matrix[row][col-1]
    if col < len(matrix[0]) - 1:
        rightNeighbor = matrix[row][col+1]

    return upperNeighbor, bottomNeighbor, leftNeighbor, rightNeighbor


def removeIsland(islandMembers, matrix):
    for islandMember in islandMembers:
        matrix[islandMember[0]][islandMember[1]] = 0


""" ************************************************************************

************************************************************************ """

matrix = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0],
          [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]]

print(matrix)
matrix2 = removeIslands(matrix)
print(matrix2)
