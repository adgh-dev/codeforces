def main():
    lines = 0

    matrix = []
    target_index = 2

    while lines < 5:
        matrix.append(input().split(" "))
        lines += 1

    line = 0
    while line < len(matrix):
        if "1" in matrix[line]:
            break
        line += 1
    moves = abs(line - target_index)

    pos = 0
    while pos < len(matrix[line]):
        if matrix[line][pos] == "1":
            moves += abs(pos - target_index)
            break
        pos += 1

    print(moves)

if __name__ == "__main__":
    main()