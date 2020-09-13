
def main():
    n, k = [int(i) for i in input().split(" ")]

    total_minutes = 4 * 60
    remaining_minutes = total_minutes - k

    print(remaining_minutes)

    problems_time = [5, 10, 15]
    total_problems_time = (n * (n + 1) / 2) * 5


if __name__ == "__main__":
    main()