def main():
    num_lines = int(input())
    lines = []
    while num_lines > 0:
        lines.append(input())
        num_lines -= 1

    solutions = 0
    for line in lines:
        arr = [int(i) for i in line.split(" ")]
        if sum(arr) > 1:
            solutions += 1

    print(solutions)

if __name__ == "__main__":
    main()