test_files = [
    './2023/day3/part1/inputs_simple.txt',
    './2023/day3/part1/inputs_full.txt'
]


def isPieceValidated(matrix, i, j):
    for ii in range(max(0, i-1), min(len(matrix), i+2)):
        for jj in range(max(0, j-1), min(len(matrix[i]), j+2)):
            symbol = matrix[ii][jj]
            if symbol.isdigit() or symbol == '.':
                continue
            else:
                # print(f"Found validating symbol {symbol} at [{ii}][{jj}]")
                return True
    return False


def checkIsValidPart(matrix, i, j):
    currJ = j
    isValid = False
    while currJ < len(matrix[i]) and matrix[i][currJ].isdigit():
        if (isPieceValidated(matrix, i, currJ)):
            isValid = True
        currJ = currJ + 1

    return (isValid, int(matrix[i][j:currJ]), currJ)


def isValidPart(matrix, i, j):
    if (matrix[i][j].isdigit()):
        (val, number, idx) = checkIsValidPart(matrix, i, j)
        # if not val:
        #     print(f"Discarding found number {number} @ [{i}][{j}]")
        # else:
        #     print(f"Accepting found number {number} @ [{i}][{j}]")
        return (val, number, idx)
    else:
        return (False, 0, j+1)


for test_file in test_files:
    print(test_file)
    total = 0
    matrix = []
    with open(test_file) as file:
        for line in file:
            matrix.append(line.strip())

        for i in range(len(matrix)):
            j = 0
            while j < len(matrix[i]):
                (isValid, pieceNo, nextJ) = isValidPart(matrix, i, j)
                if (isValid):
                    total = total + pieceNo
                j = nextJ

    print(total)
