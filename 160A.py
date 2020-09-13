def main():
    num_coins = int(input())
    values = [int(i) for i in input().split(" ")]
    total = sum(values)

    values.sort(reverse=True)

    s = 0
    i = 0
    while s <= total // 2:
        s += values[i]
        i += 1

    print(i)

if __name__ == "__main__":
    main()