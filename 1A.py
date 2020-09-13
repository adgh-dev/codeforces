def main():
    _ = input().split(" ")
    n, m, a = [int(i) for i in _]
    if n % a == 0:
        hor = n//a
    else:
        hor = n//a + 1
    if m % a == 0:
        ver = m//a
    else:
        ver = m//a + 1
    print(hor * ver)

if __name__ == "__main__":
    main()