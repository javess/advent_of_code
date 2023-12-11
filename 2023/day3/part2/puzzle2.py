test_files = [
    './2023/day3/part2/inputs_simple.txt',
    './2023/day3/part2/inputs_full.txt'
]

matchedNumbers = set()


def isPieceValidated(matrix, i, j):
    isValid = False
    isGear = False
    gearPair = None
    for ii in range(max(0, i-1), min(len(matrix), i+2)):
        for jj in range(max(0, j-1), min(len(matrix[i]), j+2)):
            symbol = matrix[ii][jj]
            if symbol.isdigit() or symbol == '.':
                continue
            else:
                # print(f"Found validating symbol {symbol} at [{ii}][{jj}]")
                if (symbol == '*'):
                    isGear = True
                    gearPair = [ii, jj]
                isValid = True
    return (isValid, isGear, gearPair)


def checkForGearMatch(matrix, initRow, initCol, initColEnd, gearPair):
    (gear_i, gear_j) = gearPair

    for ii in range(max(0, gear_i-1), min(len(matrix), gear_i+2)):
        for jj in range(max(0, gear_j-1), min(len(matrix[i]), gear_j+2)):
            if ii == initRow and jj <= initColEnd and jj >= initCol:
                continue

            if (matrix[ii][jj].isdigit()):
                # found other number, search forward and backwards in the row
                row = ii
                start_col = jj
                end_col = jj
                while start_col >= 0 and matrix[row][start_col].isdigit():
                    start_col = start_col - 1
                start_col = max(start_col+1, 0)

                while end_col < len(matrix[row]) and matrix[row][end_col].isdigit():
                    end_col = end_col + 1

                xx = (initRow, initCol, initColEnd)
                yy = (row, start_col, end_col)

                if xx not in matchedNumbers and yy not in matchedNumbers:
                    matchedNumbers.add(xx)
                    matchedNumbers.add(yy)

                    a = int(matrix[initRow][initCol:initColEnd])
                    b = int(matrix[row][start_col:end_col])
                    return a*b
    return 0


def checkIsValidPart(matrix, i, j):
    currJ = j
    isValid = False
    isGear = False
    gearPair = None
    while currJ < len(matrix[i]) and matrix[i][currJ].isdigit():
        (isValid, isGear, gearPair) = isPieceValidated(matrix, i, currJ)
        if (isValid):
            while currJ < len(matrix[i]) and matrix[i][currJ].isdigit():
                currJ = currJ + 1
        else:
            currJ = currJ + 1
    gearValue = 0
    if (isGear):
        gearValue = checkForGearMatch(matrix, i, j, currJ, gearPair)

    return (isValid, int(matrix[i][j:currJ]), currJ, gearValue)


def isValidPart(matrix, i, j):
    if (matrix[i][j].isdigit()):
        (val, number, idx, gearValue) = checkIsValidPart(matrix, i, j)
        # if not val:
        #     print(f"Discarding found number {number} @ [{i}][{j}]")
        # else:
        #     print(f"Accepting found number {number} @ [{i}][{j}]")
        return (val, number, idx, gearValue)
    else:
        return (False, 0, j+1, 0)


for test_file in test_files:
    print(test_file)
    total = 0
    totalGearValue = 0
    matrix = []
    with open(test_file) as file:
        for line in file:
            matrix.append(line.strip())

        for i in range(len(matrix)):
            j = 0
            while j < len(matrix[i]):
                (isValid, pieceNo, nextJ, gearValue) = isValidPart(matrix, i, j)
                if (isValid):
                    total = total + pieceNo
                totalGearValue = totalGearValue + gearValue
                j = nextJ

    print(total)
    print(totalGearValue)
