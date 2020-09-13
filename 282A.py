def main():
    n = int(input())
    rez = 0
    while n > 0:
        _ = input()
        n -= 1
        if "++" in _:
            rez += 1
        if "--" in _:
            rez -= 1
    print(rez)

if __name__ == "__main__":
    main()