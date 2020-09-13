# f(n) =  - 1 + 2 - 3 + .. + ( - 1) n n

def main():
    # todo
    n = int(input())
    if n % 2 == 0:
        evens = n // 2
        odds = n // 2
    else:
        evens = n // 2 - 1
        odds = n // 2

    print(odds, evens)
if __name__ == "__main__":
    main()