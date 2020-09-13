def main():
    _ = input().split(" ")
    n, m = [int(i) for i in _]

    if n < 1 or m < 1:
        return 0
    if n == 1 and m == 1:
        return 0
    if n == 1:
        return m // 2
    if m == 1:
        return n // 2

    if n % 2 == 0 or m % 2 == 0:
        return n * m // 2
    else:
        result = (n - 1) * (m - 1) // 2
        if n > 1 and m > 1:
            result += (n + m - 1) // 2
        return result
    return None

if __name__ == "__main__":
    print(main())