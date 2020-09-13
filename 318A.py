def main():
    _ = input().split(" ")
    n, k = [int(i) for i in _]
    if n % 2 == 0:
        last_odd_index = n // 2
    else:
        last_odd_index = n // 2 + 1

    if k > last_odd_index:
        # even number
        k = k - last_odd_index
        print(k * 2)
    else:
        print(k * 2 - 1)

if __name__ == "__main__":
    main()